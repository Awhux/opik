/**
 * This file was auto-generated by Fern from our API Definition.
 */

export type SpanFilterPublicOperator =
    | "contains"
    | "not_contains"
    | "starts_with"
    | "ends_with"
    | "="
    | "!="
    | ">"
    | ">="
    | "<"
    | "<="
    | "is_empty"
    | "is_not_empty";
export const SpanFilterPublicOperator = {
    Contains: "contains",
    NotContains: "not_contains",
    StartsWith: "starts_with",
    EndsWith: "ends_with",
    EqualTo: "=",
    NotEquals: "!=",
    GreaterThan: ">",
    GreaterThanOrEqualTo: ">=",
    LessThan: "<",
    LessThanOrEqualTo: "<=",
    IsEmpty: "is_empty",
    IsNotEmpty: "is_not_empty",
} as const;
