from time import sleep

from tqdm import tqdm, trange

for i in tqdm(range(100)):
     sleep(0.01)
for i in trange(100):
        sleep(0.01)

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)


with tqdm(total=100) as pbar:
    for i in range(10):
        pbar.update(10)


pbar1 = tqdm(total=100)
for i in range(10):
    pbar1.update(10)
pbar1.close()