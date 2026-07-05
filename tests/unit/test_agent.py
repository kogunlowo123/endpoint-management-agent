"""Endpoint Management Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_check_device_health():
    """Test Check health and compliance status of an endpoint."""
    tools = AgentTools()
    result = await tools.check_device_health(device_id="test", checks="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_deploy_software():
    """Test Deploy software or update to endpoints."""
    tools = AgentTools()
    result = await tools.deploy_software(package="test", targets="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_enforce_policy():
    """Test Enforce security policy on non-compliant devices."""
    tools = AgentTools()
    result = await tools.enforce_policy(policy_id="test", target_devices="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_remote_diagnose():
    """Test Run remote diagnostic on an endpoint."""
    tools = AgentTools()
    result = await tools.remote_diagnose(device_id="test", diagnostic_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.endpoint_management_agent_agent import EndpointManagementAgentAgent
    agent = EndpointManagementAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
