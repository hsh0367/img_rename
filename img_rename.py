
import sys
import os
import datetime
files_path = "./asset/" 
def img_rename(start_num, path):
    path = str(path) + "/"
    file_name_and_time_lst = []
    for file_item in os.listdir(f"{path}"):
        filename, fileExtension = os.path.splitext(file_item)
        if fileExtension in [".png", ".jpeg", ".jpg"]:
            written_time = os.path.getctime(f"{path}{file_item}")
            file_name_and_time_lst.append((file_item, written_time))
    sorted_file_list = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=False)
    recent_file = sorted_file_list[0]
    start_int = start_num
    for image in sorted_file_list:
        create_time=datetime.datetime.fromtimestamp(image[1])
        print(f'{image[0]} {create_time}')
        src = os.path.join(path, image[0])
        dst = str(start_int) + '.png'
        dst = os.path.join(path, dst)
        os.rename(src, dst)
        start_int += 1


def if_integer(string):
    if string[0] == ('-', '+'):
        return string[1:].isdigit()

    else:
        return string.isdigit()
