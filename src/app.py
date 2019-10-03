import streamlit as st 
import pandas as pd
import numpy as np 
import time

df = pd.DataFrame({
    'a': [1, 2, 4],
    'b': ['hello', 'again', 'world']
})

'''
# This is a title
## and another header

First take for a streamlit app
'''

"### Showing some data if you want to"

yes_checkbox = st.checkbox('Show me some data')

if yes_checkbox:
    'arrr off treasure hunting'
    st.dataframe(df)

'----'

"and a table"
st.table(df)

'''
## Selecting **stuff**
'''
x = st.slider('Select value')
st.write(x, 'squared', x*x)
y = st.slider("Another slieder")
st.write('call both:', x*y)

'----'

option = st.selectbox(
    'Which number do you like best?',
     ['this one', 'no this one']
     )

'You selected: ', option, 'an excellent choice!'

'----'
'Making plots is also easy'

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'----'
'## Fancy some buttons'

if st.button('click me and see what happens'):
    'hello mate'
else:
    'whatcha looking'

'----'
text = st.text_area('Tell me your secret', '''
    I am not a pirate!
''')

st.write('A shocking confession was made:', text)

st.success('You did it!')
st.warning('and a warning')