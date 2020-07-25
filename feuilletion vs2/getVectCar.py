# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 00:15:03 2020

@author: aitam
"""


def get_Vec_Car(path,dis_file,t):
 import csv
 import os
 from PIL import Image
 import numpy as np
 
 contenu=os.listdir(path)
 data=[]
 a=[0]*256
         #parcourir les image et construir le la matrice data avec la meme dimmention 
 for n in contenu:
    img = Image.open(path+n)
    img= img.convert('L')
    size=img.size
    try:
                 if size[2]==3:
                   img=np.array((img[:,:,0]+img[:,:,1]+img[:,:,2])/3)
                   
    except :
                   v=np.array(img)
    v=np.array(v)
    
    for i in  range(len(v)):
      for j in range(len(v[0])):
         
            a[v[i,j]]= a[v[i,j]]+1
       
      
    data = np.concatenate((data,a),axis=0)
      
    for i in  range(len(a)):
        a[i]=0


 data= np.reshape(data,(len(contenu),256))
 if t==1 :
              y=np.ones(len(contenu))
        
 else :
              y=np.zeros(len(contenu))
      
 data= np.c_[data,y]


 #enregister la marrice dans un fichier csv
 with open(dis_file, 'w', newline='\n') as csvfile:
             writer = csv.writer(csvfile, delimiter=',')    
             for row in data:
                 writer.writerow(row)
        

 csvfile.close()