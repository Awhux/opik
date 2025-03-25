/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../index";
import * as OpikApi from "../../../../../api/index";
import * as core from "../../../../../core";
import { TraceFilterPublic } from "../../../../types/TraceFilterPublic";

export const TraceSearchStreamRequestPublic: core.serialization.Schema<
    serializers.TraceSearchStreamRequestPublic.Raw,
    OpikApi.TraceSearchStreamRequestPublic
> = core.serialization.object({
    projectName: core.serialization.property("project_name", core.serialization.string().optional()),
    projectId: core.serialization.property("project_id", core.serialization.string().optional()),
    filters: core.serialization.list(TraceFilterPublic).optional(),
    lastRetrievedId: core.serialization.property("last_retrieved_id", core.serialization.string().optional()),
    limit: core.serialization.number().optional(),
    truncate: core.serialization.boolean().optional(),
});

export declare namespace TraceSearchStreamRequestPublic {
    export interface Raw {
        project_name?: string | null;
        project_id?: string | null;
        filters?: TraceFilterPublic.Raw[] | null;
        last_retrieved_id?: string | null;
        limit?: number | null;
        truncate?: boolean | null;
    }
}
