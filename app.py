import streamlit as st 
from analyzers import rental

st.set_page_config(page_title='Deal Runner',layout='wide')

menu = st.sidebar.selectbox('Choose a Calculator',
    ['Rental Calculator', 'Flip Calculator', 'BRRRR Calculator', 'Rehab Calculator'])

if menu == 'Rental Calculator':
    rental.run()
elif menu == 'Flip Calculator':
    st.write("Flip Calculator is under construction.")