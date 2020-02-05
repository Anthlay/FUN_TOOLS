import time

from progress.bar import IncrementalBar,Bar,ChargingBar,FillingCirclesBar,FillingSquaresBar,ShadyBar

mylist = [1,2,3,4,5,6,7,8]

bar = IncrementalBar('Countdown', max = len(mylist))

for item in mylist:
    bar.next(item+1)
    time.sleep(0.1)
bar.finish()
print(bar)