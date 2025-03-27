# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.automation_rule_evaluator_page_public import (
    AutomationRuleEvaluatorPagePublic,
)
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.automation_rule_evaluator_write import AutomationRuleEvaluatorWrite
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.automation_rule_evaluator_public import AutomationRuleEvaluatorPublic
from ..core.jsonable_encoder import jsonable_encoder
from ..types.automation_rule_evaluator_update import AutomationRuleEvaluatorUpdate
from ..types.log_page import LogPage
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AutomationRuleEvaluatorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_evaluators(
        self,
        *,
        project_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPagePublic:
        """
        Find project Evaluators

        Parameters
        ----------
        project_id : typing.Optional[str]

        name : typing.Optional[str]

        page : typing.Optional[int]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPagePublic
            Evaluators resource

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.find_evaluators()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/automations/evaluators",
            method="GET",
            params={
                "project_id": project_id,
                "name": name,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPagePublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPagePublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_automation_rule_evaluator(
        self,
        *,
        request: AutomationRuleEvaluatorWrite,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create automation rule evaluator

        Parameters
        ----------
        request : AutomationRuleEvaluatorWrite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik import AutomationRuleEvaluatorWrite_LlmAsJudge, OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.create_automation_rule_evaluator(
            request=AutomationRuleEvaluatorWrite_LlmAsJudge(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/automations/evaluators",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=AutomationRuleEvaluatorWrite,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_automation_rule_evaluator_batch(
        self,
        *,
        ids: typing.Sequence[str],
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete automation rule evaluators batch

        Parameters
        ----------
        ids : typing.Sequence[str]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.delete_automation_rule_evaluator_batch(
            ids=["ids"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/automations/evaluators/delete",
            method="POST",
            params={
                "project_id": project_id,
            },
            json={
                "ids": ids,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_evaluator_by_id(
        self,
        id: str,
        *,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPublic:
        """
        Get automation rule by id

        Parameters
        ----------
        id : str

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPublic
            Automation Rule resource

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.get_evaluator_by_id(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/evaluators/{jsonable_encoder(id)}",
            method="GET",
            params={
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_automation_rule_evaluator(
        self,
        id: str,
        *,
        request: AutomationRuleEvaluatorUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update Automation Rule Evaluator by id

        Parameters
        ----------
        id : str

        request : AutomationRuleEvaluatorUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik import AutomationRuleEvaluatorUpdate_LlmAsJudge, OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.update_automation_rule_evaluator(
            id="id",
            request=AutomationRuleEvaluatorUpdate_LlmAsJudge(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/evaluators/{jsonable_encoder(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=AutomationRuleEvaluatorUpdate,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_evaluator_logs_by_id(
        self,
        id: str,
        *,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogPage:
        """
        Get automation rule evaluator logs by id

        Parameters
        ----------
        id : str

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogPage
            Automation rule evaluator logs resource

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.get_evaluator_logs_by_id(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/evaluators/{jsonable_encoder(id)}/logs",
            method="GET",
            params={
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LogPage,
                    parse_obj_as(
                        type_=LogPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAutomationRuleEvaluatorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find_evaluators(
        self,
        *,
        project_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPagePublic:
        """
        Find project Evaluators

        Parameters
        ----------
        project_id : typing.Optional[str]

        name : typing.Optional[str]

        page : typing.Optional[int]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPagePublic
            Evaluators resource

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.find_evaluators()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/automations/evaluators",
            method="GET",
            params={
                "project_id": project_id,
                "name": name,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPagePublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPagePublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_automation_rule_evaluator(
        self,
        *,
        request: AutomationRuleEvaluatorWrite,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create automation rule evaluator

        Parameters
        ----------
        request : AutomationRuleEvaluatorWrite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi, AutomationRuleEvaluatorWrite_LlmAsJudge

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.create_automation_rule_evaluator(
                request=AutomationRuleEvaluatorWrite_LlmAsJudge(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/automations/evaluators",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=AutomationRuleEvaluatorWrite,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_automation_rule_evaluator_batch(
        self,
        *,
        ids: typing.Sequence[str],
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete automation rule evaluators batch

        Parameters
        ----------
        ids : typing.Sequence[str]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.delete_automation_rule_evaluator_batch(
                ids=["ids"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/automations/evaluators/delete",
            method="POST",
            params={
                "project_id": project_id,
            },
            json={
                "ids": ids,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_evaluator_by_id(
        self,
        id: str,
        *,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPublic:
        """
        Get automation rule by id

        Parameters
        ----------
        id : str

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPublic
            Automation Rule resource

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.get_evaluator_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/evaluators/{jsonable_encoder(id)}",
            method="GET",
            params={
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_automation_rule_evaluator(
        self,
        id: str,
        *,
        request: AutomationRuleEvaluatorUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update Automation Rule Evaluator by id

        Parameters
        ----------
        id : str

        request : AutomationRuleEvaluatorUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi, AutomationRuleEvaluatorUpdate_LlmAsJudge

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.update_automation_rule_evaluator(
                id="id",
                request=AutomationRuleEvaluatorUpdate_LlmAsJudge(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/evaluators/{jsonable_encoder(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=AutomationRuleEvaluatorUpdate,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_evaluator_logs_by_id(
        self,
        id: str,
        *,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogPage:
        """
        Get automation rule evaluator logs by id

        Parameters
        ----------
        id : str

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogPage
            Automation rule evaluator logs resource

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.get_evaluator_logs_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/evaluators/{jsonable_encoder(id)}/logs",
            method="GET",
            params={
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LogPage,
                    parse_obj_as(
                        type_=LogPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
