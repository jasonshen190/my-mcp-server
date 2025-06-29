"""
Test Client for my-mcp-server MCP Server
Demonstrates how to connect to and use the MCP server
"""

import asyncio
from mcp import ClientSession
from mcp.client.session_group import StreamableHttpParameters
from mcp.client.streamable_http import streamablehttp_client


async def test_server():
    """Test the my-mcp-server MCP server"""
    
    # Create server parameters for HTTP connection
    server_params = StreamableHttpParameters(url="http://127.0.0.1:8000/mcp")
    
    # Connect to the server via streamable-http
    async with streamablehttp_client(server_params.url) as (read, write, _):
        async with ClientSession(read, write) as session:
            
            # Initialize the connection
            await session.initialize()
            
            print("Connected to my-mcp-server MCP Server!")
            print("=" * 50)
            
            # Test tools
            print("\n1. Testing Tools:")
            print("-" * 20)
            
            # Test add_numbers tool
            result = await session.call_tool("add_numbers_tool", {"a": 5, "b": 3})
            print(f"add_numbers_tool(5, 3) = {result.content[0].text}")
            
            # Test multiply_numbers tool
            result = await session.call_tool("multiply_numbers_tool", {"a": 4.5, "b": 2.0})
            print(f"multiply_numbers_tool(4.5, 2.0) = {result.content[0].text}")
            
            # Test calculate_bmi tool
            result = await session.call_tool("calculate_bmi_tool", {"weight_kg": 70.0, "height_m": 1.75})
            print(f"calculate_bmi_tool(70kg, 1.75m) = {result.content[0].text}")
            
            # Test get_weather tool
            result = await session.call_tool("get_weather_tool", {"city": "New York"})
            print(f"get_weather_tool('New York') = {result.content[0].text}")
            
            # Test format_text tool
            result = await session.call_tool("format_text_tool", {"text": "hello world", "style": "uppercase"})
            print(f"format_text_tool('hello world', 'uppercase') = {result.content[0].text}")
            
            # Test get_current_time tool
            result = await session.call_tool("get_current_time_tool", {"timezone": "UTC"})
            print(f"get_current_time_tool('UTC') = {result.content[0].text}")
            
            # Test resources
            print("\n2. Testing Resources:")
            print("-" * 20)
            
            # Test config resource
            result = await session.read_resource("config://app")
            print(f"config://app = {result.contents[0].text[:100]}...")
            
            # Test greeting resource
            result = await session.read_resource("greeting://Alice")
            print(f"greeting://Alice = {result.contents[0].text}")
            
            # Test server info resource
            result = await session.read_resource("info://server")
            print(f"info://server = {result.contents[0].text[:100]}...")
            
            # Test math constants resource
            result = await session.read_resource("math://constants")
            print(f"math://constants = {result.contents[0].text[:100]}...")
            
            # Test prompts
            print("\n3. Testing Prompts:")
            print("-" * 20)
            
            # List available prompts
            prompts = await session.list_prompts()
            print(f"Available prompts: {[p.name for p in prompts.prompts]}")
            
            # Get a specific prompt
            result = await session.get_prompt("calculator_assistant_prompt")
            print(f"calculator_assistant_prompt = {result.description}")
            
            print("\n" + "=" * 50)
            print("All tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_server())
