import httpx
import logging
from mcp.server.fastmcp import FastMCP

mcp_server = FastMCP()

# Configure logging for better debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@mcp_server.tool()
async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    
    #async with httpx.AsyncClient() as client:
    #    response = await client.get(f"https://wttr.in/{city}?format=%C+%t")
    #    return response.text

    # fake response so it is always bad weather!
    response = f"Weather for {city} is -10 degrees Celsius and snowing."
    logger.info(response)
    
    return response


if __name__ == '__main__':
    
    mcp_server.run(transport='streamable-http')
