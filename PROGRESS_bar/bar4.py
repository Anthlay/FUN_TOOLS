import time
import logging
import progressbar

progressbar.streams.wrap_stderr()
logging.basicConfig()

for i in progressbar.progressbar(range(10)):
    logging.error('Got %d', i)
    time.sleep(0.2)