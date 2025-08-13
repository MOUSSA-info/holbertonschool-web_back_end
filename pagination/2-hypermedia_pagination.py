#!/usr/bin/env python3
"""
Hypermedia pagination module
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end indexes for a given page and page size.

    Args:
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        Tuple[int, int]: start_index and end_index for list slicing
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset (skips the header row).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): Page number (1-indexed)
            page_size (int): Number of items per page

        Returns:
            List[List]: Dataset rows for the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return pagination info with dataset.

        Args:
            page (int): Page number (1-indexed)
            page_size (int): Number of items per page

        Returns:
            Dict: {
                'page_size': int,
                'page': int,
                'data': List[List],
                'next_page': int or None,
                'prev_page': int or None,
                'total_pages': int
            }
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            'page_size': len(data),  # might be 0 for out of range
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
