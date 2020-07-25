# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:42:43 2020

@author: aitam
"""
import numpy as np
import pandas as pd
import tensorflow.keras as keras
import tensorflow as tf

#recuperer les deux matrice data
df_sans=np.genfromtxt('sans_feuilleton_scat_car.csv',delimiter=',',dtype=None)
df_avec=np.genfromtxt('avec_feuilleton_scat_car.csv',delimiter=',',dtype=None)

# width=725
# height=512
# width=int(360/2)
# height=int(252/2)


nbr=int(df_avec.shape[0]/2)
nbr1=int(df_sans.shape[0]/2)

t=256
#decouper et concatener les deux matrice data en deux autre train et test 
# x_train= np.concatenate((df_avec[:nbr, :width*height],df_sans[:nbr, :width*height]),axis=0)
# y_train= np.concatenate((df_avec[:nbr, width*height:],df_sans[:nbr, width*height:]),axis=0)
# x_test= np.concatenate((df_avec[nbr:, :width*height],df_sans[nbr:, :width*height]),axis=0)
# y_test= np.concatenate((df_avec[nbr:, width*height:],df_sans[nbr:,width*height :]),axis=0)
x_train= np.concatenate((df_avec[:nbr, :t],df_sans[:nbr1, :t]),axis=0)
y_train= np.concatenate((df_avec[:nbr,t:],df_sans[:nbr1, t:]),axis=0)
x_test= np.concatenate((df_avec[nbr:, :t],df_sans[nbr1:, :t]),axis=0)
y_test= np.concatenate((df_avec[nbr:, t:],df_sans[nbr1:,t :]),axis=0)

del df_avec
del df_sans



x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
y_train = tf.keras.utils.normalize(y_train, axis=1)
y_test = tf.keras.utils.normalize(y_test, axis=1)


#construire le structure de notre reseau de neurone 

model = keras.Sequential([
    keras.layers.Dense(256, activation='sigmoid', name="layer_in"),
    keras.layers.Dense(256, activation='sigmoid', name="layer_hidd"),
    keras.layers.Dense(1, activation='softmax', name="layer_out")
])

#model.compile(optimizer='rmsprop',loss='mse''categorical_crossentropy''binary_crossentropy', metrics=['accuracy'])

model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

# evaluer le model avec les donnee test 
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)
print(val_acc)

model.save('testing.model')