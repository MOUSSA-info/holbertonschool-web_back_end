#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with deletion-resilient pagination.
        """
        dataset_indexed = self.indexed_dataset()

        assert isinstance(index, int) and index >= 0
        assert index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        data = []
        current_index = index

        # Collect `page_size` items skipping deleted indexes
        while len(data) < page_size and current_index < len(self.dataset()) + page_size:
            if current_index in dataset_indexed:
                data.append(dataset_indexed[current_index])
            current_index += 1

        next_index = current_index  # This is where the next page should start

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }