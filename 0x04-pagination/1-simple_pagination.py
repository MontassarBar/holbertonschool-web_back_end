#!/usr/bin/env python3
'''class server'''
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get page data'''
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        list = []
        x = self.index_range(page, page_size)
        self.dataset()
        if x[1] <= len(self.__dataset):
            for i in range(x[0], x[1]):
                list.append(self.__dataset[i])
        return list

    def index_range(self, page: int, page_size: int) -> Tuple:
        '''index range'''
        return (page - 1) * page_size, page_size * page
