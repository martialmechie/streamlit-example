from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import tensorflow as tf

# Create a title for the app
st.title('Math Chatbot')

# Create a text input field
question = st.text_input('Enter your question:')

# Check if the user has entered a question
if question:

    # Use vertex ai to answer the question
    model = tf.keras.models.load_model('model.h5')
    answer = model.predict([question])

    # Show the answer to the question
    st.write('The answer is:', answer)
