#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return hypermedia pagination information for the given index.
        """
        assert isinstance(index, int), "Index must be an integer"
        assert 0 <= index < len(self.indexed_dataset()), \
            "Index must be in a valid range"
        assert isinstance(page_size, int), "Page size must be an integer"
        assert page_size > 0, "Page size must be a positive integer"

        next_index = index + page_size
        data = [
            self.indexed_dataset().get(i, [])
            for i in range(index, next_index)
            ]

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index':
            next_index if next_index < len(self.indexed_dataset())
            else None,
        }
