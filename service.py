from flow.lcel import *
from flow.agent import *
from flow.graph import *

def genContent(product,common_key,hot_key):
    #result = genContentLCEL(product,common_key,hot_key)
    #result = genContentAgent(product,common_key,hot_key)
    result = genContentMessageGraph(product,common_key,hot_key)
    #result = genContentStateGraph(product,common_key,hot_key)
    print(result)
    return result