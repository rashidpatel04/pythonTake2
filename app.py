import streamlit  as st
email = st.text_input('Enter email: ')
password = st.text_input('Enter password: ')

btn = st.button('Login Karo!')
if btn:
    if email == 'amangupta@gmail.com' and password == '12345':
        st.balloons()
        st.write()
    else:
        st.error('Login Failed!')