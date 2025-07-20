from utils.model_loader import Modeloader

llm = Modeloader()
load_llm = llm.load_llm()
print(load_llm.invoke("hi").content)