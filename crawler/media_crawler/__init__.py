import os
import subprocess

import client

from crawler.core import CrawlTask

from ..core import Crawler


class MediaCrawler(Crawler):

    def __init__(self):
        super().__init__(name="MediaCrawler")

        self.server_script = os.path.join(
            os.path.dirname(__file__), "server.py")
        command = ["conda", "run", "-n", "media_crawler",
                   "python", self.server_script]
        self.server_process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def __del__(self):
        # 对象销毁时回收资源
        self.server_process.terminate()
        self.server_process.wait()

    def run(self, task: CrawlTask):
        pass
