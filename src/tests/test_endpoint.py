import pytest
from fastapi.testclient import TestClient

from fastapi_server import app
from fastapi_server import root


def test_root_endpoint(app_state, mocker):
    mocker.patch("fastapi_server.app_state", app_state)

    client = TestClient(app=app)
    response = client.get("/",)
    assert response.status_code == 200
    assert response.json() == {"message": "No message found"}


@pytest.mark.asyncio
async def test_root(app_state, mocker):
    mocker.patch("fastapi_server.app_state", app_state)

    result = await root()
    assert result.message == "No message found"