import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from euriai.langchain import EuriaiChatModel

load_dotenv()


class ConfigLoader:
    def __init__(self):
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]


class Modeloader(BaseModel):
    model_provider: str = "EURI"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load & Return the LLM Model
        """
        print("LLM Loading")
        print(f"Loading model from provider {self.model_provider}")
        if self.model_provider == 'EURI':
            print("Loading LLM from EURI....... ")
            euri_api_key = os.getenv("EURI_API_KEY")
            model_name = self.config["llm"]['EURI']['model_name']
            llm = EuriaiChatModel(api_key=euri_api_key,
                                  model=model_name,
                                  temperature=0.7,
                                  max_tokens=3000)
            return llm


if __name__ == "__main__":
    llm = Modeloader()
    load_llm = llm.load_llm()
    print(load_llm.invoke("hi").content)
