/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const WorkspaceSpansCount: core.serialization.ObjectSchema<
    serializers.WorkspaceSpansCount.Raw,
    OpikApi.WorkspaceSpansCount
> = core.serialization.object({
    workspace: core.serialization.string().optional(),
    spanCount: core.serialization.property("span_count", core.serialization.number().optional()),
});

export declare namespace WorkspaceSpansCount {
    export interface Raw {
        workspace?: string | null;
        span_count?: number | null;
    }
}
