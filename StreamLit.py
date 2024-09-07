import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Data App with Pandas and Numpy")

# Generate a random dataframe
data = np.random.randn(10, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

st.write("Here is a random dataset:")
st.dataframe(df)

# Show summary statistics
st.write("Summary statistics:")
st.write(df.describe())

# Select a column to show
column = st.selectbox("Select a column to display:", df.columns)
st.write(f"Data from column {column}:")
st.line_chart(df[column])