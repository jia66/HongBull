from langchain_core.tools import tool
from flow.lcel import *


@tool
def genContentTool(product:str, common_key:str ,hot_key:str) -> str:
    """生成小红书种草文案"""

    return genContentLCEL(product,common_key,hot_key)
