# -*- coding: utf-8 -*-
'''
@File     : test.py
@Author   : fuzizhu
@Software : PyCharm
@Project  : pinduoduo
@Date     : 2021/2/1 17:50
@Desc     : 
'''
import requests


def download_videofile(video_links):
    root = 'test'
    for link in video_links:
        file_name = 'test.mp4'
        print("文件下载:%s" % file_name)
        print(link)
        r = requests.get(link, stream=True).iter_content(chunk_size=1024 * 1024)
        with open(root + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s 下载完成!\n" % file_name)
    print("所有视频下载完成!")
    return


if __name__ == "__main__":
    video_links = ['http://liveplay.pddpic.com/live/17283_production_sprite_20210114_2683653_03.m3u8?txSecret=6e26542c6334702bb4935936a90094e6&txTime=60190fa0&pub_type=tx-pddobs']
    download_videofile(video_links)
