from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv
import json
load_dotenv()

model = ChatOpenRouter(
    # model="google/gemini-2.5-flash",
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

class Fact(BaseModel):
    fact_1: str = Field(description="a fact1 about the topic")
    fact_2: str = Field(description="a fact2 about the topic")
    fact_3: str = Field(description="a fact3 about the topic")

parser = PydanticOutputParser(pydantic_object=Fact)

template = PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser  

result = chain.invoke({'topic':'the impact of AI on society'})
print(json.dumps(result.dict(),sort_keys=True, indent=4))
