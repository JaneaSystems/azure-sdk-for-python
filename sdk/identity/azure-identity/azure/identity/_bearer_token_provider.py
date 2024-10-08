# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import Callable

from azure.core.credentials import TokenProvider
from azure.core.pipeline.policies import BearerTokenCredentialPolicy
from azure.core.pipeline import PipelineRequest, PipelineContext
from azure.core.rest import HttpRequest


def _make_request() -> PipelineRequest[HttpRequest]:
    return PipelineRequest(HttpRequest("CredentialWrapper", "https://fakeurl"), PipelineContext(None))


def get_bearer_token_provider(credential: TokenProvider, *scopes: str) -> Callable[[], str]:
    """Returns a callable that provides a bearer token.

    It can be used for instance to write code like:

    .. code-block:: python

        from azure.identity import DefaultAzureCredential, get_bearer_token_provider

        credential = DefaultAzureCredential()
        bearer_token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")

        # Usage
        request.headers["Authorization"] = "Bearer " + bearer_token_provider()

    :param credential: The credential used to authenticate the request.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str scopes: The scopes required for the bearer token.
    :rtype: callable
    :return: A callable that returns a bearer token.
    """

    policy = BearerTokenCredentialPolicy(credential, *scopes)

    def wrapper() -> str:
        request = _make_request()
        policy.on_request(request)
        return request.http_request.headers["Authorization"][len("Bearer ") :]

    return wrapper
