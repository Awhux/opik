package com.comet.opik.domain;

import com.clickhouse.client.ClickHouseException;
import com.comet.opik.api.Dataset;
import com.comet.opik.api.Experiment;
import com.comet.opik.api.ExperimentSearchCriteria;
import com.comet.opik.api.error.EntityAlreadyExistsException;
import com.comet.opik.infrastructure.auth.RequestContext;
import jakarta.inject.Inject;
import jakarta.inject.Singleton;
import jakarta.ws.rs.ClientErrorException;
import jakarta.ws.rs.NotFoundException;
import jakarta.ws.rs.core.Response;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import reactor.core.publisher.Mono;
import reactor.core.scheduler.Schedulers;

import java.util.Set;
import java.util.UUID;

@Singleton
@RequiredArgsConstructor(onConstructor = @__(@Inject))
@Slf4j
public class ExperimentService {

    private final @NonNull ExperimentDAO experimentDAO;
    private final @NonNull DatasetService datasetService;
    private final @NonNull IdGenerator idGenerator;

    public Mono<Experiment.ExperimentPage> find(
            int page, int size, @NonNull ExperimentSearchCriteria experimentSearchCriteria) {
        log.info("Finding experiments by '{}', page '{}', size '{}'", experimentSearchCriteria, page, size);
        return experimentDAO.find(page, size, experimentSearchCriteria);
    }

    public Mono<Experiment> getById(@NonNull UUID id) {
        log.info("Getting experiment by id '{}'", id);
        return experimentDAO.getById(id).switchIfEmpty(Mono.defer(() -> Mono.error(newNotFoundException(id))));
    }

    public Mono<Experiment> create(@NonNull Experiment experiment) {
        var id = experiment.id() == null ? idGenerator.generateId() : experiment.id();
        IdGenerator.validateVersion(id, "Experiment");

        return getOrCreateDataset(experiment)
                .onErrorResume(e -> handleDatasetCreationError(e, experiment).map(Dataset::id))
                .flatMap(datasetId -> create(experiment, id, datasetId))
                .onErrorResume(exception -> handleCreateError(exception, id));
    }

    private Mono<UUID> getOrCreateDataset(Experiment experiment) {
        return Mono.deferContextual(ctx -> {
            String userName = ctx.get(RequestContext.USER_NAME);
            String workspaceId = ctx.get(RequestContext.WORKSPACE_ID);

            return Mono.fromCallable(() -> datasetService.getOrCreate(workspaceId, experiment.datasetName(), userName))
                    .subscribeOn(Schedulers.boundedElastic());
        });
    }

    private Mono<Experiment> create(Experiment experiment, UUID id, UUID datasetId) {
        var newExperiment = experiment.toBuilder().id(id).datasetId(datasetId).build();
        return experimentDAO.insert(newExperiment).thenReturn(newExperiment);
    }

    private Mono<Dataset> handleDatasetCreationError(Throwable throwable, Experiment experiment) {
        if (throwable instanceof EntityAlreadyExistsException) {
            return Mono.deferContextual(ctx -> {
                String workspaceId = ctx.get(RequestContext.WORKSPACE_ID);

                return Mono.fromCallable(() -> datasetService.findByName(workspaceId, experiment.datasetName()))
                        .subscribeOn(Schedulers.boundedElastic());
            });
        }
        return Mono.error(throwable);
    }

    private Mono<Experiment> handleCreateError(Throwable throwable, UUID id) {
        if (throwable instanceof ClickHouseException
                && throwable.getMessage().contains("TOO_LARGE_STRING_SIZE")
                && throwable.getMessage().contains("_CAST(id, FixedString(36))")) {
            return Mono.error(newConflictException(id));
        }
        return Mono.error(throwable);
    }

    private ClientErrorException newConflictException(UUID id) {
        return new ClientErrorException("Already exists experiment with id '%s'".formatted(id),
                Response.Status.CONFLICT);
    }

    private NotFoundException newNotFoundException(UUID id) {
        return new NotFoundException("Not found experiment with id '%s'".formatted(id));
    }

    public Mono<Boolean> validateExperimentWorkspace(@NonNull String workspaceId, @NonNull Set<UUID> experimentIds) {
        if (experimentIds.isEmpty()) {
            return Mono.just(true);
        }

        return experimentDAO.getExperimentWorkspaces(experimentIds)
                .all(experimentWorkspace -> workspaceId.equals(experimentWorkspace.workspaceId()));
    }

}
