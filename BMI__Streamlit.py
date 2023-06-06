# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 01:08:56 2023

@author: waiyan
"""
#import
import streamlit as st

#title
st.title ("Welcome to BMI Calculator")

#take input (Weight in kgs)
weight = st.number_input("Please Enter your Weight in kgs")
height = st.number_input("Please Enter your Height in cms")

try:
    bmi = weight / ((height/100)**2)
    
except:
    st.text("Enter some valuse of height")

#check if the button is pressed or not
if(st.button("Calculate BMI")):
    
    #print BMI index
    st.text("Your BMI is {}.".format(bmi))
    
    #give te interpertation of BMI index
    if(bmi<16):
        st.error("Yo, you need some milk fam")
        
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are not eating enough")
        
    elif(bmi >= 18.5 and bmi < 25):
        st.success("ooh, you fine as a greek god, keep up the drip my G")
    
    elif(bmi >= 25 and bmi < 30):
        st.warning("A little bit too much, go back")
        
    elif(bmi >= 30):
        st.error("American!")
        
        
        