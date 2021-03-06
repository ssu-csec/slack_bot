if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname( path.dirname( path.abspath(__file__) ) ))
        sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
        from crawler.noticebot import NoticeBot
        from crawler.crawler import Crawler
        from crawler.const import Url, FilePath
    else:
        from .crawler.noticebot import NoticeBot
        from .crawler.crawler import Crawler
        from .crawler.const import Url, FilePath

    bot_list = [NoticeBot(Crawler.crawl_grad_notice, Url.my_dm_webhook, FilePath.grad_info_path),
                NoticeBot(Crawler.crawl_ssu_notice, Url.my_dm_webhook, FilePath.ssu_info_path, seek_time=7200),
                NoticeBot(Crawler.crawl_sw_grad_notice, Url.my_dm_webhook, FilePath.sw_grad_info_path),
                NoticeBot(Crawler.crawl_sw_dept_notice, Url.my_dm_webhook, FilePath.sw_dept_info_path),
                NoticeBot(Crawler.crawl_sw_job_notice, Url.my_dm_webhook, FilePath.sw_job_info_path)
                ]

    for bot in bot_list:
        bot.daemon = True
        bot.start()

    for bot in bot_list:
        bot.join()

