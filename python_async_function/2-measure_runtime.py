#!/usr/bin/env python3
import time
from 1-concurrent_coroutines import wait_n  # Adjust this import if your wait_n is elsewhere

def measure_time(n: int, max_delay: int) -> float:
    """Measure the average runtime per wait_n execution."""
    start = time.time()
    # Actually run wait_n (it's async, so you should run it with asyncio)
    import asyncio
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
