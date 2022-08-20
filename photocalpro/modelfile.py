# import streamlit as st
from PIL import Image as image
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
from io import BytesIO
import urllib
# import image

def loadImage(URL):
    with urllib.request.urlopen(URL) as url:
        img = image.load_img(BytesIO(url.read()), target_size=(125, 125))

    return image.img_to_array(img)


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
meal = ['Khichdi','Aloo_sabji_chapati','Dal_rice','Pohe','Aloo_puri']



# os.system('python dataset.py')

# fruits = ['Apple','Banana','Bello Pepper','Chilli Pepper','Grapes','Jalepeno','Kiwi','Lemon','Mango','Orange','Paprika','Pear','Pineapple','Pomegranate','Watermelon']
# vegetables = ['Beetroot','Cabbage','Capsicum','Carrot','Cauliflower','Corn','Cucumber','Eggplant','Ginger','Lettuce','Onion','Peas','Potato','Raddish','Soy Beans','Spinach','Sweetcorn','Sweetpotato','Tomato','Turnip']

def fetch_calories(prediction):
    try:
        myDataframe = pd.read_csv("products.csv")

        # Convert 'Rates' column to float (if needed)
        # myDataframe = myDataframe.astype({"calories":"float"})

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
        print("Can't able to fetch the Calories")
        print(e)

def fetch_proteins(prediction):
    try:
        myDataframe = pd.read_csv("products.csv")

        # Convert 'Rates' column to float (if needed)
        # myDataframe = myDataframe.astype({"proteins":"float"})

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
        print("Can't able to fetch the Proteins")
        print(e)

def processed_img(img_path):
    # img=load_img(img_path,target_size=(224,224,3))
    img=loadImage(img_path)
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


def run(img_file = "C:/my folder/sih/dal rice.jpg"):
    # st.title("* Meal Calorie & Protein Predictor *")
    
    # st.markdown(unsafe_allow_html=True)
    # img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    # img_file = 'https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/khichdi-recipe-1.jpg'
    # if img_file is not None:
    # img = Image.open(img_file).resize((250,250))
    # # st.image(img,use_column_width=False)
    save_image_path = img_file
    # with open(save_image_path, "wb") as f:
    #     f.write(img_file.getbuffer())

        # if st.button("Predict"):
    if img_file is not None:
            
        result= processed_img(save_image_path)
        print(result)
        if result in meal:
                print('**Category : meal**')
            # else:
            #     st.info('**Category : Fruit**')
        # st.success("**Predicted : "+result+'**')
        cal = fetch_calories(result)
        # print(cal)
        # return cal
        # if cal <= 450:
        #     print("1")
        # else:
        #     p
        pro = fetch_proteins(result)
        # print(pro)
        # return pro
        return{
            "proteins" : pro,
            "calories" : cal
        }


        # if cal:
        #     st.warning(cal)
        #     st.warning(pro)

# ans = run()

# def return_calories_proteins(image= "C:/my folder/sih/dal rice.jpg"):
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

if __name__ == "__main__":
    ans = run('https://sih-django.run-ap-south1.goorm.io/media/images/meals/St.%20Xaviers%20High%20School%20-%20(Mumbai)/2022-08-08/Tanaya.2022-08-08.WhatsApp_I_eerqA5b.jpeg')
    print(ans)