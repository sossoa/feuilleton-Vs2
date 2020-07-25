# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:39:12 2020

@author: aitam
"""

import os
from PIL import Image

path="data_base/sans_feuilleton/"
contenu=os.listdir(path)

        
         #parcourir les image et construir le la matrice data avec la meme dimmention 
for n in contenu:
    img = Image.open(path+n)
    size=img.size

#(left, top, left+width, top+height)
    area = (0, int(2*size[1]/3), size[0], size[1])
    cropped_img = img.crop(area).save('data_base_scat/sans_feuilleton/'+n)
    

path="data_base/avec_feuilleton/"
contenu=os.listdir(path)

        
         #parcourir les image et construir le la matrice data avec la meme dimmention 
for n in contenu:
    img = Image.open(path+n)
    size=img.size

#(left, top, left+width, top+height)
    area = (0, int(2*size[1]/3), size[0], size[1])
    cropped_img = img.crop(area).save('data_base_scat/savec_feuilleton/'+n)