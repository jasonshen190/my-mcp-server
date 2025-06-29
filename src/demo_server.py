"""
my-mcp-server MCP Server
A comprehensive example showing tools, resources, and prompts
"""

from mcp.server.fastmcp import FastMCP
from components.tools import (
    add_numbers, multiply_numbers, calculate_bmi, 
    get_weather, format_text, get_current_time, WeatherData
)
from components.resources import (
    get_app_config, get_greeting, get_server_info, get_math_constants
)
from components.prompts import (
    calculator_assistant, weather_assistant, text_formatter
)

# Create the MCP server
mcp = FastMCP("my-mcp-server")


# ============================================================================
# TOOLS
# ============================================================================

@mcp.tool()
def add_numbers_tool(a: int, b: int) -> int:
    """Add two numbers together"""
    return add_numbers(a, b)


@mcp.tool()
def multiply_numbers_tool(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return multiply_numbers(a, b)


@mcp.tool()
def calculate_bmi_tool(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return calculate_bmi(weight_kg, height_m)


@mcp.tool()
def get_weather_tool(city: str) -> WeatherData:
    """Get weather information for a city (simulated)"""
    return get_weather(city)


@mcp.tool()
def format_text_tool(text: str, style: str = "normal") -> str:
    """Format text in different styles"""
    return format_text(text, style)


@mcp.tool()
def get_current_time_tool(timezone: str = "UTC") -> str:
    """Get the current time in the specified timezone"""
    return get_current_time(timezone)


# ============================================================================
# RESOURCES
# ============================================================================

@mcp.resource("config://app")
def get_app_config_resource() -> str:
    """Get application configuration"""
    return get_app_config()


@mcp.resource("greeting://{name}")
def get_greeting_resource(name: str) -> str:
    """Get a personalized greeting"""
    return get_greeting(name)


@mcp.resource("info://server")
def get_server_info_resource() -> str:
    """Get server information"""
    return get_server_info()


@mcp.resource("math://constants")
def get_math_constants_resource() -> str:
    """Get common mathematical constants"""
    return get_math_constants()


# ============================================================================
# PROMPTS
# ============================================================================

@mcp.prompt()
def calculator_assistant_prompt() -> str:
    """A helpful calculator assistant prompt"""
    return calculator_assistant()


@mcp.prompt()
def weather_assistant_prompt() -> str:
    """A weather information assistant prompt"""
    return weather_assistant()


@mcp.prompt()
def text_formatter_prompt() -> str:
    """A text formatting assistant prompt"""
    return text_formatter()


if __name__ == "__main__":
    # Run the server on HTTP at 127.0.0.1:8000
    mcp.run(transport="streamable-http")