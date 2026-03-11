from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenRouter(
    # model="google/gemini-2.5-flash",
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

# template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']
# )

# prompt1 =template1.invoke({'topic':"the impact of AI on society"})

# result1 = model.invoke(prompt1)


# template2 = PromptTemplate(
#     template='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )
# prompt2 = template2.invoke({'text': result1.content})

# result2 = model.invoke(prompt2)

# print(result2.content)


template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model |parser | template2 | model | parser

print("\n\n Chain using string outpiut parser \n\n")
result = chain.invoke({'topic':"the impact of AI on society"})
print(result)