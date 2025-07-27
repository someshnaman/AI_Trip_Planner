from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from euriai.langchain import EuriaiChatModel
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
import os

load_dotenv()

EURI_API = os.getenv('EURI_API_KEY')


class AgentState(TypedDict):
    messages: List[HumanMessage]


llm = EuriaiChatModel(
    api_key=EURI_API,
    model="gpt-4.1-nano",
    temperature=0.7,
    max_tokens=300
)


def process(state: AgentState) -> AgentState:
    response = llm.invoke(state['messages'])
    print(f"\nAI {response.content}")
    return state


graph = StateGraph(AgentState)
graph.add_node('process', process)
graph.add_edge(START, 'process')
graph.add_edge('process', END)

agent = graph.compile()

user_input = input("Enter:")
agent.invoke({'messages': [HumanMessage(content=user_input)]})
