import streamlit as sl
import pandas as pd
import requests
import snowflake.connector

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
# New Header
sl.header("Fruityvice Fruit Advice!")

fruit_choice = sl.text_input('What fruit would you like information about?','Kiwi')
sl.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
sl.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
sl.text("Hello from Snowflake:")
sl.text(my_data_row)

