from misc.pickle_io import load_pickle
from os import getcwd


class FilePath:
    slackbot = getcwd()
    webhook = slackbot + "webhooks.pkl"
    crawler = slackbot + "/crawler"
    crawler_data = {

        "grad_info": crawler + "/data/grad_home_notice.list",
        "ssu_info": crawler + "/data/ssu_home_notice.list",
        "sw_grad_info": crawler + "/data/sw_grad_notice.list",
        "sw_dept_info": crawler + "/data/sw_dept_notice.list",
        "sw_job_info": crawler + "/data/sw_job_notice.list"
    }


class Url:
    homepages = {
        "ssu": "https://scatch.ssu.ac.kr",
        "grad": "https://grad.ssu.ac.kr",
        "sw": "https://sw.ssu.ac.kr"
    }
    notices = {
        "grad": homepages["grad"] + "/%ec%a0%95%eb%b3%b4%ea%b4%91%ec%9e%a5/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/",
        "ssu": homepages["ssu"] + "/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/",
        "sw_grad": homepages["sw"] + "/bbs/board.php?bo_table=sub6_6",
        "sw_dept": homepages["sw"] + "/bbs/board.php?bo_table=sub6_1",
        "sw_job": homepages["sw"] + "/bbs/board.php?bo_table=sub6_5"
    }

    webhooks = load_pickle(FilePath.webhook)   # Secret file
    grad_announce_webhook = webhooks['grad_announce']
    ssu_announce_webhook = webhooks['ssu_announce']
    my_dm_webhook = webhooks['liberty_dm']
    sc_announce_webhook = webhooks['sc_announce']

