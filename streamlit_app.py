import streamlit as st
from PIL import Image

st.info('Default')
with st.chat_message('assistant'):
  st.write('Hello world!')

st.warning('1. URL full path')
with st.chat_message('assistant', avatar='https://raw.githubusercontent.com/dataprofessor/streamlit-chat-avatar/master/bot-icon.png'):
  st.write('Hello world!')

st.warning('2. URL relative path')
with st.chat_message('assistant', avatar='bot-icon.png'):
  st.write('Hello world!')

st.warning('3. URL relative path 2')
with st.chat_message('assistant', avatar='./bot-icon.png'):
  st.write('Hello world!')

st.warning('4. URL relative path with Image.open')
with st.chat_message('assistant', avatar=Image.open('bot-icon.png')):
  st.write('Hello world!')

# Icon Credit
# https://www.flaticon.com/free-icon/bot_4712027
