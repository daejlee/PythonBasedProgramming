import os
import random as r
from datetime import datetime
try:
    os.mkdir("./current_time")
except:
    pass
f = open("./current_time/now.txt", "w")
for i in os.listdir(os.curdir):
    f.write(i)
f.write(r.choice(os.listdir(os.curdir)))
now = datetime.now()
f.write(now.strftime('%Y-%m-%d %H:%M:%S'))
f.close()