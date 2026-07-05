# Endpoint Management Agent

[![CI](https://github.com/kogunlowo123/endpoint-management-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/endpoint-management-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: IT Operations | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Endpoint management agent that monitors device health, enforces security policies, deploys software updates, manages device compliance, and provides remote troubleshooting for enterprise endpoints.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `check_device_health` | Check health and compliance status of an endpoint |
| `deploy_software` | Deploy software or update to endpoints |
| `enforce_policy` | Enforce security policy on non-compliant devices |
| `remote_diagnose` | Run remote diagnostic on an endpoint |
| `generate_compliance_report` | Generate endpoint compliance report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/endpoints/{device_id}/health` | Check device health |
| `POST` | `/api/v1/endpoints/deploy` | Deploy software |
| `POST` | `/api/v1/endpoints/enforce-policy` | Enforce policy |
| `POST` | `/api/v1/endpoints/{device_id}/diagnose` | Remote diagnose |
| `POST` | `/api/v1/endpoints/compliance-report` | Compliance report |

## Features

- Device Monitoring
- Policy Enforcement
- Software Deployment
- Compliance Management
- Remote Troubleshooting

## Integrations

- Microsoft Intune
- Jamf
- Sccm
- Crowdstrike
- Tanium

## Architecture

```
endpoint-management-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── endpoint_management_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Microsoft Intune + SCCM + Jamf + CrowdStrike**

---

Built as part of the Enterprise AI Agent Platform.
