
import streamlit
import pandas


streamlit.title('My parents new health diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🫕 3 & Blueberry Oatmeal')
streamlit.text('🥗, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice')
import requests

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# put data in table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.header('Add a Fruit to the list')
added_fruit_text = streamlit.text_input('What fruit would you to add?','Grape')
streamlit.write('The user added ', added_fruit_text)

add_my_fruit_response = requests.get("https://fruityvice.com/api/fruit/" + added_fruit_text)
# put data in table
added_fruit = pandas.json_normalize(add_my_fruit_response.json())


