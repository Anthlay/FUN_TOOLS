from alive_progress import alive_bar,showtime
import time
mylist = [1,2,3,4,5,6,7,8]

with alive_bar(len(mylist)) as bar:

    for i in mylist:
        time.sleep(1)
        bar()

for x in 3000,4000,2000,0:
    with alive_bar(x) as bar:
        for i in range(3000):
            bar()
showtime()