import pickle
from threading import Timer
import requests
from bs4 import BeautifulSoup
from post import post_to_slack

grad_home_url = "https://grad.ssu.ac.kr/%ec%a0%95%eb%b3%b4%ea%b4%91%ec%9e%a5/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/"
sw_home_url = "https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_6"
sw_url = "https://sw.ssu.ac.kr"
crawler_home_path = "/home/20170335/crawler"
grad_info_path = crawler_home_path + "/grad_home_notice.list"
sw_info_path = crawler_home_path + "/sw_home_notice.list"
seek_time = 43200


def get_grad_notice_list():
    response = requests.get(grad_home_url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('tr')
    first = True
    notice_list = list()

    for link in links:
        if first:
            first = False
            continue

        # 링크 가져오기
        title_link = link.find('a')['href']

        # 타이틀 가져오기
        link_split = link.text.strip().split("\n\n")
        title = link_split[1] + " / " + link_split[2].split("\n")[0]

        notice = [title, title_link]
        notice_list.append(notice)

    # 오래된 날짜순으로 정렬
    notice_list.reverse()

    return notice_list


def get_sw_notice_list():
    response = requests.get(sw_home_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('tr')
    first = True
    notice_list = list()

    for link in links:

        if first:
            first = False
            continue

        # 링크 가져오기
        title_link = sw_url + link.find('a')['href'].replace("..", "")

        # 타이틀 가져오기
        classify = str(link.find('td'))

        if "공지" not in classify:
            continue

        link_split = link.text.strip().split("\n")
        title = link_split[2] + " / " + link_split[4]

        notice = [title, title_link]
        notice_list.append(notice)

    # 오래된 날짜순으로 정렬
    notice_list.reverse()

    return notice_list


def get_link(origin_list):
    link_list = list()

    for notice in origin_list:
        link_list.append(notice[1])

    return link_list


def find_new_notice(past_list, current_list):
    new_notice_list = list()
    past_links = get_link(past_list)
    current_links = get_link(current_list)

    index = 0
    for current_link in current_links:

        if current_link not in past_links:
            new_notice_list.append(current_list[index])

        index += 1

    return new_notice_list


def send_slack(notice):
    title = notice[0]
    link = notice[1]
    message = "<" + link + " | " + title + ">"
    print(message)
    return
    post_to_slack(message)


def load_list(save_path):
    try:
        f = open(save_path, "rb")
    except FileNotFoundError:
        return None

    loading_list = pickle.load(f)
    f.close()
    return loading_list


def save_list(saving_list, save_path):
    f = open(save_path, "wb")
    pickle.dump(saving_list, f)
    f.close()


def notice_bot():
    grad_past_notice = load_list(grad_info_path)
    sw_past_notice = load_list(sw_info_path)

    while True:
        grad_current_notice = get_grad_notice_list()
        sw_current_notice = get_sw_notice_list()

        if grad_past_notice is None:
            grad_past_notice = grad_current_notice

            for grad_notice in grad_current_notice:
                send_slack(grad_notice)

            save_list(grad_current_notice, grad_info_path)

        else:
            grad_new_notices = find_new_notice(grad_past_notice, grad_current_notice)

            if grad_new_notices is not []:

                for grad_notice in grad_new_notices:
                    send_slack(grad_notice)

                save_list(grad_current_notice, grad_info_path)

        if sw_past_notice is None:
            sw_past_notice = sw_current_notice

            for sw_notice in sw_current_notice:
                send_slack(sw_notice)

            save_list(sw_current_notice, sw_info_path)

        else:
            sw_new_notices = find_new_notice(sw_past_notice, sw_current_notice)

            if sw_new_notices is not []:

                for sw_notice in sw_new_notices:
                    send_slack(sw_notice)

                save_list(sw_current_notice, sw_info_path)


if __name__=="__main__":
    Timer(seek_time, notice_bot).start()
