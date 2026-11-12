import streamlit as st

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------

st.set_page_config(
    page_title="Student Portal",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("🎓 Student Portal")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Student Form",
        "Dashboard"
    ]
)


# -----------------------------------
# HOME PAGE
# -----------------------------------

if page == "Home":

    st.title("Student Portal")

    st.write(
        """
        Welcome to the Student Portal.

        This application demonstrates how Python
        can be used to build interactive websites
        using Streamlit.
        """
    )

    st.info(
        "Use the menu on the left to navigate through the application."
    )


# -----------------------------------
# STUDENT FORM
# -----------------------------------

elif page == "Student Form":

    st.title("Student Information")

    name = st.text_input(
        "Student Name"
    )

    age = st.number_input(
        "Age",
        min_value=16,
        max_value=100
    )

    course = st.selectbox(
        "Course",
        [
            "Data Science",
            "Computer Science",
            "Software Engineering"
        ]
    )

    year = st.radio(
        "Year of Study",
        [
            "Year 1",
            "Year 2",
            "Year 3"
        ]
    )

    if st.button("Submit"):

        st.success(
            "Student information submitted successfully!"
        )

        st.write("### Student Details")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Course:", course)
        st.write("Year:", year)


# -----------------------------------
# DASHBOARD
# -----------------------------------

elif page == "Dashboard":

    st.title("Student Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Students",
            120
        )

    with col2:

        st.metric(
            "Courses",
            5
        )

    with col3:

        st.metric(
            "Average Mark",
            "68%"
        )

    st.write("---")

    st.subheader("Dashboard Information")

    st.write(
        """
        Later we can replace these values with
        real information from a dataset.
        """
    )