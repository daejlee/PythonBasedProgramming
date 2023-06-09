import os
import datetime
from random import choice

#현재 폴더의 파일 목록 생성
cur_list = os.listdir()

dir_name = "current_time"

if dir_name in cur_list:
    pass
else:
    os.mkdir(dir_name)

#current_time 디렉토리로 이동
os.chdir(dir_name)

with open("now.txt", "w") as f:
     f.write("현재 폴더의 목록: ")
     for item in cur_list:
            f.write(item)
     f.write("\n그 중에 하나를 랜덤하게 선택: ")
     f.write(choice(cur_list))
     f.write("\n")
     now = datetime.datetime.now()
     f.write(now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))