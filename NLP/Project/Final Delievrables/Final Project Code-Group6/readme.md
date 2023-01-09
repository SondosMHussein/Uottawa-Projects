# A propsed apprach for creating a custom emotion chatbot

In this notebook a custom chatbot was created that uses a locally trained emotion classifier created using emotions dataset from kaggle to pick the appropriate response according to the user emotion while talking to the chatbot.
------------
### **chatbot features**
- Uses states to mimic a human conversation with the user, States matching is based on regex using the provided sataes configurations.
- Invokes the user to talk by asking about entities recognized in the user messages.
- Responds to the user messages according the deteced emotion in the user messages.
- Responding to the user using a quote that is related the messages provided by the user.
------------
### **Datasets**
- [Emotions dataset for NLP](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp) available on kaggle.
- [Quotes dataset](https://www.kaggle.com/datasets/akmittal/quotes-dataset) available on kaggle.
- [Bot Responses dataset](./content/chatbot-Responses.csv) a small dataset that was created manully and contains multiple responses based on emotions.
------------
### **Libraries**
- **sklearn:** a free software machine learning library for the Python programming language.
- **tkinter:** a Python binding to the Tk GUI toolkit
- **Spacy:** an open-source software library for advanced natural language processing.
- **Numpy:** a library adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- **Pandas:** a software library written for the Python programming language for data manipulation and analysis.
- **nltk:** is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.
- **seaborn:** a library that uses Matplotlib underneath to plot graphs.
- **matplotlib:** a plotting library for the Python programming language.
- **gensim:** an open-source library for unsupervised topic modeling, document indexing, retrieval by similarity, and other natural language processing functionalities, using modern statistical machine learning.
- **wordcloud:** A little word cloud generator in Python.
------------
### **Development environment**
- This notebook was developed using Anaconda version 4.13.0 and jupyter notebook version 6.4.11 running on version 3.9.12 of python.
------------
### **Running the code**

- Install the required libraries.
- Run the code locally using anaconda or python, because tkinter library only supports running locally on PC not on cloud based notebooks environments e.g. colab.
------------
### **GUI Screenshots**

Sad emtion detection and chatbot response example<br><br>
![sad emotion detection](./demo_screenshot/sadness.png?raw=true "sad emotion detection")