import os
from langchain_openai import ChatOpenAI
from model.ChatZhipuAI import *


def getLLM(model_name):
    if model_name == "glm-4":
        ZHIPUAI_API_KEY = os.environ["ZHIPUAI_API_KEY"]
        llm = ChatZhipuAI(
            temperature=0.01,
            api_key=ZHIPUAI_API_KEY,
            model_name="glm-4",
        )
    elif model_name == "gpt-4":
        llm = ChatOpenAI(model="gpt-4")

    return llm


