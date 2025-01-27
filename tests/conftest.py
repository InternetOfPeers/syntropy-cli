import os
from unittest import mock

import pytest
import syntropy_sdk as sdk
from click.testing import CliRunner
from syntropy_sdk.rest import ApiException

from syntropycli import __main__ as ctl


@pytest.fixture
def login_mock():
    with mock.patch(
        "syntropy_sdk.utils.login_with_access_token",
        autospec=True,
        returns="JWT access token",
    ) as the_mock:
        yield the_mock


@pytest.fixture
def env_mock():
    with mock.patch.dict(
        os.environ, {"SYNTROPY_API_SERVER": "server", "SYNTROPY_API_TOKEN": "token"}
    ) as the_mock:
        yield the_mock


@pytest.fixture
def runner(env_mock):
    return CliRunner()


@pytest.fixture
def print_table_mock():
    with mock.patch(
        "syntropycli.__main__.print_table",
        autospec=True,
    ) as the_mock:
        yield the_mock


@pytest.fixture
def mock_index_api_key():
    with mock.patch.object(
        ctl.sdk.APIKeysApi,
        "get_api_key",
        autospec=True,
        return_value=ctl.sdk.models.ApiResponseApiKeyDtoArray_(
            [
                ctl.sdk.models.ApiKeyDto(
                    **{
                        "api_key_name": "skip",
                        "api_key_id": 123,
                        "api_key_created_at": "date",
                        "api_key_updated_at": "date",
                        "api_key_status": "status",
                    }
                ),
                ctl.sdk.models.ApiKeyDto(
                    **{
                        "api_key_name": "test",
                        "api_key_id": 321,
                        "api_key_created_at": "date",
                        "api_key_updated_at": "date",
                        "api_key_status": "status",
                    }
                ),
            ]
        ),
    ) as index_mock:
        yield index_mock


@pytest.fixture
def mock_delete_api_key():
    with mock.patch.object(
        ctl.sdk.APIKeysApi, "delete_api_key", autospec=True
    ) as the_mock:
        yield the_mock


@pytest.fixture
def with_pagination():
    with mock.patch.object(
        ctl.sdk.utils,
        "WithPagination",
        autospec=True,
        side_effect=lambda x: x,
    ) as the_mock:
        yield the_mock


@pytest.fixture
def mock_create_api_key():
    with mock.patch.object(
        ctl.sdk.APIKeysApi,
        "create_api_key",
        autospec=True,
        return_value=ctl.sdk.models.ApiResponseApiKeyObject_(
            ctl.sdk.models.ApiKeyObject(
                **{
                    "api_key_name": "skip",
                    "api_key_id": 123,
                    "user_id": 1,
                    "api_key_secret": "secret",
                    "api_key_created_at": "date",
                    "api_key_updated_at": "date",
                }
            )
        ),
    ) as the_mock:
        yield the_mock
