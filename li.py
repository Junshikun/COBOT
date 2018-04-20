import cv2
import os
import li
import numpy as np


def read_image_reader(data_dir_path):
    # http://t-nkb.hatenablog.com/entry/2016/12/08/204143
    # If you have any questions, plz open the above website at first.
    # 日本語の入った文字は、u'....' のように、頭に"u"をつけて、 この文字列がUTF-8で書かれている事を明言します。
    image_name_list = []
    file_list = os.listdir(data_dir_path)
    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == u'.png' or u'.jpeg' or u'.jpg':
            abs_name = data_dir_path + '/' + file_name
            image_name_list.append(abs_name)
            #  image = cv2.imread(abs_name)
            # 以下各画像に対する処理を記載する
    return image_name_list

def array_change(input_array):
    # This function changes the double nested list into the list.
    # For example
    # input:list_input=([321],[231],[321])
    # output:list_output=[321,231,321]
    output_array=[]
    for s in input_array:
        for class1 in s:
            output_array.append(class1)
    return output_array