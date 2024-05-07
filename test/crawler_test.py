from crawler import *

def run():
    crawler = MediaCrawler()
    task = CrawlSearchTask(keyword="云养宠物")
    crawler.run(task=task)
