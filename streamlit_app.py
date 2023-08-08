import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, time

st.header('Enter a number below and click the button. Can you guess what\'s the math\
          behind it?')

def sum_up_to_(n):
    val = 0
    for i in range(n + 1):
        val += i
    return val

user_num = st.number_input('Enter a number', format='%i', step=2) # min_value=0, max_value=99, step=1

if st.button('Compute'):
    # st.write(sum_up_to_(user_num))
    sum_ = sum_up_to_(user_num)
    st.write(sum_)
# else:
#     st.write('Hello')

ans_1 = 'Summing up all the integers from 0 up to and inluding n'
ans_2 = 'Multiplying all the integers from 1 up to and including n'
ans_3 = 'This is a Fibonacci Series'


side_bar = st.sidebar.selectbox('What do you think the math behind is?',
           ('<select>',
            ans_1,
            ans_2,
            ans_3))

if side_bar == ans_1:
    st.write('That is correct. You, my friend, are a genius.')
elif side_bar == ans_2:
    st.write('Well, not quite! Would you like another guess?')
elif side_bar == ans_3:
    st.write('Good try but that is incorrect!')
else:
    st.write('')

@st.cache_data
def df_and_viz(user_num):
    # Creating a dataframe based off of a user input number
    df = pd.DataFrame(np.random.randn(user_num, 2), columns=['rand_1', 'rand_2'])

    # st.dataframe(df) # the same as st.write(df)
    st.data_editor(df) # the same as st.dataframe but allows to enter your values into the table

    alt_viz = alt.Chart(df).mark_circle().encode(x='rand_1', y='rand_2', size='rand_1', color='rand_2',
                                            tooltip=['rand_1', 'rand_2'])

    st.write(alt_viz)

## Just deployed this to 30daysoflearning.streamlit.app
df_and_viz(user_num)


#Trying out st.slider

age = st.slider('Tell us your age', 1, 100, 26)
st.write('I\'m ', age, ' years old.')

busy_hrs = st.slider('During what hours of the day are you the busiest? Select a range', 
                     value=(time(9,30), time(18,30)))
st.write('Busy hours: ', busy_hrs)

sleep_hrs = st.slider('How many hours a day do you sleep?',
                      min_value=0, max_value=24, value=(4, 8))
st.write('Hours slept each day: ', sleep_hrs)