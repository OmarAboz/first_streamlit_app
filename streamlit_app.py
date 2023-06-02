import streamlit as sl
import pandas as pd
import requests

sl.title("My Parents Healthy Diner")

sl.header("Breakfast Menu")

# Main healthy options
sl.text("🥣 Omega 3 & Blueberry Oatmeal")
sl.text("🥗 Kale, Spinach & Rocket Smoothie")
sl.text("🐔 Hard-Boiled Free-Range Egg")
sl.text("🥑🍞 Avocado Toast")

# Creating Smoothie section
sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Allow selection of the fruits
fruits_selected = sl.multiselect("Please pick some fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_display = my_fruit_list.loc[fruits_selected]

#Display the data frame for the user to select the items
sl.dataframe(fruits_display)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
sl.text(fruityvice_response)
