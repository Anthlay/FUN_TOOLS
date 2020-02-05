import requests
from PIL import Image
from PIL.ExifTags import TAGS
import exifread
class Exif:

    def get_location(self, lon, lat):
        items = {'location': str(lat) + "," + str(lon), 'ak': self.ak, 'output': 'json'}
        header = {'Referer': '1.grayddq.top'}
        res = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items, headers=header).json()
        return res['result']['formatted_address'] if res['status'] == 0 else ""

if __name__ == '__main__':
    img_name = "e://pk1/2.jpg"
    for (k, v) in Image.open(img_name)._getexif().items():
        print('%s = %s' % (TAGS.get(k), v))

    f = open(img_name, 'rb')
    tag_c = {"制造厂商", "相机型号", "图象方向", "图象分辨率X", "图象分辨率Y", "分辨率单位", "", "", "", "", "", "", "", "", "", }
    tags = exifread.process_file(f)
    for tag in tags.keys():
        print(tag, tags[tag])

    f = open(img_name, 'rb')
    tags = exifread.process_file(f)
    # 拍摄时间
    time = tags["EXIF DateTimeOriginal"].printable
    # 纬度
    LatRef = tags["GPS GPSLatitudeRef"].printable
    Lat = tags["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    Lat = float(Lat[0]) + float(Lat[1]) / 60 + float(Lat[2]) / float(Lat[3]) / 3600
    if LatRef != "N":
        Lat = Lat * (-1)
    # 经度
    LonRef = tags["GPS GPSLongitudeRef"].printable
    Lon = tags["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    Lon = float(Lon[0]) + float(Lon[1]) / 60 + float(Lon[2]) / float(Lon[3]) / 3600
    if LonRef != "E":
        Lon = Lon * (-1)
    print('照相机品：', tags['Image Make'])
    print('照相机型号：', tags['Image Model'])
    print("拍摄时间:" + time)
    print('经纬度'+ str(Lat)+'  '+str(Lon))






