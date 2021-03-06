from .utils import get_html_attributes
from .const import Url


class Crawler:

    @staticmethod
    def crawl_grad_notice():
        attrs = get_html_attributes(Url.grad_home, 'tr')
        notice_list = list()

        for attr in attrs[1:]:
            # 링크 가져오기
            title_link = attr.find('a')['href']

            # 타이틀 가져오기
            link_split = attr.text.strip().split("\n\n")
            title = link_split[1] + " / " + link_split[2].split("\n")[0]

            notice = [title, title_link]
            notice_list.append(notice)

        # 오래된 날짜순으로 정렬
        notice_list.reverse()

        return notice_list

    @staticmethod
    def crawl_ssu_notice():
        attrs = get_html_attributes(Url.ssu_home, 'div.notice_col3')
        notice_list = list()

        for attr in attrs[1:]:
            # 링크 가져오기
            title_link = attr.find('a')['href'].replace("..", "")

            # 타이틀 가져오기
            link_split = attr.text.strip().split("\n")
            title = link_split[1]

            notice = [title, title_link]
            notice_list.append(notice)

        # 오래된 날짜순으로 정렬
        notice_list.reverse()

        return notice_list

    @staticmethod
    def crawl_sw_notice(url, announce_only=True):
        attrs = get_html_attributes(url, 'tr')
        notice_list = list()

        for attr in attrs[1:]:
            # 링크 가져오기
            title_link = Url.sw_homepage + attr.find('a')['href'].replace("..", "")

            # 타이틀 가져오기
            classify = str(attr.find('td'))

            if "공지" not in classify and announce_only is True:
                continue

            link_split = attr.text.strip().split("\n")
            title = link_split[2] + " / " + link_split[4]

            notice = [title, title_link]
            notice_list.append(notice)

        # 오래된 날짜순으로 정렬
        notice_list.reverse()

        return notice_list

    @classmethod
    def crawl_sw_grad_notice(cls):
        return cls.crawl_sw_notice(Url.sw_grad)

    @classmethod
    def crawl_sw_dept_notice(cls):
        return cls.crawl_sw_notice(Url.sw_dept)

    @classmethod
    def crawl_sw_job_notice(cls):
        return cls.crawl_sw_notice(Url.sw_job, announce_only=False)
