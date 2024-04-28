

import os 
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from model.embedding_model import ZhipuEmbedding
from langchain_text_splitters import CharacterTextSplitter
from python_dotenv import load_dotenv
load_dotenv()

ZHIPUAI_API_KEY = os.environ("ZHIPUAI_API_KEY") 
collection_name = "xiaohongshu"
persist_directory = "data/vector"

# load the document and split it into chunks
loader = TextLoader("data/docs/example.txt")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the embedding function
embedding_function = ZhipuEmbedding(key=ZHIPUAI_API_KEY)

# load it into Chroma
db = Chroma(collection_name, embedding_function=embedding_function, persist_directory=persist_directory)
db.add_documents(docs)
print("save to db done")
