from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

import json
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenRouter(
    # model="google/gemini-2.5-flash",
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

schema = [
    ResponseSchema(name="fact_1.1", description="a fact1 about the topic"),
    ResponseSchema(name="fact_2", description="a fact2 about the topic"),
    ResponseSchema(name="fact_3", description="a fact3 about the topic"),
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser   

result = chain.invoke({'topic':'the impact of AI on society'})  
print(json.dumps(result,sort_keys=True, indent=4))

