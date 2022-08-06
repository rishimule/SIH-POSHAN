import streamlit as st
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
# from google.colab import drive

# root = os.getcwd()
# imagePath = os.path.join(root, 'images')
# labelsPath = os.path.join(root, 'labels')
# linksPath = os.path.join(imagePath, 'imageLinks')
# trainPath = os.path.join(imagePath, 'train')
# testPath = os.path.join(imagePath, 'test')

model = load_model('FV.h5')
# labels = "C:/Users/mahee/OneDrive/Desktop/sih6/indian_food.csv"
labels = {0:'Dal_rice',1:'Kichdi',2:'chapati'}
meal = ["Dal_rice","Kichdi","Chapati"]  
# os.system('python dataset.py')

# fruits = ['Apple','Banana','Bello Pepper','Chilli Pepper','Grapes','Jalepeno','Kiwi','Lemon','Mango','Orange','Paprika','Pear','Pineapple','Pomegranate','Watermelon']
# vegetables = ['Beetroot','Cabbage','Capsicum','Carrot','Cauliflower','Corn','Cucumber','Eggplant','Ginger','Lettuce','Onion','Peas','Potato','Raddish','Soy Beans','Spinach','Sweetcorn','Sweetpotato','Tomato','Turnip']

def fetch_calories(prediction):
    try:
        myDataframe = pd.read_csv("products.csv")

        # Convert 'Rates' column to float (if needed)
        myDataframe = myDataframe.astype({"calories":"float"})

        # Extract the 'interesting' row by using this notation
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        # Extract the rate value from the row
        theRate = str(interestingRow["calories"])
        return theRate
        # url = pd.read_csv('C:/Users/mahee/OneDrive/Desktop/sih_final/products.csv in' + prediction)
        # req = requests.get(url).text
        # scrap = BeautifulSoup(req, 'html.parser')
        # calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        # return calories
        
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)

def fetch_proteins(prediction):
    try:
        myDataframe = pd.read_csv("products.csv")

        # Convert 'Rates' column to float (if needed)
        myDataframe = myDataframe.astype({"proteins":"float"})

        # Extract the 'interesting' row by using this notation
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        # Extract the rate value from the row
        theRate1 = str(interestingRow["proteins"])
        return theRate1
        # url = 'https://www.google.com/search?&q=proteins in' + prediction
        # req = requests.get(url).text
        # scrap = BeautifulSoup(req, 'html.parser')
        # proteins = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        # return proteins
    except Exception as e:
        st.error("Can't able to fetch the Proteins")
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
    res = labels[y]
    print(res)
    return res.capitalize()




# def return_calories_proteins(image='https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/khichdi-recipe-1.jpg',meal_name='Khicdi'):
#     """_summary_
#     Args:
#         image (_type_): Image of  meal
#         meal_name (_type_): Name of meal
#     Returns:
#         Dict: {proteins, calories}
#     """
#     # your code here
#     result= processed_img(image)
#     cal = fetch_calories(result)
#     pro = fetch_proteins(result)

    

#     return {
#         'proteins' : pro,
#         'calories' : cal,
        
#     }


def return_calories_proteins(image='https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/khichdi-recipe-1.jpg',meal_name='Khicdi'):
    """_summary_
    Args:
        image (_type_): Image of  meal
        meal_name (_type_): Name of meal
    Returns:
        Dict: {proteins, calories}
    """
    # your code here
 

    return {
        'proteins' : 66,
        'calories' : 225.6,
        
    }

if __name__ == "__main__":
    ans = return_calories_proteins()
    print(ans)