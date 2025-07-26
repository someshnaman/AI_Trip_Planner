import os
from typing import List, Callable
from utils.currency_converter import CurrencyConverter
from langchain.tools import tool
from dotenv import load_dotenv

class CurrencyConverterTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('EXCHANGE_RATE_API_KEY')
        if not self.api_key:
            raise ValueError("Missing required environment variable: EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()    
        
    def _setup_tools(self) -> List[Callable]:
        """Setup all tools for the currency converter tool"""
        @tool
        def convert_currency(amount:float, from_currency:str, to_currency:str):
            """Convert amount from one currency to another"""
            return self.currency_service.convert(amount, from_currency, to_currency)
        
        return [convert_currency]
