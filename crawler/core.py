from abc import ABC, abstractmethod


class CrawlTask(ABC):
    # 爬取任务
    def __init__(self) -> None:
        pass

class CrawlSearchTask(CrawlTask):
    # 爬取搜索任务
    def __init__(self, keyword: str, start_page: int = 1) -> None:
        self.keyword = keyword
        self.start_page = start_page


class Crawler(ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def run(self, task: CrawlTask):
        pass
 