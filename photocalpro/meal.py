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

root = os.getcwd()
imagePath = os.path.join(root, 'images')
labelsPath = os.path.join(root, 'labels')
linksPath = os.path.join(imagePath, 'imageLinks')
trainPath = os.path.join(imagePath, 'train')
testPath = os.path.join(imagePath, 'test')
 
model = load_model('Vv.h5')
# labels = "C:/Users/mahee/OneDrive/Desktop/sih6/indian_food.csv"
# labels = {0:'Dal_rice',1:'Kichdi',2:'chapati'}
# meal = ["Dal_rice","Kichdi","Chapati"]  
# meal = ['Dal_rice','Chole_chapati','Idli_sambhar','Pohe','Khichdi','Aloo_sabji_chapati','Aloo_puri','Chole_and_puri']
meal = ['Khichdi','Aloo_sabji_chapati','Dal_rice','Pohe','Aloo_puri']
# meal = 'poha khicdi eggs'.split()
# os.system('python dataset.py')

# fruits = ['Apple','Banana','Bello Pepper','Chilli Pepper','Grapes','Jalepeno','Kiwi','Lemon','Mango','Orange','Paprika','Pear','Pineapple','Pomegranate','Watermelon']
# vegetables = ['Beetroot','Cabbage','Capsicum','Carrot','Cauliflower','Corn','Cucumber','Eggplant','Ginger','Lettuce','Onion','Peas','Potato','Raddish','Soy Beans','Spinach','Sweetcorn','Sweetpotato','Tomato','Turnip']

# imp
def fetch_calories(prediction):
    try: 
        myDataframe = pd.read_csv("products.csv")

        # Convert 'Rates' column to float (if needed)
        myDataframe = myDataframe.astype({"calories":"float"})

        # Extract the 'interesting' row by using this notation
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        # Extract the rate value from the row
        theRate = float(interestingRow["calories"])
        return theRate
        # url = pd.read_csv('C:/Users/mahee/OneDrive/Desktop/sih_final/products.csv in' + prediction)
        # req = requests.get(url).text
        # scrap = BeautifulSoup(req, 'html.parser')
        # calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        # return calories
        
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)

# imp
def fetch_proteins(prediction):
    try:
        myDataframe = pd.read_csv("products.csv")

        # Convert 'Rates' column to float (if needed)
        myDataframe = myDataframe.astype({"proteins":"float"})

        # Extract the 'interesting' row by using this notation
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        # Extract the rate value from the row
        theRate1 = float(interestingRow["proteins"])
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
    res = meal[y]
    print(res)
    return res.capitalize()
 


def run():
    st.title("* Meal Calorie & Protein Predictor *")
    
    # st.markdown(unsafe_allow_html=True)
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    # img_file = 'https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/khichdi-recipe-1.jpg'
    if img_file is not None:
        img = Image.open(img_file).resize((250,250))
        st.image(img,use_column_width=False)
        save_image_path = 'C:/my folder/dataset_pics'+img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # if st.button("Predict"):
        if img_file is not None:
            
            result= processed_img(save_image_path)
            print(result)
            if result in meal:
                st.info('**Category : meal**')
            # else:
            #     st.info('**Category : Fruit**')
            st.success("**Predicted : "+result+'**')
            cal = fetch_calories(result)#imp
            # print(cal)#imp
            
            pro = fetch_proteins(result)#imp
            # print(pro)#imp

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


            if cal:#imp
                st.warning("calories: "+str(cal))#imp
                st.warning("proteins: "+str(pro))#imp
                st.warning("suggestions to satisfy calories: "+str(lol))
                st.warning("suggestions to satisfy proteins: "+str(lol1))
                # st.warning('**Calories: '+cal+'(100 grams)**')
                # st.warning('**Proteins: '+pro+'(100 grams)**')

run()