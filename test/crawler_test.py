from crawler import *

def run():
    crawler = MediaCrawler()
    task = CrawlSearchTask(keyword="动物手链,云养宠物")
    crawler.run(task=task)
