from model.LLMHub import *
from prompt.PromptHub import *
from langchain_core.output_parsers import StrOutputParser

def genContentLCEL(product,common_key,hot_key):
    llm = getLLM('glm-4')
    #llm = getLLM('gpt-4')
    prompt_template = getPrompt("gencontent-zhongcao-1.0")
    output_parser = StrOutputParser()
    prompt_value = prompt_template.invoke({"product": product, "common_key": common_key, "hot_key": hot_key})
    #print(prompt_value)
    chain = prompt_template | llm | output_parser
    out_text = chain.invoke({"product": product, "common_key": common_key, "hot_key": hot_key})
    return out_text

