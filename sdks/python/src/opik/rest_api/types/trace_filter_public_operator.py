# This file was auto-generated by Fern from our API Definition.

import typing

TraceFilterPublicOperator = typing.Union[
    typing.Literal[
        "contains",
        "not_contains",
        "starts_with",
        "ends_with",
        "=",
        "!=",
        ">",
        ">=",
        "<",
        "<=",
        "is_empty",
        "is_not_empty",
    ],
    typing.Any,
]
