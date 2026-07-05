"""Test configuration for Endpoint Management Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "endpoint-management-agent", "category": "IT Operations"}
