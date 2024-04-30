
import os,sys 
from langchain_chroma import Chroma

from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.embedding_model import ZhipuEmbeddings

load_dotenv()

ZHIPUAI_API_KEY = os.environ["ZHIPUAI_API_KEY"] 
collection_name = "xiaohongshu"
persist_directory = "data/vector"


def query_docs(query:str, k=4, score_threshold=0.2):

    # create the open-source embedding function
    embedding_function = ZhipuEmbeddings(key=ZHIPUAI_API_KEY)

    # load it into Chroma
    db = Chroma(collection_name, embedding_function=embedding_function, persist_directory=persist_directory)

    # query it,with result, List[tuple(doc,score)]
    docs = db.similarity_search_with_relevance_scores(query,k=k,score_threshold=score_threshold)
    return docs

if __name__ == "__main__":
    query=""
    docs = query_docs("云养小动物")
    print(docs)