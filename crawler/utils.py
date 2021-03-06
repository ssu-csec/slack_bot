import requests
from bs4 import BeautifulSoup


def get_html_attributes(url, tag):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select(tag)


def merge_to_anchor(title, link):
    anchor = "<" + link + " | " + title + ">"
    return anchor


def get_link(notice_list):
    link_list = list()

    for notice in notice_list:
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
