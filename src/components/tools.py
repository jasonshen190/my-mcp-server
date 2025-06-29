"""
Tools module for my-mcp-server MCP Server
Contains all tool functions and related models
"""

from pydantic import BaseModel, Field
import datetime


class WeatherData(BaseModel):
    temperature: float = Field(description="Temperature in Celsius")
    humidity: float = Field(description="Humidity percentage")
    condition: str = Field(description="Weather condition")
    wind_speed: float = Field(description="Wind speed in km/h")


def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return a * b


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m ** 2)


def get_weather(city: str) -> WeatherData:
    """Get weather information for a city (simulated)"""
    # This is a simulated weather API
    weather_data = {
        "New York": WeatherData(temperature=22.5, humidity=65.0, condition="partly cloudy", wind_speed=12.3),
        "London": WeatherData(temperature=15.2, humidity=78.0, condition="rainy", wind_speed=8.7),
        "Tokyo": WeatherData(temperature=28.1, humidity=72.0, condition="sunny", wind_speed=5.2),
        "Sydney": WeatherData(temperature=25.8, humidity=68.0, condition="clear", wind_speed=15.1)
    }
    
    if city in weather_data:
        return weather_data[city]
    else:
        # Return default data for unknown cities
        return WeatherData(temperature=20.0, humidity=60.0, condition="unknown", wind_speed=10.0)


def format_text(text: str, style: str = "normal") -> str:
    """Format text in different styles"""
    styles = {
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "title": text.title(),
        "reverse": text[::-1],
        "normal": text
    }
    return styles.get(style, text)


def get_current_time(timezone: str = "UTC") -> str:
    """Get the current time in the specified timezone"""
    now = datetime.datetime.now()
    return f"Current time in {timezone}: {now.strftime('%Y-%m-%d %H:%M:%S')}"