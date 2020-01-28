from cocoNLP.extractor import extractor
ex = extractor()
text = '急寻特朗普，男孩，于2018年11月27号11时在陕西省安康市汉滨区走失。丢失发型短发，...如有线索，请迅速与警方联系：18100065143，132-6156-2938，baizhantang@sina.com.cn 和yangyangfuture at gmail dot com'
# 抽取邮箱
emails = ex.extract_email(text)
print("邮箱：")
print(emails)
# 抽取手机号
cellphones = ex.extract_cellphone(text,nation='CHN')
print("手机号：")
print(cellphones)
# 抽取手机归属地、运营商
cell_locs = [ex.extract_cellphone_location(cell,'CHN') for cell in cellphones]

print("归属地，运营商：")
print(cell_locs)

# 抽取地址信息
locations = ex.extract_locations(text)
print("地址：")
print(locations)
# 抽取时间点
times = ex.extract_time(text)
print("时间点：")
print(times)

# 抽取人名
name = ex.extract_name(text)
print("人名")
print(name)
