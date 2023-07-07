import streamlit as st

st.info('Default')
with st.chat_message('assistant'):
  st.write('Hello world!')

st.warning('URL full path')
with st.chat_message('assistant', avatar='https://raw.githubusercontent.com/dataprofessor/streamlit-chat-avatar/master/bot-icon.png'):
  st.write('Hello world!')



# Icon Credit
# https://www.flaticon.com/free-icon/bot_4712027
