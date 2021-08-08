# -*- coding: utf-8 -*-
'''
@File     : main.py
@Author   : fuzizhu
@Software : PyCharm
@Project  : pinduoduo
@Date     : 2021/2/2 11:15
@Desc     : 
'''
from pinduoduo import crawl, get_goods_id
from video import get_video_url

if __name__ == "__main__":
    # url = 'http://yangkeduo.com/goods.html?goods_id=215337688112&_oak_gallery=http%3A%2F%2Ft00img.yangkeduo.com%2Fgoods%2Fimages%2F2021-01-16%2F64b4c72791b9962c5ce59a5cac8dab4a.jpeg&_oak_rem_ar_id=999&page_from=35&refer_page_name=index&refer_page_id=10002_1611912254262_3brz7wsvsi&refer_page_sn=10002'
    # url = 'http://yangkeduo.com/goods.html?goods_id=216024081700&_oak_rem_ar_id=999&_oak_gallery=http%3A%2F%2Ft00img.yangkeduo.com%2Fgoods%2Fimages%2F2021-01-16%2Ff79e5ede04cbe666936822d743229791.jpeg&page_from=35&refer_page_name=psnl_varification&refer_page_id=10390_1612161675742_h9i2ba9swq&refer_page_sn=10390'
    # url = "http://yangkeduo.com/goods.html?goods_id=83440081887&page_from=0&pxq_secret_key=57EZ56NPKDU35MDFXCQMGCZG6GIYWVJEWAJJGZA3GSQKWTAPX6IQ&share_uin=D2YTBA74JXGLH6VQDTWNB445GI_GEXDA&refer_share_id=a916d3488d114041bc707613c7b0334c&refer_share_uid=3327138972&refer_share_channel=message&refer_share_form=card&page_id=10014_1612171319914_cy4e698zwo&is_back=1"
    url = 'https://yangkeduo.com/goods1.html?goods_id=175273997100&page_from=23&pxq_secret_key=HK5FZO7TZCPHUJHNWJ5ORND64OVKEUWGEGVT5CPEQZKO4NN3IVBA&share_uin=D2YTBA74JXGLH6VQDTWNB445GI_GEXDA&refer_share_id=8b2f5843c4b54a0eab1c0d8c14f1be03&refer_share_uid=3327138972&refer_share_channel=message&refer_share_form=card'
    goods_id = get_goods_id(url)
    video_url = crawl(url, goods_id)
    get_video_url(video_url, goods_id)
