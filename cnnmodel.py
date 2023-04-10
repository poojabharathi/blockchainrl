import numpy as np
import pandas as pd
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
import pickle

train = pd.read_csv('/data/inputs/dataset_shard1.csv')
# split the datasets into features and labels
X_train, y_train = train.iloc[:, 1:].values / 255.0, train.iloc[:, 0].values
# reshape the input data to 28x28x1 (since MNIST images are grayscale)
X_train = X_train.reshape(-1, 28, 28, 1)
# one-hot encode the target variable
y_train = np_utils.to_categorical(y_train)

# define the CNN architecture
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# train the model
model.fit(X_train, y_train, epochs=2, batch_size=128, verbose=1)

#get the weights of the model
model_weights = model.get_weights()

#pickle the weights
with open('/data/outputs/model_weights.pkl', 'wb') as f:
    pickle.dump(model_weights, f)





