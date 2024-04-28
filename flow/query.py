
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


def query_docs(query:str, k=4, score_threshold=0.6):

    # create the open-source embedding function
    embedding_function = ZhipuEmbedding(key=ZHIPUAI_API_KEY)

    # load it into Chroma
    db = Chroma(collection_name, embedding_function=embedding_function, persist_directory=persist_directory)

    # query it
    docs = db.similarity_search(query,k=k,score_threshold=score_threshold)

    # print results
    print(docs[0])
    return docs