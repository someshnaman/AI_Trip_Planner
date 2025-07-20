from euriai.langchain import EuriaiChatModel
from langchain_core.messages import SystemMessage, HumanMessage

chat = EuriaiChatModel(
    api_key="euri-bc2ae16e7d40c167df6c59920835de0cfaecaf0ba6afe9a88cb64f3b5d13bf9d",
    model="gpt-4.1-nano",
    max_tokens=500
)

messages = [
    SystemMessage(content="You are an 5th Standard Person."),
    HumanMessage(content="Tell me a Joke?")
]
response = chat.invoke(messages)
print(chat.invoke(response.content))