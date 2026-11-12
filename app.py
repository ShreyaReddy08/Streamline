import streamlit as st

# Part 1 — Your first Streamlit webpage

# Display a title
st.title("My First Streamlit Website")

# Display a heading
st.header("Welcome to Streamlit")

# Display some normal text
st.write("This is my first interactive website using Python.")
st.write(123)
st.write({'Name': "John", 'Age': 30, 'City': "New York"})

3+2
"Hello, World!"

# Display smaller text
st.caption("Created using Python and Streamlit")

st.divider()

#Part 3 — Different ways to display information

#-----------------------------------------------------
st.title("Learning Streamlit")

st.header("About this App")

st.subheader("What is Streamlit?")

st.write(
    "Streamlit allows us to create interactive "
    "web applications using Python."
)

st.info("This is an information message.")

st.success("The operation was successful!")

st.warning("Please check your input.")

st.error("Something went wrong!")

#-----------------------------------------------------
#Part 4 — User input
import streamlit as st

st.title("Student Information")

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=16,
    max_value=100
)

course = st.selectbox(
    "Select your course",
    [
        "Data Science",
        "Computer Science",
        "Software Engineering"
    ]
)

st.write("Name:", name)
st.write("Age:", age)
st.write("Course:", course)

#-----------------------------------------------------
st.title("Part 5a — Buttons")

pressed1 = st.button("Click Me")
print('first:', pressed1)

pressed2 = st.button("Click Me Too")
print('second:', pressed2)
#-----------------------------------------------------


import streamlit as st

st.title(" Part 5b (Buttons) — Welcome App")

name = st.text_input("What is your name?")

if st.button("Submit"):

    st.success("Information submitted!")

    st.write("Hello", name)
#-----------------------------------------------------
# Application with a button and conditional logic

import streamlit as st

st.title("Welcome App")

name1 = st.text_input("Enter another name:")

if st.button("Say Hello"):

    if name1:
        st.success(f"Hello {name1}! Welcome to the website.")
    else:
        st.warning("Please enter your name.")


st.title ("Part 6 — Sliders")     

import streamlit as st

st.title("Student Feedback")

rating = st.slider(
    "How would you rate today's class?",
    1,
    10,
    5
)

st.write("Your rating:", rating)

if rating >= 8:
    st.success("Great! We're glad you enjoyed the class.")

elif rating >= 5:
    st.info("Thank you for your feedback.")

else:
    st.warning("Thank you. We will try to improve.")

# st.title("Part 7 — Radio buttons and checkboxes")

import streamlit as st

st.title("Course Survey")

learning_mode = st.radio(
    "Preferred learning mode",
    [
        "Face-to-face",
        "Online",
        "Blended"
    ]
)

st.write("You selected:", learning_mode)

python_experience = st.checkbox(
    "I have used Python before"
)


if python_experience:
    st.write("Great! You already have some Python experience.")


st.title("Part 8 — Sidebar")

import streamlit as st

st.set_page_config(
    page_title="Student Dashboard",
    layout="wide"
)


st.title("Student Dashboard")


st.sidebar.header("Navigation")


page = st.sidebar.selectbox(
    "Choose a page",
    [
        "Home",
        "About",
        "Contact"
    ]
)


st.write("Selected page:", page)


# st.title("Part 8b — sidebar with radio buttons")
import streamlit as st

st.set_page_config(
    page_title="Student Website",
    layout="wide"
)

st.sidebar.title("Menu")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "About",
        "Contact"
    ]
)

if page == "Home":

    st.title("Home")
    st.write("Welcome to our website.")

elif page == "About":

    st.title("About")
    st.write(
        "This website was created using Python and Streamlit."
    )

elif page == "Contact":

    st.title("Contact")
    st.write("Email: example@email.com")


st.title("Part 9 — Columns")

import streamlit as st

st.title("Student Dashboard")
   
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Students", 120)

with col2:
    st.metric("Modules", 6)

with col3:
    st.metric("Average Mark", "68%")