

import os, sys 
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
from model.embedding_model import ZhipuEmbeddings 



load_dotenv()

ZHIPUAI_API_KEY = os.environ["ZHIPUAI_API_KEY"] 
collection_name = "xiaohongshu"
persist_directory = "data/vector"

def load_documents(file_path):

    # load the document and split it into chunks
    if os.path.exists(file_path):
        print("file exist")
    else:
        print("file not exist")
        return
    loader = TextLoader(file_path,autodetect_encoding=True)
    documents = loader.load()

    # split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # create the embedding function
    embedding_function = ZhipuEmbeddings(key=ZHIPUAI_API_KEY)

    # load it into Chroma
    db = Chroma(collection_name, embedding_function=embedding_function, persist_directory=persist_directory)
    db.add_documents(docs)
    print("save to db done")

if __name__ == "__main__":
    file_path = "data/docs/example.txt"
    load_documents(file_path)
