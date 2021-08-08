# -*- coding: utf-8 -*-
'''
@File     : video.py
@Author   : fuzizhu
@Software : PyCharm
@Project  : pinduoduo
@Date     : 2021/2/1 21:40
@Desc     : 
'''
# -*- coding: utf-8 -*-
'''
@File     : pinduoduo.py
@Author   : fuzizhu
@Software : PyCharm
@Project  : pinduoduo
@Date     : 2021/1/29 17:07
@Desc     :
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import csv


#


def get_video_url(url, goods_id):
    options = Options()
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    # options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
    browser = webdriver.Chrome(
        executable_path="chromedriver.exe", options=options)
    browser.get(url)
    time.sleep(1)
    video = browser.find_element_by_tag_name("video").get_attribute('src')
    print(video)

    filename = "datas/" + goods_id + "/goods.csv"
    df = pd.read_csv(filename, encoding='utf-8')
    data = [video, ]
    df['视频u3m8下载地址'] = data
    df.to_csv(filename, index=None)


if __name__ == "__main__":
    # url = 'http://yangkeduo.com/goods.html?goods_id=215337688112&_oak_gallery=http%3A%2F%2Ft00img.yangkeduo.com%2Fgoods%2Fimages%2F2021-01-16%2F64b4c72791b9962c5ce59a5cac8dab4a.jpeg&_oak_rem_ar_id=999&page_from=35&refer_page_name=index&refer_page_id=10002_1611912254262_3brz7wsvsi&refer_page_sn=10002'
    # url = 'http://yangkeduo.com/goods.html?goods_id=216024081700&_oak_rem_ar_id=999&_oak_gallery=http%3A%2F%2Ft00img.yangkeduo.com%2Fgoods%2Fimages%2F2021-01-16%2Ff79e5ede04cbe666936822d743229791.jpeg&page_from=35&refer_page_name=psnl_varification&refer_page_id=10390_1612161675742_h9i2ba9swq&refer_page_sn=10390'
    # url = "http://yangkeduo.com/ddplteec.html?mall_id=269590020&page_from=1&skip_ddjb=false&_live_goods_id=83440081887&refer_page_name=goods_detail&refer_page_id=10014_1612171319914_cy4e698zwo&refer_page_sn=10014&_x_share_id=a916d3488d114041bc707613c7b0334c"
    url ='https://yangkeduo.com/ddplteec.html?mall_id=885004032&page_from=1&skip_ddjb=false&_live_goods_id=175273997100&refer_page_name=goods_detail&refer_page_id=10014_1612247708575_h7z7nwh5uv&refer_page_sn=10014&_x_share_id=8b2f5843c4b54a0eab1c0d8c14f1be03'
    # goods_id = '215337688112'
    goods_id = '175273997100'

    get_video_url(url, goods_id)
