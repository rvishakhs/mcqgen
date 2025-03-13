from setuptools import setup, find_packages


setup(
    name="mcqgenerator",
    version="0.1.0",
    packages=find_packages(),
    author="visakh",
    author_email="me@visakhsr.com",
    description="A simple MCQ generator",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
)

