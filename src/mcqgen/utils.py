import os
import PyPDF2
import json 
import traceback

# Function to read the file 

def read_file(file):
    """
    Read the file and return the text
    """
    if file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = " "
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception("Invalid file format, This model only supports .txt and .pdf files")
    
# Function to get the table data
def get_table_data(quiz):
    """
    Convert the quiz from string to dictable data 
    """
    try:
        quiz_dict = json.loads(quiz)
        quiz_table_data = []

        # Loop through the quiz dict and get the data
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ" : mcq, "Choices": options, "Correct": correct})
        return quiz_table_data
    

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False 
