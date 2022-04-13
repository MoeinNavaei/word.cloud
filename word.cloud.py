# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import pandas as pd
import numpy as np
from PIL import Image
from wordcloud_fa import WordCloudFa
wc = WordCloudFa()
wc = WordCloudFa(width=1200, height=800) 
#wc.add_stop_words(['اینجور', 'کنم','بده','بسیاری','ایسایت','khamenei_ir','ما','نیست','لطفا','fln','تصویر','masale','اینگونه','asli','بصورت','نبود','ast','سر','دلایل'])
stop_words = set()
wc = WordCloudFa(persian_normalize=True)
wc = WordCloudFa(include_numbers=False)
#mask_array = np.array(Image.open("image.3.png"))
#wc = WordCloudFa(mask=mask_array)
#wc = WordCloudFa(background_color="white") 
w2=[]
w3=[]
#with open('khamenei_ir.txt', 'r', encoding='utf-8') as f:
#    y = f.read()
#word_cloud = wc.generate(y)
#image = word_cloud.to_image()
#image.show()
#image.save('khamenei.png')
#print (y)
with open('behnoosh_bakhtiari.json', 'r', encoding='utf-8') as f:
    y = json.load(f)
    f.close()


df0 = pd.DataFrame()
t=100

for k in range(0,t):
    try:
        z=y["GraphImages"][k]["comments"]
#        df0[k] = pd.DataFrame.from_dict(z)
#        print(z)
        for j in range(0,10000):
            try:
                w=z["data"][j]["text"]
                w2.append(w)
                
#                w3=list(itertools.chain.from_iterable(w2))
#                print(w2)
                
            except:
                pass
    
    except:
        pass
w3=''.join(w2) 
#print (w3)
word_cloud = wc.generate(w3)
image = word_cloud.to_image()
 
image.show()
image.save('khamenei.png')
#print (w)

#print(w)    
#print(w)
