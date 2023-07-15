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
