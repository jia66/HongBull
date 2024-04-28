from abc import ABC, abstractmethod


class CrawlTask():
    # 爬取任务
    def __init__(self) -> None:
        pass


class Crawler(ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def run(self, task: CrawlTask):
        pass
 