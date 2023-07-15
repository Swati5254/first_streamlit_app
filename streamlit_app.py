import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣omega 3 & blueberry oatmeal')
streamlit.text('🥗kale,spinach & Rocket')
streamlit.text('🐔Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

fruit_options = list(my_fruit_list.index)
default_fruits = ['Avocado', 'strawberries']

print("Options in CSV file:", fruit_options)
print("Default values:", default_fruits)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
