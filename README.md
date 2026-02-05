# CodingAgent

A Pydantic AI–powered coding agent that uses **AWS Bedrock** (Claude 3.5 Sonnet) and multiple **MCP (Model Context Protocol)** servers to help maintain and develop codebases. The agent can run tests, search the web, reason about code, use AWS tools and docs, and run Python code.

## Features

- **AWS Bedrock** – Uses Claude 3.5 Sonnet via the Bedrock Converse API
- **MCP integrations** – Several MCP servers for different capabilities:
  - **AWS Labs** – Core AWS operations
  - **AWS Documentation** – AWS docs lookup
  - **Run Python** – Execute Python code (via Deno/MCP)
  - **Context7** – Upstash Context7
  - **DuckDuckGo** – Internet search
  - **Code Reasoning** – Code analysis and reasoning
  - **Desktop Commander** – Desktop automation
- **Custom tools** – `run_unit_tests` to run the project’s test suite with `uv run pytest`
- **CLI** – Interactive chat via `agent.to_cli()`

## Prerequisites

- **Python 3.13+**
- [uv](https://docs.astral.sh/uv/) – Package and project management
- **AWS** – Account and credentials with access to Bedrock in `us-east-1`
- **Node.js** (and `npx`) – For MCP servers that use `npx`
- **Deno** – For the run-python MCP server (`jsr:@pydantic/mcp-run-python`)

## Installation

1. Clone the repo and go to the project directory:

   ```bash
   cd CodingAgent
   ```

2. Install dependencies with uv (creates a venv and installs from `pyproject.toml`):

   ```bash
   uv sync
   ```

3. Ensure AWS is configured (credentials and region for Bedrock):

   ```bash
   aws configure
   # or set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION
   ```

4. Install Node/Deno dependencies as required by the MCP servers (e.g. `node_modules` for run-python). The run-python server expects a `node_modules` directory; install any Node deps your MCP setup needs.

## Configuration

- **Model** – Set in `main.py`: `BedrockConverseModel("anthropic.claude-3-5-sonnet-20240620-v1:0", ...)`. Change the model id to use another Bedrock model.
- **Agent instructions** – Edit the `instructions` string in `main.py` (replace the `XXXXXX` placeholder with your actual project/codebase name and any extra guidelines).
- **MCP servers** – Enable/disable or add servers via the `mcp_servers` list passed to `Agent(...)`.

## Usage

Run the agent CLI:

```bash
uv run python main.py
```

Then interact in the terminal. The agent can:

- Run unit tests (`run_unit_tests` tool)
- Search the web, reason about code, run Python snippets
- Use AWS tools and documentation
- Follow the development guidelines defined in its instructions

## Development

- **Tests** – Unit tests live under `tests/`. Run them with:

  ```bash
  uv run pytest -xvs tests/
  ```

  The agent uses the same command via the `run_unit_tests` tool.

- **Dependencies** – Managed in `pyproject.toml`. Add new deps with:

  ```bash
  uv add <package>
  ```

  Dev/test deps are in the `[dependency-groups] dev` section.

## Project structure

```
CodingAgent/
├── main.py           # Agent definition, MCP servers, Bedrock config, CLI entrypoint
├── pyproject.toml    # Project metadata and dependencies (uv)
├── uv.lock           # Locked dependencies
├── calculator.py     # Example module (optional)
├── tests/            # Pytest test suite
└── README.md         # This file
```

## License

See the repository for license information.
