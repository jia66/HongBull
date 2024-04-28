

from zhipuai import ZhipuAI
from langchain_core.embeddings.embeddings import Embeddings


class ZhipuEmbeddings(Embeddings):
    def __init__(self, key, model_name="embedding-2", **kwargs):
        self.client = ZhipuAI(api_key=key)
        self.model_name = model_name

    def embed_documents(self, texts: list, batch_size=32):
        """embed search documents
        texts: list of Documents
        """
        arr = []
        # tks_num = 0
        for txt in texts:
            res = self.client.embeddings.create(input=txt,
                                            model=self.model_name)
            arr.append(res.data[0].embedding)
            # tks_num += res.usage.total_tokens
        return arr

    def embed_query(self, text):
        res = self.client.embeddings.create(input=text,
                                            model=self.model_name)
        # res.usage.total_tokens
        return res.data[0].embedding 
