import json
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import END, MessageGraph,StateGraph
from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain.tools.render import format_tool_to_openai_function
from model.LLMHub import *
from promt import *
from tool.tools import *
from langgraph.prebuilt import ToolInvocation,ToolExecutor
from langchain_core.messages import FunctionMessage
from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

"""
by:霍炜佳 2024.04.26
生成文案内容
使用StateGraph
使用ToolExecutor
"""
def genContentStateGraph(product,common_key,hot_key):

    model = getLLM('glm-4')

    tools = [genContentTool]
    openai_tools = [convert_to_openai_tool(t) for t in tools]
    model_with_tools = model.bind(tools=openai_tools)
    tool_executor = ToolExecutor(tools)

    def invoke_model(state):
        messages = state['messages']
        response = model_with_tools.invoke(messages)
        return {"messages": [response]}

    def invoke_tool(state):
        messages = state['messages']
        last_message = messages[-1]

        tool_calls = last_message.additional_kwargs.get("tool_calls", [])

        for tool_call in tool_calls:
            if tool_call.get("function").get("name") == "genContentTool":
                action = ToolInvocation(
                    tool=tool_call.get("function").get("name"),
                    tool_input=json.loads(tool_call.get("function").get("arguments")),
                )

                response = tool_executor.invoke(action)

                tool_message = ToolMessage(
                    tool_call_id=tool_call.get("id"),
                    content=response
                )
                return {"messages": [tool_message]}


        return {"messages": []}

    def router(state):
        messages = state['messages']
        last_message = messages[-1]

        tool_calls = last_message.additional_kwargs.get("tool_calls", [])

        for tool_call in tool_calls:
            if tool_call.get("function").get("name") == "genContentTool":
                return "genContentTool"

        return "end"

    graph = StateGraph(AgentState)

    graph.add_node("model", invoke_model)

    graph.add_node("tool", invoke_tool)

    graph.add_conditional_edges("model", router, {
        "genContentTool": "tool",
        "end": END,
    })

    graph.add_edge("tool", END)

    graph.set_entry_point("model")

    runnable = graph.compile()

    output_parser = StrOutputParser()
    inputs = {"messages": [HumanMessage(content=f"生成小红书种草文案，product={product}，common_key={common_key}, hot_key={hot_key}")]}
    result = runnable.invoke(inputs)
    #print(result['messages'])
    return output_parser.invoke(result['messages'][-1])


"""
by:霍炜佳 2024.04.26
生成文案内容
使用MessageGraph方式
"""
def genContentMessageGraph(product,common_key,hot_key):

    model = getLLM('glm-4')
    tools = [genContentTool]
    openai_tools = [convert_to_openai_tool(t) for t in tools]
    model_with_tools = model.bind(tools=openai_tools)
   

    def invoke_model(state: List[BaseMessage]):
        return model_with_tools.invoke(state)
  

    def invoke_tool(state: List[BaseMessage]):
        tool_calls = state[-1].additional_kwargs.get("tool_calls", [])

        for tool_call in tool_calls:
            if tool_call.get("function").get("name") == "genContentTool":

                res = genContentTool.invoke(
                    json.loads(tool_call.get("function").get("arguments"))
                )

                return ToolMessage(
                    tool_call_id=tool_call.get("id"),
                    content=res
                )
            
        return None
    
    def router(state: List[BaseMessage]):
        tool_calls = state[-1].additional_kwargs.get("tool_calls", [])

        for tool_call in tool_calls:
            if tool_call.get("function").get("name") == "genContentTool":
                return "genContentTool"

        return "end"
    
    graph = MessageGraph()

    graph.add_node("model", invoke_model)

    graph.add_node("tool", invoke_tool)
    
    graph.add_conditional_edges("model", router, {
        "genContentTool": "tool",
        "end": END,
    })

    graph.add_edge("tool", END)

    graph.set_entry_point("model")

    runnable = graph.compile()

    output_parser = StrOutputParser()
    result = runnable.invoke(HumanMessage(f"生成小红书种草文案，product={product}，common_key={common_key}, hot_key={hot_key}"))
    
    return output_parser.invoke(result[-1])
