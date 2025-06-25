from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

my_key = config("GEMINI_API_KEY")
print(my_key)

client = AsyncOpenAI(api_key=my_key, 
base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)
