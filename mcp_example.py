"""
Example of using MCPServerStdio with pydantic-ai
"""

import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider
import boto3
from botocore.config import Config as BotocoreConfig

async def main():
    # Set up Bedrock client
    bedrock_config = BotocoreConfig(
        read_timeout=300,
        connect_timeout=60,
        retries={"max_attempts": 3},
    )
    bedrock_client = boto3.client(
        "bedrock-runtime", region_name="us-east-1", config=bedrock_config
    )
    
    model = BedrockConverseModel(
        "anthropic.claude-3-5-sonnet-20240620-v1:0",
        provider=BedrockProvider(bedrock_client=bedrock_client),
    )
    
    # Connect to an MCP server (example: file system server)
    async with MCPServerStdio(
        command="npx",
        args=["@modelcontextprotocol/server-filesystem", "/path/to/directory"],
    ) as mcp_server:
        
        # Create agent with MCP server tools
        agent = Agent(
            model=model,
            deps_type=type(None),
        )
        
        # Add MCP server tools to the agent
        agent.add_mcp_server(mcp_server)
        
        # Now the agent can use file system tools
        result = await agent.run("List the files in the directory")
        print(result.data)

if __name__ == "__main__":
    asyncio.run(main())


