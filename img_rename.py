
import sys
import os
files_path = "./asset/" 
file_name_and_time_lst = []
for f_name in os.listdir(f"{files_path}"):
    written_time = os.path.getctime(f"{files_path}{f_name}")
    file_name_and_time_lst.append((f_name, written_time))
sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
recent_file = sorted_file_lst[0]
start_int = int(input('숫자를 입력해주세요 : '))
for image in sorted_file_lst:
    if image[0] != ".gitkeep":
        src = os.path.join(files_path, image[0])
        dst = str(start_int) + '.png'
        dst = os.path.join(files_path, dst)
        os.rename(src, dst)
        start_int += 1
