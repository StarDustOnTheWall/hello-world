import pandas as pd
import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier, KerasRegressor
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import RMSprop, Adam
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
# import seaborn as sns

from tensorflow_practice.utility.normalization import normalization_pipe


# def get_histplot_central_tendency(df: dict, fields: list):
#     for field in fields:
#         f, (ax1) = plt.subplots(1, 1, figsize=(9, 4))
#         v_dist_1 = df[field].values
#         sns.histplot(v_dist_1, ax=ax1, color=get_random_color(), kde=True)
#
#         mean=df[field].mean()
#         median=df[field].median()
#         mode=df[field].mode().values[0]
#
#         ax1.axvline(mean, color='r', linestyle='--', label="Mean")
#         ax1.axvline(median, color='g', linestyle='-', label="Mean")
#         ax1.axvline(mode, color='b', linestyle='-', label="Mode")
#         ax1.legend()
#         plt.grid()
#         plt.title(f"{field} - Histogram analysis")

def create_models(activation='relu', dropout_rate=0.2,
                  optimizer='Adam'):
    model = Sequential()
    model.add(layers.Dense(32, activation=activation, input_shape=(num_input_features,)))
    model.add(layers.Dense(32, activation=activation))
    model.add(layers.Dense(32, activation=activation))
    model.add(layers.Dense(num_classes, activation='softmax'))
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    # model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy',
    #               metrics=['accuracy'])
    return model


df = pd.read_csv('WineQT.csv')
column_list = df.columns.to_list()
for key in ['quality', 'Id']:
    column_list.remove(key)
num_classes = len(set(df['quality'].tolist()))
# num_classes = max(set(df['quality'].tolist()))+1

pipe = normalization_pipe(numeric_index=column_list)
output_pipe = normalization_pipe(cat_index=[('quality', None)])
x = pipe.fit_transform(df[column_list])
num_input_features = x.shape[-1]
y = output_pipe.fit_transform(df[['quality']]).A
# y = df['quality'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)


# history = model.fit(x=x_train, y=y_train, steps_per_epoch=100, epochs=20, validation_data=(x_test, y_test))
# loss = model.evaluate(x_test, y_test)
# y_predict = model.predict(x)
# class_predict = (y_predict > 0.5).astype("int32")
# classes_predict_b = np.argmax(y_predict, axis=1)
# score = accuracy_score(y, y_predict)

keras_model = create_models()
cv_model = KerasClassifier(build_fn=create_models)
param_grid = {
              'epochs': [1, 2, 3],
              'batch_size': [128],
              #'epochs' :              [100,150,200],
              #'batch_size' :          [32, 128],
              #'optimizer' :           ['Adam', 'Nadam'],
              #'dropout_rate' :        [0.2, 0.3],
              'activation':          ['relu', 'elu']
             }
grid = GridSearchCV(estimator=cv_model, param_grid=param_grid)
grid_result = grid.fit(x_train, y_train)


# loss = history.history['loss']
# val_loss = history.history['val_loss']
# epochs = range(1, len(loss) + 1)
# plt.figure()
# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.legend()
# plt.show()