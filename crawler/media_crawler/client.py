import time
from xmlrpc.client import ServerProxy

from ..core import Crawler, CrawlSearchTask, CrawlTask


class MediaCrawler(Crawler):

    __server_url = "http://localhost:8000/"

    def __init__(self):
        super().__init__(name="MediaCrawler")

    def __call_rpc(self, rpc_method: str, *args, retry_times: int = 1, retry_sleep: int = 2):
        for i in range(retry_times):
            try:
                with ServerProxy(self.__server_url) as proxy:
                    method = getattr(proxy, rpc_method)
                    print(method.__name__)
                    print(args)
                    if method:
                        method(*args)
                    else:
                        print(f"RPC method {rpc_method} not found")
                    return
            except Exception as e:
                print(e)
                if i == retry_times - 1:
                    raise e
                else:
                    time.sleep(retry_sleep)

    def run(self, task: CrawlTask):
        if isinstance(task, CrawlSearchTask):
            self.__call_rpc("search", task.keyword, task.start_page)
        else:
            print(f"MediaCrawler unsupported task type: {type(task)}")
