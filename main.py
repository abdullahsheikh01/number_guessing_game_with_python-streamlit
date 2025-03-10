import streamlit as st
import random
st.set_page_config(
    page_title="Number Guessing Game By Abdullah Shaikh",
    page_icon="icon.png"
)
# Title of Page
st.markdown(
    """## Number Guessing Game By [Abdullah Shaikh](https://www.linkedin.com/in/abdullah-shaikh-29699b302/)
    """
)
# Session Variable random_number initialization
if 'random_number' not in st.session_state:
     st.session_state.random_number = 0
# Guessing Number function to check guess number
def guessing_check(user_guess:int,random_number:int,start_range:int,end_range:int):
        if(user_guess<start_range):
            st.write("Your guess is lower than range")
        elif(user_guess>end_range):
            st.write("Your guess is higher than range")
        elif(user_guess==random_number):
            st.success("Booyah! You guess correct Number")               
        elif(user_guess>random_number):
            remainder_number : int = user_guess-random_number
            if(remainder_number>=10):
                st.write("Your guess is too high!")
            elif(remainder_number<10):
                st.write("Your guess is little high!")
        elif(user_guess<st.session_state.random_number):
                remainder_number : int = random_number-user_guess
                if(remainder_number>=10):
                    st.write("Your guess is too low!")
                elif(remainder_number<10):
                    st.write("Your guess is little low!")
        else:
            st.write(3)
# Range of Guessing numbers
st.session_state.start_range = st.number_input("Range of numbers from ",format="%d",step=1,key=1)
st.session_state.end_range  = st.number_input("to ",format="%d",step=1,min_value=st.session_state.start_range+5,key=2)
if 'start_range_with_random' not in st.session_state and  'end_range_with_random' not in st.session_state: 
    st.session_state.start_range_with_random = 0
    st.session_state.end_range_with_random = 5
# Confirm the number of range and generating random number
if st.button("Confirm range"):
    st.session_state.random_number=random.randint(st.session_state.start_range,st.session_state.end_range)
    st.session_state.start_range_with_random = st.session_state.start_range
    st.session_state.end_range_with_random = st.session_state.end_range
# Taking Guess Number from user
user_guess : int = int(st.number_input("Enter your guess number",format="%d",step=1,key=3))
# Confirming Guess Number and check it by function
if st.button("Confirm Guess"):
    guessing_check(user_guess,st.session_state.random_number,st.session_state.start_range_with_random,st.session_state.end_range_with_random)