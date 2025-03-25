# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..core.pydantic_utilities import parse_obj_as
from ..errors.not_found_error import NotFoundError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper


class RedirectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def datasets_redirect(
        self,
        *,
        dataset_id: str,
        path: str,
        workspace_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create dataset redirect url

        Parameters
        ----------
        dataset_id : str

        path : str

        workspace_name : typing.Optional[str]

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
        client.redirect.datasets_redirect(
            dataset_id="dataset_id",
            path="path",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/session/redirect/datasets",
            method="GET",
            params={
                "dataset_id": dataset_id,
                "workspace_name": workspace_name,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def experiments_redirect(
        self,
        *,
        dataset_id: str,
        experiment_id: str,
        path: str,
        workspace_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create experiment redirect url

        Parameters
        ----------
        dataset_id : str

        experiment_id : str

        path : str

        workspace_name : typing.Optional[str]

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
        client.redirect.experiments_redirect(
            dataset_id="dataset_id",
            experiment_id="experiment_id",
            path="path",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/session/redirect/experiments",
            method="GET",
            params={
                "dataset_id": dataset_id,
                "experiment_id": experiment_id,
                "workspace_name": workspace_name,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def projects_redirect(
        self,
        *,
        trace_id: str,
        path: str,
        workspace_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create project redirect url

        Parameters
        ----------
        trace_id : str

        path : str

        workspace_name : typing.Optional[str]

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
        client.redirect.projects_redirect(
            trace_id="trace_id",
            path="path",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/session/redirect/projects",
            method="GET",
            params={
                "trace_id": trace_id,
                "workspace_name": workspace_name,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRedirectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def datasets_redirect(
        self,
        *,
        dataset_id: str,
        path: str,
        workspace_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create dataset redirect url

        Parameters
        ----------
        dataset_id : str

        path : str

        workspace_name : typing.Optional[str]

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
            await client.redirect.datasets_redirect(
                dataset_id="dataset_id",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/session/redirect/datasets",
            method="GET",
            params={
                "dataset_id": dataset_id,
                "workspace_name": workspace_name,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def experiments_redirect(
        self,
        *,
        dataset_id: str,
        experiment_id: str,
        path: str,
        workspace_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create experiment redirect url

        Parameters
        ----------
        dataset_id : str

        experiment_id : str

        path : str

        workspace_name : typing.Optional[str]

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
            await client.redirect.experiments_redirect(
                dataset_id="dataset_id",
                experiment_id="experiment_id",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/session/redirect/experiments",
            method="GET",
            params={
                "dataset_id": dataset_id,
                "experiment_id": experiment_id,
                "workspace_name": workspace_name,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def projects_redirect(
        self,
        *,
        trace_id: str,
        path: str,
        workspace_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create project redirect url

        Parameters
        ----------
        trace_id : str

        path : str

        workspace_name : typing.Optional[str]

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
            await client.redirect.projects_redirect(
                trace_id="trace_id",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/session/redirect/projects",
            method="GET",
            params={
                "trace_id": trace_id,
                "workspace_name": workspace_name,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
