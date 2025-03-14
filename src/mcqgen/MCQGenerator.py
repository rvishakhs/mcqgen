# Import some necessary libraries
import os
import json 
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgen.utils import read_file, get_table_data
from src.mcqgen.logger import logging

# Importing necessary libraries from langchain 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI

# Load the environment variables from the .env file and store them in the KEY variable
load_dotenv()
KEY = os.getenv("OPEN_AI_API_KEY")

# Calling the OPENAI model with the API key
llm = ChatOpenAI(openai_api_key=KEY, model_name="gpt-3.5-turbo",temperature=0.7)

# Template
TEMPLATE = """
Text : {text}
You are an expert MCQ creator. You have to create a multiple choice questions based on the above given text.
create a quiz with {number} of multiple choice questions for {subject} students with {tone} difficulty level.
Make sure the questions are not repeated and check all the questions to be conforming text as well
Make sure to format the response like RESPONSE_JSON below and use it as a guide.
Ensure to make {number} of MCQs
### RESPONSE_JSON
{response_json} 
"""

# Input prompt template
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE
)

# LLM Chain for generating MCQs
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

# Template for the quiz evaluation prompt
TEMPLATE2 = """
You are an expert english grammar teacher and writer. Given a Multiple choice quiz for {subject} students.
You need to evalaute the complexity of the quiz and provide feedback on the quiz. use only max 50 words for complexity analysis.
if the quiz is not at par with the subject level, update the quiz questions which needs to be changed and change the tone such that it perfectly fits the students abilities 
Quiz_MCQs: {quiz}

check from an expert English writer of the above quiz and provide feedback on the quiz.
"""

# Input prompt template for quiz evaluation
review_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=TEMPLATE2
)

# LLM Chain for evaluating the MCQs
review_chain = LLMChain(llm=llm, prompt=review_prompt, output_key="review", verbose=True)

# Create an object of the SequentialChain class
generate_Quiz_Evaluate_Chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                               output_variables=["quiz","review"], verbose=True)