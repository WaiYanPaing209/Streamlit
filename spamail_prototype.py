
### This whole program is entirely written from scratch by DS Garnett Dan Nu [Backend] and Wai Yan Paing [Frontend]. ###

#Import
import pandas as pd 
import joblib
from sklearn import set_config
import streamlit as st

# Set page config
st.set_page_config(
    page_title="Spam Email Detection",
    page_icon=":email:",
    layout="wide"
)


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

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-image: url('background.jpg');
        background-size: cover;
        color: white;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
    }
    .spam-text {
        font-size: 24px;
        color: red;
    }
    .not-spam-text {
        font-size: 24px;
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Streamlit UI
st.title("Spam Email Detection")

# Input text area for user to enter email paragraph
paragraph = st.text_area("Enter the email paragraph:")

# Button to predict
if st.button("Predict"):
    # Start word extraction
    word_appearances = count_word_appearances(paragraph, col_names)
    
    # Prepare data for prediction
    y_test = [word_appearances.get(word, 0) for word in col_names]
    y_test2d = [y_test]


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
joblib.dump(model, 'spamail_model.joblib', protocol=4)

# Remove feature names from the saved model
set_config(assume_finite=True)

#Spam or no spam?
result = model.predict(y_test2d)

# Display prediction result
if result[0] == 1:
    st.markdown('<p class="spam-text">Prediction: Spam</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="not-spam-text">Prediction: Not Spam</p>', unsafe_allow_html=True)
    
print(result)