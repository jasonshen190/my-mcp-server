# my-mcp-server MCP Server

## Overview

my-mcp-server is a comprehensive example MCP server demonstrating tools, resources, and prompts using the FastMCP framework. It is modular, extensible, and includes structured output, error handling, and async support.

## Local Testing Instructions

If you want to test the server locally after cloning the repository or downloading and unzipping the package:

1. Open `src/demo_server.py` and go to lines 114 and 115.
1. Comment the mcp.run()
1. Uncomment or update these lines to enable the `streamable-http` mode:
   ```python
   # mcp.run(transport="streamable-http")
   # print("Starting MCP server...")
   mcp.run(transport="streamable-http")
   ```
1. run by following [Testing with the Client](#testing-with-the-client)
1. To test with IDEs like Cursor, use the contents in mcp-local.json in ~/.cursor/mcp.json(restart Cursor might be needed)

## Test with Remote(uvx)

1. Instead of run the demo_server.py locally, use mcp.json in ~/.cursor/mcp.json to use it as remote MCP server

## Project Structure

```
my-mcp-server/
├── src/
│   ├── demo_server.py         # Main MCP server with tool/resource/prompt registration
│   ├── setup_and_run.py      # Interactive setup and run script
│   ├── test_client.py        # Async test client for all features
|   |── mcp-local.json        # local test server configuration
│   ├── mcp.json              # Server configuration
│   └── components/
│       ├── tools.py          # Tool logic and models
│       ├── resources.py      # Resource logic
│       ├── prompts.py        # Prompt logic
│       └── __init__.py
├── requirements.txt
├── pyproject.toml
├── README.md
```

## Usage

### Testing the Server locally

#### Method 1: Direct execution
```bash
python src/demo_server.py
```


#### Method 2: Interactive Setup (Recommended)
```bash
python src/setup_and_run.py
```

### Testing with the Client

Run the test client to see all features in action:
```bash
python src/test_client.py
```

## Example Output

When you run the test client, you should see output like:

```
Connected to my-mcp-server MCP Server!
==================================================

1. Testing Tools:
--------------------
add_numbers_tool(5, 3) = 8
multiply_numbers_tool(4.5, 2.0) = 9.0
calculate_bmi_tool(70kg, 1.75m) = 22.857142857142858
get_weather_tool('New York') = {"temperature": 22.5, "humidity": 65.0, "condition": "partly cloudy", "wind_speed": 12.3}
format_text_tool('hello world', 'uppercase') = HELLO WORLD
get_current_time_tool('UTC') = Current time in UTC: 2024-01-15 10:30:45

2. Testing Resources:
--------------------
config://app = {
  "name": "my-mcp-server",
  "version": "1.0.0",
  "features": ["tools", "resources", "prompts"],
  "status": "active"
}...
greeting://Alice = Hello, Alice! Welcome to the my-mcp-server MCP Server.
info://server = {
  "server_name": "my-mcp-server",
  "description": "A comprehensive MCP server demonstrating various features",
  "available_tools": [...]
}...
math://constants = {
  "pi": 3.14159265359,
  "e": 2.71828182846,
  "golden_ratio": 1.61803398875,
  "sqrt_2": 1.41421356237
}...

3. Testing Prompts:
--------------------
Available prompts: ['calculator_assistant_prompt', 'weather_assistant_prompt', 'text_formatter_prompt']
calculator_assistant_prompt = You are a helpful calculator assistant. You can:
- Add numbers using the add_numbers tool
- Multiply numbers using the multiply_numbers tool
- Calculate BMI using the calculate_bmi tool
- Get mathematical constants from the math://constants resource

Please help users with their calculations!

==================================================
All tests completed successfully!
```

## Features

### Tools
- **add_numbers_tool(a, b)**: Add two numbers (int)
- **multiply_numbers_tool(a, b)**: Multiply two numbers (float)
- **calculate_bmi_tool(weight_kg, height_m)**: Calculate BMI given weight (kg) and height (m)
- **get_weather_tool(city)**: Get simulated weather data for a city (returns structured WeatherData)
- **format_text_tool(text, style)**: Format text in different styles (uppercase, lowercase, title, reverse, normal)
- **get_current_time_tool(timezone)**: Get the current time in the specified timezone (default: UTC)

### Resources
- **config://app**: Application configuration (name, version, features, status)
- **greeting://{name}**: Personalized greeting
- **info://server**: Server information and available features
- **math://constants**: Common mathematical constants (pi, e, golden_ratio, sqrt_2)

### Prompts
- **calculator_assistant_prompt**: Assistant for mathematical calculations
- **weather_assistant_prompt**: Assistant for weather-related queries
- **text_formatter_prompt**: Assistant for text formatting

## Main Files

- **src/demo_server.py**: Registers all tools, resources, and prompts with FastMCP. Entry point for running the server.
- **src/setup_and_run.py**: Installs dependencies and interactively runs the server or test client.
- **src/test_client.py**: Async client that tests all tools, resources, and prompts via HTTP.
- **src/components/tools.py**: Implements tool logic and the WeatherData model.
- **src/components/resources.py**: Implements resource logic and returns JSON-encoded data.
- **src/components/prompts.py**: Implements prompt logic for assistants.

## Advanced Usage

- **Structured Output**: `get_weather_tool` returns a Pydantic model for structured weather data.
- **Error Handling**: Tools like `calculate_bmi_tool` raise errors for invalid input (e.g., non-positive height).
- **Customization**: Add new tools/resources/prompts by editing the respective files in `src/components/`.

## Development

- Modular, decoupled design for easy extension and debugging
- Pydantic models for type safety
- Async/await support
- Comprehensive error handling

## Next Steps

- Explore the [MCP Python SDK documentation](https://modelcontextprotocol.io)
- Build your own MCP server with custom functionality
- Integrate with Claude Desktop or other MCP clients
