"""
Resources module for my-mcp-server MCP Server
Contains all resource functions
"""

import json


def get_app_config() -> str:
    """Get application configuration"""
    config = {
        "name": "my-mcp-server",
        "version": "1.0.0",
        "features": ["tools", "resources", "prompts"],
        "status": "active"
    }
    return json.dumps(config, indent=2)


def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Welcome to the my-mcp-server MCP Server."


def get_server_info() -> str:
    """Get server information"""
    info = {
        "server_name": "my-mcp-server",
        "description": "A comprehensive MCP server demonstrating various features",
        "available_tools": [
            "add_numbers",
            "multiply_numbers", 
            "calculate_bmi",
            "get_weather",
            "format_text",
            "get_current_time"
        ],
        "available_resources": [
            "config://app",
            "greeting://{name}",
            "info://server",
            "math://constants"
        ]
    }
    return json.dumps(info, indent=2)


def get_math_constants() -> str:
    """Get common mathematical constants"""
    constants = {
        "pi": 3.14159265359,
        "e": 2.71828182846,
        "golden_ratio": 1.61803398875,
        "sqrt_2": 1.41421356237
    }
    return json.dumps(constants, indent=2)