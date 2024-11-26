import streamlit as st
import pandas as pd
import numpy as np
import altair as alt



st.header('st.write')

st.markdown("## This is a markdown header")
st.markdown("### This is a markdown header")
st.markdown("**Bold text** and *italic text* with markdown.")

st.header("This is a header")
st.subheader("This is a subheader")

st.caption("This is a caption, often used for small explanatory text.")

st.text("This is plain text.")

st.latex(r"""
a^2 + b^2 = c^2
""")

st.code("""
def hello():
    print("Hello, Streamlit!")
""", language="python")