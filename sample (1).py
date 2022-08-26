
from PIL import Image
from keras.preprocessing.image import load_img,img_to_array
import numpy as np
from keras.models import load_model
import requests
from bs4 import BeautifulSoup
import tensorflow as tf
import os
import csv
import pandas as pd
import itertools as IT

root = os.getcwd()
imagePath = os.path.join(root, 'images')
labelsPath = os.path.join(root, 'labels')
linksPath = os.path.join(imagePath, 'imageLinks')
trainPath = os.path.join(imagePath, 'train')
testPath = os.path.join(imagePath, 'test')

model = load_model('Vv.h5')
 
meal = ['Khichdi','Aloo_sabji_chapati','Dal_rice','Pohe','Aloo_puri']


def fetch_calories(prediction):
    try:
        myDataframe = pd.read_csv("products.csv")
        
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        theRate = float(interestingRow["calories"])
        return theRate
        
        
    except Exception as e:
        print("Can't able to fetch the Calories")
        print(e)

def fetch_proteins(prediction):
    try:
        myDataframe = pd.read_csv("products.csv")

    
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        theRate1 = float(interestingRow["proteins"])
        return theRate1

    except Exception as e:
        print("Can't able to fetch the Proteins")
        print(e)

def processed_img(img_path):
    img=load_img(img_path,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = meal[y]
    print(res)
    return res.capitalize()



def run(img_file = "C:/my folder/dataset_pics/DR (1).jpg"):
    
    save_image_path = img_file
    
    if img_file is not None:
            
        result= processed_img(save_image_path)
        print(result)
        if result in meal:
                print('**Category : meal**')
            
        cal = fetch_calories(result)
        pro = fetch_proteins(result)
        

        if cal < 450:
            ans = 450 - cal
            
            df2 = pd.read_csv("products.csv")
            df2 = df2.sort_values('calories')
            df2 = df2[df2["calories"] <= ans]
            lol = df2.values.tolist()
            

            



    
        if pro < 12:
            ans = 12 - pro
          
            df2 = pd.read_csv("products.csv")
            df2 = df2.sort_values('proteins')
            df2 = df2[df2["proteins"] <= ans]
            lol1 = df2.values.tolist()
            

        return{
            "proteins" : pro,
            "calories" : cal,
            "suggestions_to__satisfy_calories":lol,
            "suggestions_to_satisfy_proteins":lol1
        }


        
    


if __name__ == "__main__":
    ans = run()
    print(ans)