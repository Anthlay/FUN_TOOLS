from phone import Phone
from openpyxl import load_workbook
def get_phone_region(phone_num):

    info = Phone().find(phone_num)
    if info is not None:
        region = info['province'] + ' ' + info['city'] + ' ' + info['phone_type']
    else:
        region = '该号码暂未查询到归属地，请检查号码正确性或手动查询！'
    return region
def add_exl(excel_path):
    excel = load_workbook(excel_path)  # 读取表格
    #sheet = excel.get_sheet_by_name(sheet_name)  # 读取指定名页签
    sheet = 1
    phone_col = sheet['I']  # 拿到C列
    for index in range(2, len(phone_col) + 1):  # 从C列第2行开始循环
        phone_data = sheet['I%s' % index]  # 拿到C列当前行单元格对象
        phone_num = phone_data.value.strip()  # 去除号码前后空格，得到号码字符串
        phone_region = get_phone_region(phone_num)  # 获得当前号码归属地
        print(phone_region)
        print('正在向J列第' + str(index) + '行(对应号码为' + phone_num + ')写入归属地信息: ' + phone_region)  # 打印出行数，号码，地区信息
        sheet['J%s' % index] = phone_region  # 将归属地内容写入D列对应行
    excel.save(excel_path)
if __name__ == '__main__':
    try:
        excel_path = "wuhan.xlsx"
        print("已读取excel")
        #sheet_name = input('请输入你要操作的sheet名(如果仅有一个sheet，请直接按enter):')
        #if sheet_name.strip() == '':
         #   sheet_name = None
        print("已进入")
        add_exl(excel_path)

    except Exception as e:
        print('[ERROR]发生错误:%s' % e)
p = Phone()
y=p.find(15629668188)
lct = y['province']+ ' ' + y['city'] + ' ' + y['phone_type']
pnumber = y['area_code']+' ' +y['phone']
print(pnumber)
print(lct)
print(y)
#return {'phone': '18100065143', 'province': '上海', 'city': '上海', 'zip_code': '200000', 'area_code': '021', 'phone_type': '电信'}