import pytest
import run

@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()

