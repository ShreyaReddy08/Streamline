import streamlit as st
import pandas as pd

from streamlit_folder import app

st.title("Student Data")

data = {
    "Name": [
        "Ali",
        "Sara",
        "John",
        "Priya"
    ],

    "Course": [
        "Data Science",
        "Computer Science",
        "Data Science",
        "Software Engineering"
    ],

    "Mark": [
        72,
        65,
        81,
        69
    ]
}

df = pd.DataFrame(data)

st.write("### Student Dataset")

st.dataframe(df)

st.divider()

st.title('Editable DataFrame Example')
editable_df = st.data_editor(df, num_rows="dynamic")
st.divider()

import streamlit as st
import pandas as pd

st.title("Student Performance")

data = {
    "Student": [
        "Ali",
        "Sara",
        "John",
        "Priya"
    ],

    "Mark": [
        72,
        65,
        81,
        69
    ]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.subheader("Student Marks")

st.bar_chart(
    df,
    x="Student",
    y="Mark"
)

#-------------------------------------------------------------------------------------
##cd /workspaces/Streamlit_tutorial
#source .venv/bin/activate
#python -m pip install streamlit
#streamlit run streamlit_folder/app.py