import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣omega 3 & blueberry oatmeal')
streamlit.text('🥗kale, spinach & Rocket')
streamlit.text('🐔Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_options = list(my_fruit_list.index)
default_fruits = ['Avocado', 'strawberries']

selected_fruits = streamlit.multiselect("Pick some fruits:", fruit_options, default_fruits)
fruits_to_show = my_fruit_list.loc[selected_fruits]

streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
