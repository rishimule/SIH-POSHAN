from PIL import Image
import requests
from bs4 import BeautifulSoup
import tensorflow as tf
import os
import csv
import pandas as pd
import itertools as IT

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

meal = ['Khichdi','Aloo_sabji_chapati','Dal_rice','Pohe','Aloo_puri']

# name = st.text_input("Enter level")

# if name == "Primary":
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

    except Exception as e:
        print("Can't able to fetch the Calories")
        print(e)


def fetch_proteins(prediction):
    try:
        myDataframe = pd.read_csv("products.csv") 

        # Convert 'Rates' column to float (if needed)
        myDataframe = myDataframe.astype({"proteins":"float"})

        # Extract the 'interesting' row by using this notation
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        # Extract the rate value from the row
        theRate = float(interestingRow["proteins"])
        return theRate
    
    except Exception as e:
        print("Can't able to fetch the proteins")
        print(e)

# elif name == "Upper Primary":
def fetch_calories1(prediction):
    try:
        myDataframe = pd.read_csv("products2.csv")

        # Convert 'Rates' column to float (if needed)
        myDataframe = myDataframe.astype({"calories":"float"})

        # Extract the 'interesting' row by using this notation
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        # Extract the rate value from the row
        theRate = float(interestingRow["calories"])
        return theRate
        
    except Exception as e:
        print("Can't able to fetch the Calories")
        print(e)

def fetch_proteins1(prediction):
    try:
        myDataframe = pd.read_csv("products2.csv")

        # Convert 'Rates' column to float (if needed)
        myDataframe = myDataframe.astype({"proteins":"float"})

        # Extract the 'interesting' row by using this notation
        interestingRow = myDataframe[myDataframe["Meal"] == prediction]

        # Extract the rate value from the row
        theRate = float(interestingRow["proteins"])
        return theRate

    except Exception as e:
        print("Can't able to fetch the proteins")
        print(e)
# else:
#     print("Invalid Input")

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


def run1(img_file):
    # st.title("* Meal Calorie & Protein Predictor *")
    
    # # st.markdown(unsafe_allow_html=True)
    # img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    # # img_file = 'https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/khichdi-recipe-1.jpg'
    # if img_file is not None:
    #     img = Image.open(img_file).resize((250,250))
    #     st.image(img,use_column_width=False)
    #     save_image_path = 'C:/my folder/dataset_pics'+img_file.name
    #     with open(save_image_path, "wb") as f:
    #         f.write(img_file.getbuffer())

        save_image_path = img_file
        if img_file is not None:
            result= processed_img(save_image_path)
            print(result)
            if result in meal:
                print('**Category : meal**')
            # else:
            #     print('**Category : Fruit**')
            print("**Predicted : "+result+'**')
            cal = fetch_calories(result)#imp
            print(cal)#imp
            
            pro = fetch_proteins(result)#imp
            # print(pro)#imp

            if cal < 450:
                ans = 450 - cal
            
                df2 = pd.read_csv("products.csv")
                df2 = df2.sort_values('calories')
                df2 = df2[df2["calories"] <= ans]
                lol = df2.values.tolist()
            
            else:
                lol = "Condition satisfied"

            if pro < 12:
                ans = 12 - pro
                df2 = pd.read_csv("products.csv")
                df2 = df2.sort_values('proteins')
                df2 = df2[df2["proteins"] <= ans]
                lol1 = df2.values.tolist()

            else:
                lol1 = "Condition satisfied"

            return {
                'calories':str(cal),
                'proteins':str(pro),
                "suggestions to satisfy calories": str(lol),
                'suggestions to satisfy proteins':str(lol1)
            }
            
            # if cal:#imp
            #     st.warning("calories: "+str(cal))#imp
            #     st.warning("proteins: "+str(pro))#imp
            #     st.warning("suggestions to satisfy calories: "+str(lol))
            #     st.warning("suggestions to satisfy proteins: "+str(lol1))


def run2(img_file):
    # st.title("* Meal Calorie & Protein Predictor *")
    
    # # st.markdown(unsafe_allow_html=True)
    # img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    # # img_file = 'https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/khichdi-recipe-1.jpg'
    
    
    # if img_file is not None:
    #     img = Image.open(img_file).resize((250,250))
    #     st.image(img,use_column_width=False)
    #     save_image_path = 'C:/my folder/dataset_pics'+img_file.name
    #     with open(save_image_path, "wb") as f:
    #         f.write(img_file.getbuffer())

        # if st.button("Predict"):
        
        save_image_path = img_file
        if img_file is not None:
            result1= processed_img(save_image_path)
            print(result1)
            if result1 in meal:
                print('**Category : meal**')
            # else:
            #     print('**Category : Fruit**')
            print("**Predicted : "+result1+'**')
            cal1 = fetch_calories1(result1)#imp
            # print(cal)#imp
            
            pro1 = fetch_proteins1(result1)#imp
            # print(pro)#imp

            if cal1 < 700:
                ans1 = 700 - cal1    
            
                df2 = pd.read_csv("products2.csv")
                df2 = df2.sort_values('calories')
                df2 = df2[df2["calories"] <= ans1]
                lol3 = df2.values.tolist()
            
            else:
                lol3 = "Condition satisfied"

            if pro1 < 20:
                ans1 = 20 - pro1
                df2 = pd.read_csv("products2.csv")
                df2 = df2.sort_values('proteins')
                df2 = df2[df2["proteins"] <= ans1]
                lol4 = df2.values.tolist()

            else:
                lol4 = "Condition satisfied"

            return {
                'calories':str(cal1),
                'proteins':str(pro1),
                "suggestions to satisfy calories": str(lol3),
                'suggestions to satisfy proteins':str(lol4)
            }
            
            # if cal1:#imp
            #     st.warning("calories: "+str(cal1))#imp
            #     st.warning("proteins: "+str(pro1))#imp
            #     st.warning("suggestions to satisfy calories: "+str(lol3))
            #     st.warning("suggestions to satisfy proteins: "+str(lol4))

# name = st.text_input("Enter level")



def final_run(img):
    primary = run1(img)
    print('+'*300)
    print(primary)
    upper_primary = run2(img)
    print('+'*300)
    print(upper_primary)
    
    return {
        'primary':primary,
        'upper_primary':upper_primary
    }







# if name == "Primary":
#     run1()

# elif name == "Upper Primary":
#     run2()

# else:
#     print("Invalid Input")







    
    
    


