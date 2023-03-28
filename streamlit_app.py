import streamlit as st
from streamlit_chat import message
import time
from chatCode import reply_to_question
import random

cnt = 0
if __name__ == '__main__':
    st.header('Duplicate ChatGPT')

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    with st.form('form', clear_on_submit=True):
        cnt += 1
        user_input = st.text_input('enter message : ', '')
        submitted = st.form_submit_button('submit', use_container_width=10)
    
    style = """
    <style>
     div[class='css-12ttj6m epcbefy1']{
                background: rgba(0, 0, 0, 0.3);
                position: fixed;
                bottom: 0;
                transform: translate(-50%, -50%);
                width: 40%;
                left: 50%;
                z-index: 999;
                margin-top: 10rem;
              }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

    if submitted and user_input:
        try:
            ans = reply_to_question(user_input)
            print(ans)
        except:
            ans = 'An error occured. Please try again later.'
        st.session_state.past.append(user_input)
        st.session_state.generated.append(ans)
        if 'key' not in st.session_state:
            st.session_state['key'] = time.time() + random.randint(0, 100)

        else:
            st.session_state['key'] = time.time() + random.randint(0, 100)

       
    for i in range(len(st.session_state['past'])):
        message(st.session_state['past'][i], is_user=True,key=str(time.time() + random.randint(100, 200)))
        if len(st.session_state['generated']) > i:
            message(st.session_state['generated'][i], key= str(time.time() + random.randint(300, 400)))