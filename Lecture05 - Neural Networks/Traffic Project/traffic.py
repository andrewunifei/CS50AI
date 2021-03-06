# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 20/02/2021
#
# Os conteúdos de todas as funções, exceto a main, foram implementados por mim

import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    path = str(data_dir) + os.sep
    images = list()
    labels = list()

    for folder in os.listdir(path):
        for file in os.listdir(os.path.join(path, folder)):
            img = cv2.imread(os.path.join(path, folder, file), cv2.IMREAD_UNCHANGED)
            img_resized = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT)) 

            images.append(img_resized)
            labels.append(int(folder))

    return images, labels

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([
                # Convolução 2D
                # A rede neural irá aprender 64 filtros,
                # os filtros aplicados têm dimensões 3x3
                Conv2D(64, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
                # Max pooling aplicado terá as dimensões 2x2
                MaxPooling2D(pool_size=(2, 2)),

                Conv2D(64, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
                MaxPooling2D(pool_size=(2, 2)),

                # Flatten: a entrada da camada densa tem que ser 1D,
                # a funão Flatten recebe um tensor 2D das camadas anteriores e o converte para 1D
                Flatten(),
                
                Dense(units=128, activation='relu'),
                Dropout(0.5),

                # Ativação 'softmax' representa uma distribuição de probabilidade
                Dense(units=NUM_CATEGORIES, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


if __name__ == "__main__":
    main()
