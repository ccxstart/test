import tensorflow as tf
import numpy as np
import pickle

model = tf.keras.models.load_model('poem_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


poem_incomplete = 'bbb郑****州****工****商****'
poem_index = []
poem_text = ''
for i in range(len(poem_incomplete)):
    current_word = poem_incomplete[i]
    if current_word != '*':
        # 给定的词
        index = tokenizer.word_index[current_word]
    else:
        # 根据前三个词预测 *
        x = poem_index[-3:]
        y = model.predict(np.expand_dims(x, axis=0))[0]
        index = y.argmax()
        current_word = tokenizer.index_word[index]

    poem_index.append(index)
    poem_text = poem_text + current_word

poem_text = poem_text[3:]
print(poem_text[0:5])
print(poem_text[5:10])
print(poem_text[10:15])
print(poem_text[15:20])