import streamlit as st
from planner import get_personalized_plan

# App title
st.title("StudBud: AI Personalized Study Planner")

# Input fields
st.header("Tell us about your study preferences:")
goals = st.text_area("What are your academic goals?", placeholder="E.g., Score 90% in exams, learn Python.")
strengths = st.text_area("What are your strengths?", placeholder="E.g., Good at Math, strong logical reasoning.")
weaknesses = st.text_area("What are your weaknesses?", placeholder="E.g., Struggle with time management, weak in History.")
preferences = st.text_area("What are your study preferences?", placeholder="E.g., Study at night, short sessions.")

# Generate plan button
if st.button("Generate My Study Plan"):
    if not (goals and strengths and weaknesses and preferences):
        st.warning("Please fill in all fields to get your personalized plan.")
    else:
        with st.spinner("Generating your study plan..."):
            plan = get_personalized_plan(goals, strengths, weaknesses, preferences)
        st.success("Here is your personalized study plan:")
        st.write(plan)