import os 
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel,Agent,Runner,AsyncOpenAI
from agents.run import RunConfig

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("Key not find")

provider=AsyncOpenAI(
    api_key= api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)


config = RunConfig(
    model = model,
    model_provider=provider,
    tracing_disabled=True
)


agent1 = Agent(
    name = "assistant",
    instructions="you are a helpful assisstant",
    model = model
)

result = Runner.run_sync(agent1, "Tell me about Piaic", run_config=config)
print(result.final_output)