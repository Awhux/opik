import React, { useCallback, useMemo, useRef, useState } from "react";
import { keepPreviousData } from "@tanstack/react-query";
import useLocalStorageState from "use-local-storage-state";
import { ColumnPinningState } from "@tanstack/react-table";
import { Link } from "@tanstack/react-router";
import { ArrowRight } from "lucide-react";
import get from "lodash/get";

import DataTable from "@/components/shared/DataTable/DataTable";
import DataTableNoData from "@/components/shared/DataTableNoData/DataTableNoData";
import ResourceCell from "@/components/shared/DataTableCells/ResourceCell";
import useExperimentsList from "@/api/datasets/useExperimentsList";
import Loader from "@/components/shared/Loader/Loader";
import AddExperimentDialog from "@/components/pages/ExperimentsShared/AddExperimentDialog";
import { Button } from "@/components/ui/button";
import useAppStore from "@/store/AppStore";
import { COLUMN_NAME_ID, COLUMN_SELECT_ID, COLUMN_TYPE } from "@/types/shared";
import { RESOURCE_TYPE } from "@/components/shared/ResourceLink/ResourceLink";
import { Experiment } from "@/types/datasets";
import { convertColumnDataToColumn } from "@/lib/table";
import { formatDate } from "@/lib/date";
import MultiResourceCell from "@/components/shared/DataTableCells/MultiResourceCell";
import FeedbackScoreListCell from "@/components/shared/DataTableCells/FeedbackScoreListCell";

const COLUMNS_WIDTH_KEY = "home-experiments-columns-width";

export const COLUMNS = convertColumnDataToColumn<Experiment, Experiment>(
  [
    {
      id: COLUMN_NAME_ID,
      label: "Experiment",
      type: COLUMN_TYPE.string,
      cell: ResourceCell as never,
      sortable: true,
      customMeta: {
        nameKey: "name",
        idKey: "dataset_id",
        resource: RESOURCE_TYPE.experiment,
        getSearch: (data: Experiment) => ({
          experiments: [data.id],
        }),
      },
    },
    {
      id: "dataset",
      label: "Dataset",
      type: COLUMN_TYPE.string,
      cell: ResourceCell as never,
      customMeta: {
        nameKey: "dataset_name",
        idKey: "dataset_id",
        resource: RESOURCE_TYPE.dataset,
      },
    },
    {
      id: "prompt",
      label: "Prompt commit",
      type: COLUMN_TYPE.list,
      accessorFn: (row) => get(row, ["prompt_versions"], []),
      cell: MultiResourceCell as never,
      customMeta: {
        nameKey: "commit",
        idKey: "prompt_id",
        resource: RESOURCE_TYPE.prompt,
        getSearch: (data: Experiment) => ({
          activeVersionId: get(data, "id", null),
        }),
      },
    },
    {
      id: "trace_count",
      label: "Trace count",
      type: COLUMN_TYPE.number,
    },
    {
      id: "feedback_scores",
      label: "Feedback scores",
      type: COLUMN_TYPE.numberDictionary,
      accessorFn: (row) => get(row, "feedback_scores", []),
      cell: FeedbackScoreListCell as never,
    },
    {
      id: "created_at",
      label: "Created",
      type: COLUMN_TYPE.time,
      accessorFn: (row) => formatDate(row.created_at),
      sortable: true,
    },
    {
      id: "last_updated_at",
      label: "Last updated",
      type: COLUMN_TYPE.time,
      accessorFn: (row) => formatDate(row.last_updated_at),
      sortable: true,
    },
  ],
  {},
);

export const DEFAULT_COLUMN_PINNING: ColumnPinningState = {
  left: [COLUMN_SELECT_ID, COLUMN_NAME_ID],
  right: [],
};

const EvaluationSection: React.FunctionComponent = () => {
  const workspaceName = useAppStore((state) => state.activeWorkspaceName);

  const resetDialogKeyRef = useRef(0);
  const [openDialog, setOpenDialog] = useState<boolean>(false);

  const { data, isPending } = useExperimentsList(
    {
      workspaceName,
      page: 1,
      size: 5,
    },
    {
      placeholderData: keepPreviousData,
    },
  );

  const experiments = useMemo(() => data?.content ?? [], [data?.content]);
  const noDataText = "There are no experiments yet";

  const [columnsWidth, setColumnsWidth] = useLocalStorageState<
    Record<string, number>
  >(COLUMNS_WIDTH_KEY, {
    defaultValue: {},
  });

  const resizeConfig = useMemo(
    () => ({
      enabled: true,
      columnSizing: columnsWidth,
      onColumnResize: setColumnsWidth,
    }),
    [columnsWidth, setColumnsWidth],
  );

  const handleNewExperimentClick = useCallback(() => {
    setOpenDialog(true);
    resetDialogKeyRef.current = resetDialogKeyRef.current + 1;
  }, []);

  if (isPending) {
    return <Loader />;
  }

  return (
    <div className="pb-4 pt-2">
      <h2 className="comet-body-accented truncate break-words pb-3">
        Evaluation
      </h2>
      <DataTable
        columns={COLUMNS}
        data={experiments}
        resizeConfig={resizeConfig}
        columnPinning={DEFAULT_COLUMN_PINNING}
        noData={
          <DataTableNoData title={noDataText}>
            <Button variant="link" onClick={handleNewExperimentClick}>
              Create new experiment
            </Button>
          </DataTableNoData>
        }
      />
      <div className="flex justify-end pt-1">
        <Link to="/$workspaceName/experiments" params={{ workspaceName }}>
          <Button variant="ghost" className="flex items-center gap-1 pr-0">
            All experiments <ArrowRight className="size-4" />
          </Button>
        </Link>
      </div>
      <AddExperimentDialog
        key={resetDialogKeyRef.current}
        open={openDialog}
        setOpen={setOpenDialog}
      />
    </div>
  );
};

export default EvaluationSection;
