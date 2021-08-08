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
import re
import urllib.request
import os
import csv


def get_goods_id(url):
    goods_id = re.match('.*goods_id=(\d*)&.*', url).group(1)
    return goods_id


def crawl(url, goods_id):
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome(
        executable_path="chromedriver.exe", options=options)
    browser.get(url)
    time.sleep(1)
    try:
        title = browser.find_element_by_xpath('//*[@id="g-base"]/div[3]/span/span/span[1]/span').text
    except:
        browser.find_element_by_xpath('//div[@class="_3Sv259qt"]').click()
        time.sleep(1)
        title = browser.find_element_by_xpath('//*[@id="g-base"]/div[3]/span/span/span[1]/span').text
    browser.find_element_by_xpath('//img[@class="live-video-cover"]').click()
    time.sleep(2)
    video_PageUrl = browser.current_url
    print("当前页面的url是：", video_PageUrl)
    browser.back()
    time.sleep(2)

    images = browser.find_elements_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div//div/img')
    price = browser.find_element_by_xpath('//*[@id="g-base"]/div[1]/span[1]/span[1]').text
    detail_images = browser.find_elements_by_xpath('//div[@class="_386c1C8A"]//img')
    detail_images_list = []
    image_index = 0
    for detail_image in detail_images:
        image_index += 1
        image_url = detail_image.get_attribute('data-src')
        if image_url == "none":
            continue
        if not os.path.exists("downloads/" + goods_id + "/goods_detail"):
            os.makedirs("downloads/" + goods_id + "/goods_detail")  # 如果没有这个path则直接创建
        filename = '{}{}{}'.format("downloads/" + goods_id + "/goods_detail/", image_index, '.jpg')

        print(filename)
        urllib.request.urlretrieve(image_url, filename=filename)
        detail_images_list.append(image_url)

    image_list = []
    image_index = 0
    for image in images:
        image_url = image.get_attribute('src')
        if image_url == "none" or image_url is None:
            continue
        print(image_url)
        image_list.append(image_url)
        image_index += 1
        if not os.path.exists("downloads/" + goods_id + "/goods"):
            os.makedirs("downloads/" + goods_id + "/goods")  # 如果没有这个path则直接创建
        filename = '{}{}{}'.format("downloads/" + goods_id + "/goods/", image_index, '.jpg')

        print(filename)
        urllib.request.urlretrieve(image_url, filename=filename)
        detail_images_list.append(image_url)
    print("标题：", title)
    print("价格：", price)
    print("图片url：", image_list)
    print("商品详情图片url：", detail_images_list)
    if not os.path.exists("datas/" + goods_id):
        os.makedirs("datas/" + goods_id)  # 如果没有这个path则直接创建
    with open(file="datas/" + goods_id + "/goods.csv", mode='w', encoding='utf-8', newline='') as f:
        write = csv.writer(f)
        write.writerow(['标题', '最低价格', '商品图片路径', '商品详情路径'])
        write.writerow([title, price, "downloads/" + goods_id + "/goods/", "downloads/" + goods_id + "/goods_detail/"])
    browser.find_element_by_xpath('//div[@class="_3dlX1BNw"]').click()

    time.sleep(1)
    items = browser.find_elements_by_xpath('//div[@class="sku-spec-value-list"]')
    if len(items) == 1:
        skus = browser.find_elements_by_xpath('//div[@class="sku-spec-value"]')
        image_index = 0
        if not os.path.exists("datas/" + goods_id):
            os.makedirs("datas/" + goods_id)  # 如果没有这个path则直接创建
        with open(file="datas/" + goods_id + "/sku.csv", mode='w', encoding='utf-8', newline='') as f:
            write = csv.writer(f)
            write.writerow(['规格', '价格', '图片路径'])
        for sku in skus:
            sku.click()
            sku_spec = browser.find_element_by_xpath('//div[@class="sku-spec-value sku-spec-value-selected"]').text
            sku_price = browser.find_element_by_xpath('//div[@class="_27FaiT3N"]').text
            sku_image = browser.find_element_by_xpath('//div[@class="_6DeKnpV8"]/img').get_attribute('src')

            image_index += 1
            if not os.path.exists("downloads/" + goods_id + "/goods_sku"):
                os.makedirs("downloads/" + goods_id + "/goods_sku")  # 如果没有这个path则直接创建
            filename = '{}{}{}'.format("downloads/" + goods_id + "/goods_sku/", image_index, '.jpg')
            with open(file="datas/" + goods_id + "/sku.csv", mode='a', encoding='utf-8', newline='') as f:
                write = csv.writer(f)
                write.writerow([sku_spec, sku_price, filename])
            print(filename)
            urllib.request.urlretrieve(sku_image, filename=filename)
            print(sku_spec, sku_price, sku_image)
    else:
        skus = browser.find_elements_by_xpath('//div[@class="sku-spec-value"]')
        # colors = browser.find_elements_by_xpath('//div[@class="r-mksVqr"]/div[@class="sku-spec-value-list"]//div')
        image_index = 0
        if not os.path.exists("datas/" + goods_id):
            os.makedirs("datas/" + goods_id)  # 如果没有这个path则直接创建
        with open(file="datas/" + goods_id + "/sku.csv", mode='w', encoding='utf-8', newline='') as f:
            write = csv.writer(f)
            write.writerow(['规格', '价格', '图片路径'])
        for index, sku_1 in enumerate(skus):
            try:
                sku_1.click()
            except:
                continue
            for sku_2 in skus[index + 1:]:
                try:
                    sku_2.click()
                except:
                    continue
                sku_price = browser.find_element_by_xpath('//div[@class="_27FaiT3N"]').text
                tmp_spec = browser.find_element_by_xpath('//div[@class="_2HvLhENT"]').text
                if sku_price.count('-') == 1:
                    sku_1.click()
                    continue
                sku_2.click()
                sku_spec = re.match("已选：(.*)", tmp_spec).group(1)

                sku_image = browser.find_element_by_xpath('//div[@class="_6DeKnpV8"]/img').get_attribute('src')

                image_index += 1
                if not os.path.exists("downloads/" + goods_id + "/goods_sku"):
                    os.makedirs("downloads/" + goods_id + "/goods_sku")  # 如果没有这个path则直接创建
                filename = '{}{}{}'.format("downloads/" + goods_id + "/goods_sku/", image_index, '.jpg')
                with open(file="datas/" + goods_id + "/sku.csv", mode='a', encoding='utf-8', newline='') as f:
                    write = csv.writer(f)
                    write.writerow([sku_spec, sku_price, filename])
                print(filename)
                urllib.request.urlretrieve(sku_image, filename=filename)
                print(sku_spec, sku_price, sku_image)

    # newline='' 作用去除行，若没有每添加一条数据，添加一空行
    browser.find_element_by_xpath('//div[@class="_2Geq26GV"]').click()
    js = "var q=document.documentElement.scrollTop=100000"
    browser.execute_script(js)
    time.sleep(3)
    try:
        browser.find_element_by_xpath('//div[@class="_1mw0PBZl"]').click()
        time.sleep(2)
    except:
        browser.execute_script("window.scrollTo(100,1200)")
        time.sleep(1)
        browser.find_element_by_xpath('//div[@class="_1mw0PBZl"]').click()
        time.sleep(2)

    browser.execute_script("window.scrollTo(100,500)")
    time.sleep(5)
    # js = "var q=document.documentElement.scrollTop=20000"
    # browser.execute_script(js)
    # time.sleep(5)
    # comments = browser.find_elements_by_xpath('//*[@id="goods-comments-list"]/div/div[1]//div[@class="_5u0xYxN0"]')
    scroll_size = 700
    if not os.path.exists("datas/" + goods_id):
        os.makedirs("datas/" + goods_id)  # 如果没有这个path则直接创建
    with open(file="datas/" + goods_id + "/comments.csv", mode='w', encoding='utf-8', newline='') as f:
        write = csv.writer(f)
        write.writerow(['用户名', '规格', '评论', '追评', '评论图片目录'])
    for i in range(20):
        print("第", i, "条评论")
        # time.sleep(2)
        try:
            comment = \
                browser.find_elements_by_xpath('//*[@id="goods-comments-list"]/div/div[1]//div[@class="_5u0xYxN0"]')[i]
        except:
            scroll_size += 500
            browser.execute_script("window.scrollTo(100," + str(scroll_size) + ")")
            time.sleep(2)
            comment = \
                browser.find_elements_by_xpath('//*[@id="goods-comments-list"]/div/div[1]//div[@class="_5u0xYxN0"]')[i]
        user = comment.find_element_by_xpath('div[1]/div').text
        text = comment.find_element_by_xpath('div[3]').text
        spec = comment.find_element_by_xpath('div[2]').text
        try:
            review = comment.find_element_by_xpath('div[6]').text
        except:
            review = ''
        # image = comment.find_element_by_xpath('div[4]/div[1]/div[1]').get_attribute('background-image')

        comment_images = comment.find_elements_by_xpath('div[4]/div')
        comment_image_list = []
        image_index = 0
        for comment_image in comment_images:
            image_tmp = comment_image.find_element_by_xpath("div").value_of_css_property('background-image')
            # print(image_tmp)

            while image_tmp == "none":
                browser.execute_script("window.scrollTo(100," + str(scroll_size) + ")")
                time.sleep(1)
                scroll_size += 300
                image_tmp = comment_image.find_element_by_xpath("div").value_of_css_property('background-image')
                print("图片未加载，正在下滑")
            image_index += 1
            image_url = re.match('url\(.*(http.*)"\)', image_tmp).group(1)
            if image_url == "none":
                continue
            if not os.path.exists("downloads/" + goods_id + "/goods_comments/comment_" + str(i)):
                os.makedirs("downloads/" + goods_id + "/goods_comments/comment_" + str(i))  # 如果没有这个path则直接创建
            filename = '{}{}{}'.format("downloads/" + goods_id + "/goods_comments/comment_" + str(i) + "/", image_index,
                                       '.jpg')

            print(filename)
            urllib.request.urlretrieve(image_url, filename=filename)
            comment_image_list.append(image_url)
        print("用户名：", user)
        print("规格：", spec)
        print("评论：", text)
        print("评论中图片url：", comment_image_list)
        print("追评：", review)
        with open(file="datas/" + goods_id + "/comments.csv", mode='a', encoding='utf-8', newline='') as f:
            write = csv.writer(f)
            write.writerow(
                [user, spec, text, review, "downloads/" + goods_id + "/goods_comments/comment_" + str(i) + "/"])

    return video_PageUrl


