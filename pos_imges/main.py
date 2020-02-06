# -*- encoding: utf-8 -*-

import os
import exifread
from decimal import Decimal
import m_utils
import requests
import json
import datetime

class Location(object):

    def __init__(self, image_path):
        self.img_path = image_path
        self.api_key = "9d3f867e3d8abb92fefde881a8cadd57"
        self.url_get_position = 'https://restapi.amap.com/v3/geocode/regeo?key={}&location={}'
    def run(self):

        location_info = self.__get_image_ability()
        if not location_info:
            return
        # 根据经度和纬度，获取到详细地址
        address = self.__get_address(location_info)
        # 检验坐标值
        # https://lbs.amap.com/console/show/picker


    def __get_address(self, location):
        """
        根据坐标得到详细地址
        :param location: 经纬度值
        :return:
        """
        resp = requests.get(self.url_get_position.format(self.api_key, location))
        location_data = json.loads(resp.text)
        address = location_data.get('regeocode').get('formatted_address')
        print(f'当前位置在：{address}')
        return address

    def __format_lati_long_data(self, data):
        """
        对经度和纬度数据做处理，保留6位小数
        :param data: 原始经度和纬度值
        :return:
        """
        # 删除左右括号和空格
        data_list_tmp = str(data).replace('[', '').replace(']', '').split(',')
        data_list = [data.strip() for data in data_list_tmp]

        # 替换秒的值
        data_tmp = data_list[-1].split('/')
        # 秒的值
        data_sec = int(data_tmp[0]) / int(data_tmp[1]) / 3600
        # 替换分的值
        data_tmp = data_list[-2]
        # 分的值
        data_minute = int(data_tmp) / 60
        # 度的值
        data_degree = int(data_list[0])
        # 由于高德API只能识别到小数点后的6位
        # 需要转换为浮点数，并保留为6位小数
        result = "%.6f" % (data_degree + data_minute + data_sec)
        return float(result)

    def __get_image_ability(self):
        """
        获取图片的属性值，包含：经纬度、拍摄时间等
        :param picture_name:
        :return:
        """
        # 利用exifread库，读取图片的属性,提取tag
        img_tags = exifread.process_file(open(self.img_path, 'rb'))
        # 能够读取到属性
        if img_tags:
            # 纬度数
            latitude_gps = img_tags['GPS GPSLatitude']
            # N,S 南北纬方向
            latitude_direction = img_tags['GPS GPSLatitudeRef']
            # 经度数
            longitude_gps = img_tags['GPS GPSLongitude']
            # E,W 东西经方向
            longitude_direction = img_tags['GPS GPSLongitudeRef']
            # 拍摄时间
            take_time = img_tags['EXIF DateTimeOriginal']
            take_time = img_tags['EXIF DateTimeOriginal']
            print('照相机品：', img_tags['Image Make'])
            print('照相机型号：', img_tags['Image Model'])
            print(f"照片拍摄时间：{take_time}")
            # 纬度、经度、拍摄时间
            if latitude_gps and longitude_gps and take_time:
                # 对纬度、经度值原始值作进一步的处理，不处理的话，有偏差
                latitude = self.__format_lati_long_data(latitude_gps)
                longitude = self.__format_lati_long_data(longitude_gps)
                # print(f'{longitude},{latitude}')
                # 这里需要转换为火星坐标系
                location = m_utils.wgs84togcj02(longitude, latitude)
                return f'{location[0]},{location[1]}'
            else:
                print(f'获取的图片数据属性不完整')
                return ''
        else:
            print('抱歉，图片不是原图，没法获取到图片属性。')
            return ''

if __name__ == '__main__':
    # 【原图路径】
    location = Location('e://pk1/12.jpg')
    # 运行
    location.run()