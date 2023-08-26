
### This whole program is entirely written from scratch by DS Garnett Dan Nu [Backend] and Wai Yan Paing [Frontend]. ###

#Import
import pandas as pd 
import joblib
import streamlit as st

#Read
df = pd.read_csv('emails.csv')

#Extract the necessary column names (There are exactly 3000 column names)
df_list = df.columns[1:3001].values.tolist()

#Sort the columns
col_names = sorted(df_list)

#Word Extractor and counter
def count_word_appearances(paragraph, words):
    word_count = {}
    
    # Split the paragraph into words
    words_in_paragraph = paragraph.split()
    
    for word in words:
        count = words_in_paragraph.count(word)
        word_count[word] = count
        
    return word_count

# Streamlit UI
st.title("Spam Email Detection")

# Input text area for user to enter email paragraph
paragraph = st.text_area("Enter the email paragraph:")

# "Predict" button to trigger the prediction
if st.button("Predict"):
    # Start the extraction
    word_appearances = count_word_appearances(paragraph, col_names)
#Start the extraction
word_appearances = count_word_appearances(paragraph, col_names)

#Data list to test
y_test = []

#Count time!
for word, count in word_appearances.items():

    #print(f"'{word}' appears {count} times.") #this just for testing

    y_test.append(count)

#Reshape the array to 2D
y_test2d = [y_test]

#Import da MOOODEELL!
model = joblib.load("spamail_model.joblib")

#Spam or no spam?
result = model.predict(y_test2d)

if result[0] == 1:
   st.write("This email is predicted to be SPAM.")
else:
   st.write("This email is predicted NOT to be SPAM.")