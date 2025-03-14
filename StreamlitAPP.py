import os 
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgen.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgen.MCQGenerator import generate_Quiz_Evaluate_Chain
from src.mcqgen.logger import logging 


# Load json file Manually from the folder
#with open('/Users/visakh/Desktop/Gen_AI/mcqgen/response.json', 'r') as file:
#    Response_JSON = json.load(file)

# Load json file dynamically from the folder in order to get production ready
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(script_dir, "response.json")

with open(json_path, 'r') as file:
    Response_JSON = json.load(file)




# Stremlit Part 

st.set_page_config(page_title='MCQ-Gen by Visakh', page_icon="📝", layout = 'centered', initial_sidebar_state = 'auto')


# Create a title for the app
st.title("MCQ Generator")

# Create a form using st.form 
with st.form("user_inputs"):
    # File uploder 
    uploaded_file = st.file_uploader("Upload a PDF or Txt file ", type=["pdf", "txt"])

    # Input for the number of questions
    mcq_count = st.number_input("Number of MCQs", min_value=3, max_value=50)

    # Input for the subject
    mcq_subject = st.text_input("Subject", max_chars=20, placeholder="Science, Maths, English etc")

    # Input the tone of MCQs
    mcq_tone = st.selectbox("Difficulty of the Quiz", ["Easy", "Medium", "Hard"])

    # Submit button
    button = st.form_submit_button("Generate MCQs")

    # Check if the button is clicked and all the input fields are filled 
    if button and uploaded_file is not None and mcq_subject and mcq_count and mcq_tone:
        with st.spinner("Generating MCQs"):
            try:
               TEXT = read_file(uploaded_file)
               # Count the tokens and the cost of API Call
               with get_openai_callback() as cb:
                    response = generate_Quiz_Evaluate_Chain(
                        {
                            "text" : TEXT,
                            "number" : mcq_count,
                            "subject" : mcq_subject,
                            "tone" : mcq_tone,
                            "response_json" : json.dumps(Response_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error in generating MCQs")
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Cost: {cb.total_cost}")
                if isinstance(response, dict):
                    # Extract the quiz data from the response
                    quiz=response.get("quiz")
                    print(quiz)
                    if quiz is not None:
                        # Get the table data
                        table_data = get_table_data(quiz)
                        if table_data:
                            # Create a dataframe
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            # Display the dataframe
                            st.table(df)
                            # Display the review in a text box
                            st.text_area("Review", response.get("review", "No Review"))
                        else:
                            st.error("Error in Table data")
                    else:
                        st.error("Error in Quiz data")

                else: 
                    st.write(response)