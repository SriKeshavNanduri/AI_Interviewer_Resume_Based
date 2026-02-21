from logging import warning
from pydoc import text
import tiktoken 
from text_extracter import text_extracter
from langchain_openai import AzureOpenAIEmbeddings 
from langchain_text_splitters import RecursiveCharacterTextSplitter  
import os 
from langchain_community.vectorstores import AzureSearch 

import warnings 
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv() 

# def chunk_text(text, chunk_size=250, overlap = 25): 
#     encoding = tiktoken.get_encoding("cl100k_base")
#     tokens = encoding.encode(text)
#     chunks = []
#     start = 0
#     while start < len(tokens):
#         end = start + chunk_size
#         chunk_tokens = tokens[start:end]
#         chunk_text = encoding.decode(chunk_tokens)
#         chunks.append(chunk_text)

#         start += chunk_size - overlap
    
#     return chunks 



def create_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=150,chunk_overlap=15)
    chunks = text_splitter.split_text(text)
    return chunks


def text3_embeddings(chunks): 
    embeddings_model = AzureOpenAIEmbeddings(
    azure_deployment="text-embedding-3-small",  # Use deployment name here
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    model="text-embedding-3-small" ) 
    vector = embeddings_model.embed_query(chunks)
    return vector 

chunks = create_chunks(text = text_extracter('Resume_Sandeep_latest_GL.pdf')) 
print("chunks ",len(chunks))
print("chunks type",type(chunks))

# text3_embeddings(chunks =chunks[0]) 
# print(len(text3_embeddings))

