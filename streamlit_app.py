import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

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

side_bar = st.sidebar.selectbox('What do you think the math behind is?',
           ('<select>',
            'Summing up all the integers from 0 up to and inluding n',
            'Multiplying all the integers from 1 up to and including n',
            'This is a Fibonacci Series.'))

if side_bar == 'Summing up all the integers from 0 up to and inluding n':
    st.write('That is correct. You, my friend, are a genius.')
elif side_bar == 'Multiplying all the integers from 1 up to and including n':
    st.write('Well, not quite! Would you like another guess?')
elif side_bar == 'This is a Fibonacci Series.':
    st.write('Good try but that is incorrect!')
else:
    st.write('')

df = pd.DataFrame({'name': ['John', 'Mary', 'Jane'],
                   'age': [9, 23, 56], 
                   'occupation': ['student', 'engineer', 'lawyer']})

# st.dataframe(df) # the same as st.write(df)
st.data_editor(df) # the same as st.dataframe but allows to enter your values into the table

df2 = pd.DataFrame(np.random.randn(50,4), columns=['rand_1', 'rand_2', 'rand_3', 'rand_4'])

alt_viz = alt.Chart(df2).mark_square().encode(x='rand_1', y='rand_2', size='rand_3', color='rand_3',
                                         tooltip=['rand_1', 'rand_2', 'rand_3'])

st.write(alt_viz)