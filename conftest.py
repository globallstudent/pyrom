import pytest
from app import PyRomApp


@pytest.fixture
def app():
    return PyRomApp()

@pytest.fixture
def test_client(app):
    return app.test_session()