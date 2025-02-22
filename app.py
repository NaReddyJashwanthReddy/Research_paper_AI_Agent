import streamlit as st
from model_llm import get_responce
from rad import retrive_data


st.title('AI Research Paper Assistant')
st.header('personal research assistant')

if 'messages' not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

prompt=st.chat_input("Type your research details here.......")

if prompt:
    st.session_state.messages.append({'role':'user','content':prompt})

    with st.chat_message('user'):
        st.write(prompt)


    retrive=retrive_data(prompt)
    retrive="\n".join(text for text in retrive['documents'][0])
    print(retrive)
    reasoning,responce=get_responce(prompt,retrive)
    
    st.session_state.messages.append({'role':'Agent','content':responce})

    with st.chat_message('ai'):
        st.write(responce)  

