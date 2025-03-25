/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as OpikApi from "../../../../api/index";
import * as core from "../../../../core";

export const StartMultipartUploadRequestEntityType: core.serialization.Schema<
    serializers.StartMultipartUploadRequestEntityType.Raw,
    OpikApi.StartMultipartUploadRequestEntityType
> = core.serialization.enum_(["trace", "span"]);

export declare namespace StartMultipartUploadRequestEntityType {
    export type Raw = "trace" | "span";
}