if __name__ == "__main__":
    # url = 'http://yangkeduo.com/goods.html?goods_id=215337688112&_oak_gallery=http%3A%2F%2Ft00img.yangkeduo.com%2Fgoods%2Fimages%2F2021-01-16%2F64b4c72791b9962c5ce59a5cac8dab4a.jpeg&_oak_rem_ar_id=999&page_from=35&refer_page_name=index&refer_page_id=10002_1611912254262_3brz7wsvsi&refer_page_sn=10002'
    # url = 'http://yangkeduo.com/goods.html?goods_id=216024081700&_oak_rem_ar_id=999&_oak_gallery=http%3A%2F%2Ft00img.yangkeduo.com%2Fgoods%2Fimages%2F2021-01-16%2Ff79e5ede04cbe666936822d743229791.jpeg&page_from=35&refer_page_name=psnl_varification&refer_page_id=10390_1612161675742_h9i2ba9swq&refer_page_sn=10390'
    url = "http://yangkeduo.com/goods.html?goods_id=83440081887&page_from=0&pxq_secret_key=57EZ56NPKDU35MDFXCQMGCZG6GIYWVJEWAJJGZA3GSQKWTAPX6IQ&share_uin=D2YTBA74JXGLH6VQDTWNB445GI_GEXDA&refer_share_id=a916d3488d114041bc707613c7b0334c&refer_share_uid=3327138972&refer_share_channel=message&refer_share_form=card&page_id=10014_1612171319914_cy4e698zwo&is_back=1"
    # goods_id = '215337688112'
    # goods_id = '216024081700'
    # goods_id = '83440081887'
    goods_id = get_goods_id(url)
    print(goods_id)
    # crawl(url, goods_id)
