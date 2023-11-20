"""
@coding: utf-8
@author: 星辰
@date: 2023/9/17 15:57
"""
import requests
from lxml import etree
import random
import traceback
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import pymysql


class Data:
    def __init__(self):
        self.headers = {
            'Cookie': 'lianjia_uuid=1d97d769-d34a-454e-8baf-aac8aa406a90; gr_user_id=78811c46-43de-40e1-9556-73a22c974a5b; _smt_uid=64112593.522a41a5; _ga=GA1.2.891075059.1678845333; _jzqc=1; _qzjc=1; _gid=GA1.2.1862046156.1694838529; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1694866687; _ga_KJTRWRHDL1=GS1.2.1694866675.1.1.1694866716.0.0.0; _ga_QJN1VP0CMS=GS1.2.1694866675.1.1.1694866716.0.0.0; crosSdkDT2019DeviceId=-3x64fd--sua0yd-imbstgm2schvejd-segn2vt8y; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22186e2fac76f691-01c32910ef4066-26031951-1327104-186e2fac770131f%22%2C%22%24device_id%22%3A%22186e2fac76f691-01c32910ef4066-26031951-1327104-186e2fac770131f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _jzqy=1.1681196644.1694936491.1.jzqsr=baidu.-; _jzqckmp=1; _jzqa=1.3797889365898060000.1678845331.1694936491.1694943928.8; _jzqx=1.1694881859.1694943928.2.jzqsr=zz%2Elianjia%2Ecom|jzqct=/ershoufang/.jzqsr=zz%2Elianjia%2Ecom|jzqct=/ershoufang/jinshuiqu/pg2/; _qzja=1.2022150959.1681196643579.1694936491425.1694943927664.1694943927664.1694943951916.0.0.0.19.6; _qzjto=8.3.0; _ga_WLZSQZX7DE=GS1.2.1694944077.2.0.1694944077.0.0.0; _ga_TJZVFLS7KV=GS1.2.1694944077.2.0.1694944077.0.0.0; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1694944109; _ga_654P0WDKYN=GS1.2.1694944085.1.1.1694944110.0.0.0; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiOGE5MWM4ODNmMWUyZmUzN2EyMTA3ZDI5ZmNkN2YxYWQ1OGQ2NzYyOTJiOTAxMmYzOWQ4NTJlNTZlYzM4NmM4ZWI1OTQ2M2NhMzQ5MTNjNGRlNWZhNDA5MDExM2UxMTZhODcwODAyZjBiYTk3OTUyZTMwYTAyOTBiNTk1MmZjY2M2MDk4NTZiNGIwNDM3Zjc2OWJkZjZlY2Q1MmI3NDNkYTEzNjVhZTYwMDAzNjg4NTkyM2NhYmJiMmU4MTAzOWUyODI3YzNiODBjMTQxMGEwNjQ2MDY3MWRkMDA3YzMxYWE1Mjc0YjhlYmJjYjc5YzQ4OGJkOGJlMWFmYzkzMTk1ZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0NTExOWY2ZlwifSIsInIiOiJodHRwczovL3p6LmxpYW5qaWEuY29tL3p1ZmFuZy9lcnFpcXUvcGczLyNjb250ZW50TGlzdCIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; lianjia_ssid=e4edc3ab-a6c5-1c76-fb33-3572c2d79b4b; select_city=440100',
            'User-Agent': UserAgent().Chrome,
        }
        self.url_list = []
        self.db_connection = pymysql.connect(
            host="localhost",  # 数据库服务器主机名
            user="root",  # 数据库用户名
            password="",  # 数据库密码
            database="flask_graduation"  # 数据库名称
        )
        # 创建游标对象
        self.cursor = self.db_connection.cursor()

    def get_urls_data(self, city_url_list):
        """
        获取每个城市的信息
        :param city_url_list:
        :return: url_list
        """
        for i in city_url_list:
            try:
                province = i['province']
                city = i['city_name']
                url = i['city_url']
                response = requests.get(url=url, headers=self.headers)
                tree = etree.HTML(response.text)
                li_list = tree.xpath('//*[@id="filter"]/ul[2]/li')[1:]
                for li in li_list:
                    downtown_name = li.xpath('./a/text()')[0]
                    page_url = url[0:-8] + li.xpath('./a/@href')[0]
                    for j in range(1, random.randint(15, 25)):
                        downtown_url = page_url + f'pg{str(j)}/'
                        self.url_list.append({'province': province, 'city': city, 'downtown_name': downtown_name,
                                              'downtown_url': downtown_url})
                    print(f'正在提交: {province}--{city}--{downtown_name}  ！！！')

            except Exception as e:
                print(e)
        # print(self.url_list)
        return self.url_list

    def get_datas(self, url_list):
        """
        遍历每一页的url地址，获取每一页的房价数据信息，存入数据库中。
        :param url_list: 每一页的url地址
        :return:
        """
        province = url_list['province']
        city = url_list['city']
        downtown = url_list['downtown_name']
        url = url_list['downtown_url']
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            tree = etree.HTML(response.text)
            div_list = tree.xpath('//*[@id="content"]/div[@class="content__article"]/div[@class="content__list"]/div')
            for div in div_list:
                try:
                    db_connection = pymysql.connect(
                        host="localhost",  # 数据库服务器主机名
                        user="root",  # 数据库用户名
                        password="",  # 数据库密码
                        database="flask_graduation"  # 数据库名称
                    )
                    # 创建游标对象
                    cursor = db_connection.cursor()

                    # 介绍
                    introduce = \
                        div.xpath(
                            './div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a/text()')[
                            0].strip()
                    address_list = \
                        div.xpath('./div[@class="content__list--item--main"]/p[@class="content__list--item--des"]/a')

                    # 详细地址
                    address = ''
                    for i in address_list:
                        j = i.xpath('./text()')[0].strip()
                        address += '-'
                        address += j
                    address = address[1:]

                    three_list = div.xpath(
                        './div[@class="content__list--item--main"]/p[@class="content__list--item--des"]//text()')

                    # 房屋面积
                    area = three_list[8].strip()
                    # 朝向
                    orientation = three_list[10].strip()
                    # 格局
                    pattern = three_list[12].strip()

                    # 每月租金
                    rent = div.xpath(
                        './div[@class="content__list--item--main"]/span[@class="content__list--item-price"]/em/text()')[
                        0].strip()

                    # 链接
                    link = url[0:22] + div.xpath(
                        './div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a/@href')[
                        0].strip()

                    # SQL 插入语句
                    insert_query = "INSERT INTO t_data_all (province, city, downtown, introduce, address, area, orientation, pattern, rent, link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    # 插入数据
                    data_to_insert = (
                    province, city, downtown, introduce, address, area, orientation, pattern, rent, link)
                    # 关闭游标和连接
                    cursor.execute(insert_query, data_to_insert)
                    db_connection.commit()

                    print(province, city, downtown, introduce, address, area, orientation, pattern, rent, link)
                    cursor.close()
                    db_connection.close()
                except Exception as e:
                    print(e)
                    traceback.print_exc()

    def get_city_url(self):
        """
        city_url_list: 每一个市级地区的租房url列表
        :return: city_url_list
        """
        city_url_list = []
        url = 'https://www.lianjia.com/city/'
        res = requests.get(url=url, headers=self.headers)
        city_list_ul = etree.HTML(res.text)
        li_list = city_list_ul.xpath('/html/body/div[2]/div[2]/div/div/ul/li')[9:]
        for li in li_list:
            province_list = li.xpath('./div[@class="city_list"]/div')
            for x in province_list:
                province = x.xpath('./div/text()')[0]
                city_list = x.xpath('./ul/li')
                for city in city_list:
                    try:
                        city_name = city.xpath('./a/text()')[0]
                        city_url = city.xpath('./a/@href')[0] + 'zufang/'
                        print({'province': province, 'city_name': city_name, 'city_url': city_url})
                        city_url_list.append({'province': province, 'city_name': city_name, 'city_url': city_url})
                    except Exception:
                        traceback.print_exc()
        # print(city_url_list)
        return city_url_list


if __name__ == '__main__':
    data = Data()
    # data.get_urls_data()
    city_url_list = data.get_city_url()
    url_list = data.get_urls_data(city_url_list)
    # data.get_datas(url_list)
    # print(url_list)

    with ThreadPoolExecutor(max_workers=4) as Pool:
        result = Pool.map(data.get_datas, url_list)
