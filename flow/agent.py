from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, create_structured_chat_agent
from langchain_core.tools import tool
from model.LLMHub import *
from flow.lcel import *
from tool.tools import *

def genContentAgent(product,common_key,hot_key):
    llm = getLLM('glm-4')

    #prompt = hub.pull("hwchase17/structured-chat-agent")
    #agent = create_structured_chat_agent(llm, tools, prompt)

    prompt = hub.pull("hwchase17/openai-tools-agent")
    print(prompt)
    tools = [genContentTool]
    agent = create_openai_tools_agent(llm, tools, prompt)
  

    agent_executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True, verbose=True)


    result = agent_executor.invoke(
        {
            "input": f"生成小红书种草文案，product={product}，common_key={common_key}, hot_key={hot_key}"

        }
    )

    return result['output']
