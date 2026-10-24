Server Generation Prompt:
----------------------------------------------------------------------------------

SYSTEM:
You are an expert python developer

CONTEXT:
I want to setup a simple webserver using FastAPI. It should run locally. 
I have function as below: 
def ask(query: str) -> str 
    <function body> 
    return {"answer": answer}


The function is in a file called rag_pipeline.py 
URL enpoint: 127.0.0.1:5000/ask 
Used for sending queries like: what are the symptoms of diabetes? 

TASK:
Give the python file for the FastAPI server

OUTPUT:
Python Code
Steps to run the code


UI Generation Prompt
----------------------------------------------------------------------------------

I want to creata UI application using Streamlit which has the following widgets

Title            : "Medical Assistant" (add appropriate icons | color: Brown)
Input            : Query text input
Response         : Print the response from the server

Connection details:

URL to connect   : http://127.0.0.1:5000/ask (GET request)
Response         : Dictionary

Example output:
{"answer":"Based on the provided context, the common symptoms of diabetes include:\n\n* Increased thirst\n* Frequent urination\n* Shortness of breath\n* Fatigue\n* Muscle weakness\n* Blurred vision\n* Weight loss"}

Other instructions:
- Keep  a bounding box for the input and output widgets with thin black boarder
- Use bright contrasting colors
- Give steps to run the application
- Refer the server.py for further details and finer adjustments