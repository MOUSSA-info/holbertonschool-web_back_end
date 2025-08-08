#!/usr/bin/env python3
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random delay between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times concurrently and return sorted delays"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
