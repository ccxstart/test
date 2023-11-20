import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False
import os
IMSIZE = 128
model = tf.keras.models.load_model('food_score.h5')
plt.ion()  # 打开动画开关
for root, sub, files in os.walk("test_pic/"):
    for file in files:
        plt.cla()
        img_name = os.path.join(root, file)

        mypic = Image.open(img_name)
        mypic=mypic.resize((IMSIZE, IMSIZE))
        mypic = np.array(mypic)/255

        mypic = mypic.reshape((1, IMSIZE, IMSIZE, 3))
        y_pred = model.predict(mypic)

        mypic = Image.open(img_name)
        plt.imshow(mypic)
        plt.title("美食评分{}".format(y_pred[0][0]))
        plt.pause(3)
plt.ioff()
plt.show()

