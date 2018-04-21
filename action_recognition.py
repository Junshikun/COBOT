from sklearn import svm
import cv2
import os
import junshi_function
import numpy as np

class utensil_recognize(object):
    def __init__(self
                 ,svm_address=None
                 ,utensil_win_size=(100,100)):
        self._svm_trainedmodel=svm_address
        self._utensil_win_size=utensil_win_size

    def generate_HOG_SVM_model(self):
        image_list = []  # we put all the address for the images in this list
        class_list = ['apple', 'banana', 'orange']
        # write the class name folder. the order is correspond to class_label
        # For example, first element is class1, second element is class2. and all the way down.
        for class_name in class_list:
            # the last back slash is added to find data properly
            training_data_address = "C:/Users/zhulab-2016-10/Desktop/test/" + class_name
            image_list.append(junshi_function.read_image_reader(training_data_address))
        print('We are going to calculate HOG features of every image')
        class_label = []
        count = 1  # This count is for labeling class
        block_size = (16, 16)
        block_stride = (4, 4)
        cell_size = (4, 4)
        bins = 9
        hog = cv2.HOGDescriptor(self._utensil_win_size, block_size, block_stride, cell_size, bins)
        for image_name in image_list: #Check each class. If class_list=['apple','banana','orange'], we check apple at first
            for class_1 in image_name:  # Calculate HOG Feature at each class/
                image = cv2.imread(class_1)  # read a image in a file
                image = cv2.resize(image, self._utensil_win_size)
                temp_array1 = hog.compute(image)  # Append HOG Feature
                temp_array2 = junshi_function.array_change(temp_array1)
                try:
                    HOG_feature #if HOG feature is not defined, we create
                except NameError: #If HOG_featuer is already defined
                    feature_dimention = len(temp_array2)
                    HOG_feature = np.empty((0, feature_dimention), int)
                    #HOG_featuer is a array consisted of 1 by n. Where n is the number of dimetion of HOG
                temp = np.array([temp_array2]) #Change the array into taple so that we can generate a SVM model.
                HOG_feature = np.append(HOG_feature, temp, axis=0)
                class_label.append(count)  # Put a label
            count = count + 1
        print('We finished to calculate HOG features./n We are going to generate the model with SVM')
        # 線形SVMのインスタンスを生成
        model = svm.SVC()
        # モデルの学習。fit関数で行う。
        model.fit(HOG_feature, class_label)
        print(model)



    def recognize_utensil(self):
        """Capture video from camera"""
        # カメラをキャプチャする
        cap = cv2.VideoCapture(0)  # 0はカメラのデバイス番号
        while(True):
            # retは画像を取得成功フラグ
            ret, frame = cap.read()
            cv2.imshow('camera capture', frame)
            # フレームを表示する
            # slide a window across the image
            step_size=10
            for y in range(0, frame.shape[0], step_size):
                for x in range(0, frame.shape[1], step_size):
                   # yield the current window
                    slide_image = frame[y:y + self._utensil_win_size[1], x:x + self._utensil_win_size[0], :]
                    #show the sliled image on the camera image
                    # cv2.imshow('camera capture', slide_image)
            k = cv2.waitKey(1)  # 1msec待つ
            if k == 27:  # ESCキーで終了
                break
        # キャプチャを解放する
        cap.release()
        cv2.destroyAllWindows()



s=utensil_recognize()
#s.recognize_utensil()
s.generate_HOG_SVM_model()