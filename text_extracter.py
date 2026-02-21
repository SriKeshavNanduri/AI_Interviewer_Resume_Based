from pydoc import text
from connect_blob import connect_blob
from pypdf import PdfReader
from io import BytesIO
import os 
from dotenv import load_dotenv
load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")
    
    
def text_extracter(blob_name) : 
    resume_text = " "
    blob_client = connect_blob(blob_name=blob_name, connection_string=connection_string, container_name= container_name)
    
    pdf_bytes = blob_client.download_blob().readall()
    pdf_stream = BytesIO(pdf_bytes)
    reader = PdfReader(pdf_stream)

    for page in reader.pages:
        text=page.extract_text() 
        if text : 
            resume_text+= text 
    return resume_text 

if __name__ == '__main__' : 
    resume_text = text_extracter('Resume_Sandeep_latest_GL.pdf')
    print(resume_text)