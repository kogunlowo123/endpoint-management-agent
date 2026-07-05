"""Endpoint Management Agent - MCP Server."""

import structlog

logger = structlog.get_logger(__name__)


class MCPServer:
    """MCP server for Endpoint Management Agent."""

    def __init__(self):
        logger.info("mcp_server_initialized")
