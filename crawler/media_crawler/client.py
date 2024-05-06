import time
from xmlrpc.client import ServerProxy
import json

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
                    result = None
                    print(method.__name__)
                    print(args)
                    if method:
                        result = method(*args)
                    else:
                        print(f"RPC method {rpc_method} not found")
                    print(f"search result: {result}")
                    return result
            except Exception as e:
                print(e)
                if i == retry_times - 1:
                    raise e
                else:
                    time.sleep(retry_sleep)

    def run(self, task: CrawlTask):
        if isinstance(task, CrawlSearchTask):
            result = self.__call_rpc("search", task.keyword, task.start_page)
            with open(result, "r", encoding="utf-8") as f:
                search_result_json = json.load(f)
                print(search_result_json)
        else:
            print(f"MediaCrawler unsupported task type: {type(task)}")
