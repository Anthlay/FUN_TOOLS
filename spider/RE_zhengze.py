import re

#re.match方法
list = "abcdefghijklmn"
m = re.match('abc',list)
#print(m)
print("match result：  ", m.span())
print("start position：", m.start())
print("end position：  ", m.end())
print()

list1="Fat cats are smarter than dogs"
m1 = re.match(r'(.*) are (.*?) dogs',list1)
#print (m1)
print('match whole sentence:',m1.group(0))
print('match first result:  ',m1.group(1))
print('match senond reault: ',m1.group(2))
print('match all relusts:   ',m1.groups())
print()

#re.search方法
#上述 match 和 search 方法中，只能找到一个匹配，而 findall 方法可以找到所有匹配
m_match = re.match('efg',list)
m_search= re.search('fgh',list)
print(m_match)
print(m_search)
print()

#re.findall方法
list2="12345 is the first number,67890 is the second number."
m1_match = re.match('[0-9]+',list2)
m1_search= re.search('[0-9]+',list2)
mi_findall=re.findall('[0-9]+',list2)
print(m1_match.group())
print(m1_search.group())
print(mi_findall)