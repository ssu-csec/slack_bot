from misc.pickle_io import load_list


class FilePath:
    slack_bot_path = "/home/20170335/slack_bot"
    crawler_home_path = slack_bot_path + "/crawler"
    webhook_path = crawler_home_path + "/data/webhooks.pkl"
    grad_info_path = crawler_home_path + "/data/grad_home_notice.list"
    ssu_info_path = crawler_home_path + "/data/ssu_home_notice.list"
    sw_grad_info_path = crawler_home_path + "/data/sw_grad_notice.list"
    sw_dept_info_path = crawler_home_path + "/data/sw_dept_notice.list"
    sw_job_info_path = crawler_home_path + "/data/sw_job_notice.list"


class Url:
    grad_home = "https://grad.ssu.ac.kr/%ec%a0%95%eb%b3%b4%ea%b4%91%ec%9e%a5/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/"
    ssu_home = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/"
    sw_grad = "https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_6"
    sw_dept = "https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_1"
    sw_job = "https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_5"
    sw_homepage = "https://sw.ssu.ac.kr"
    webhooks = load_list(FilePath.webhook_path)
    grad_announce_webhook = webhooks['grad_announce']
    my_dm_webhook = webhooks['liberty_dm']

