from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import json
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenRouter(
    # model="google/gemini-2.5-flash",
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

parser = JsonOutputParser()


template = PromptTemplate(
    template='Give me 1 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

resilt = chain.invoke({'topic':'the impact of AI on society'})

print(json.dumps(resilt,sort_keys=True, indent=4))
