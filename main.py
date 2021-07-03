if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname( path.dirname( path.abspath(__file__) ) ))
        sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
        from bot.noticebot import NoticeBot
        from crawler.crawler import Crawler
        from const import Url, FilePath
    else:
        from bot.noticebot import NoticeBot
        from .crawler.crawler import Crawler
        from const import Url, FilePath

    path = FilePath
    bot_list = [NoticeBot(Crawler.crawl_grad_notice, Url.my_dm_webhook, path.crawler_data["grad_info"]),
                NoticeBot(Crawler.crawl_ssu_notice, Url.my_dm_webhook, path.crawler_data["ssu_info"], seek_time=7200),
                NoticeBot(Crawler.crawl_sw_grad_notice, Url.my_dm_webhook, path.crawler_data["sw_grad_info"]),
                NoticeBot(Crawler.crawl_sw_dept_notice, Url.my_dm_webhook, path.crawler_data["sw_dept_info"]),
                NoticeBot(Crawler.crawl_sw_job_notice, Url.my_dm_webhook, path.crawler_data["sw_job_info"])
                ]

    for bot in bot_list:
        bot.daemon = True
        bot.start()

    for bot in bot_list:
        bot.join()

