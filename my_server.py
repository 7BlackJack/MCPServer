from fastmcp import FastMCP, Client
import asyncio

mcp = FastMCP("My MCP Server")

@mcp.tool()
def great(name: str) -> str:
    return f"Hello, {name}!"

client = Client(mcp)

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

# asyncio.run(call_tool("Ford"))

if __name__ == "__main__":
    mcp.run()