from filter import DFAFilter

f=DFAFilter()
f.add("sexy")
y=f.filter("hello sexy baby")
print(y)