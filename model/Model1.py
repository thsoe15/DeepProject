from keras.utils import plot_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, Concatenate, BatchNormalization
from keras.models import Sequential
import os

batch_size = 32
# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['1 Papilionidae', '2 Pieridae']

# Training data
training_data = os.path.join(root_path, '..', 'data', 'dataset', 'model1', 'train')

# Validation data
validation_data = os.path.join(root_path, '..', 'data', 'dataset', 'model1', 'validation')

trainImageDataGen = ImageDataGenerator(rescale=1 / 255., horizontal_flip=True)
validationImageDataGen = ImageDataGenerator(rescale=1 / 255.)

trainGen = trainImageDataGen.flow_from_directory(
    training_data,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode="binary")

valGen = validationImageDataGen.flow_from_directory(
    validation_data,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode="binary")

# Test Model in the making - Thor


model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), strides=1, padding=None, activation='relu'))
model.add(MaxPooling2D(pool_size=[2, 2], strides=1, padding='same', data_format=None))
model.add(Conv2D(32, kernel_size=(3, 3), strides=1, padding=None, activation='relu'))
model.add(MaxPooling2D(pool_size=[2, 2], strides=1, padding='same', data_format=None))
model.add(Conv2D(32, kernel_size=(3, 3), strides=1, padding=None, activation='relu'))
model.add(MaxPooling2D(pool_size=[2, 2], strides=1, padding='same', data_format=None))
model.add(Flatten(data_format=None))
model.add(Dense(units=2, activation='softmax'))

model.save('task2Subtask1Test')
plot_model(model, to_file='model.png')

np_epoch = 10

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit_generator(trainGen, epochs=np_epoch, batch_size=batch_size, validation_data=valGen)

# inputLayer = Input(batch_shape=(batch_size,) + trainGen.shape[1:])

# conv2d_1 = Conv2D(32, kernel_size=(3,3), strides=1,padding='none', activation='relu')(inputLayer)
# maxPooling_1 = MaxPooling2D(pool_size=[2,2],strides=1, padding='same', data_format=None)(conv2d_1)
# conv2d_2 = Conv2D(32, kernel_size=(3,3), strides=1,padding='none', activation='relu')(maxPooling_1)
# maxPooling_2 = MaxPooling2D(pool_size=[2,2],strides=1, padding='same', data_format=None)(conv2d_2)
# conv2d_3 = Conv2D(32, kernel_size=(3,3), strides=1,padding='none', activation='relu')(maxPooling_2)
# maxPooling_3 = MaxPooling2D(pool_size=[2,2],strides=1, padding='same', data_format=None)(conv2d_3)
# flatLayer = Flatten(data_format=None)(maxPooling_3)
# outputLayer = Dense(units=2,activation='softmax')(flatLayer)'


##model = Model(inputLayer, outputLayer)
