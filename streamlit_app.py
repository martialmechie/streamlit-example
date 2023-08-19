from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# Create a title for the app
st.title('Math Chatbot')

# Create a text input field
question = st.text_input('Enter your question:')

# Check if the user has entered a question
if question:

    # Try to parse the question as a math expression
    try:
        answer = np.eval(question)

    # If the question is not a valid math expression, show an error message
    except:
        st.error('Invalid math expression.')

    # Otherwise, show the answer to the question
    else:
        st.write('The answer is:', answer)
