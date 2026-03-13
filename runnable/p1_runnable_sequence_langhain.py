from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

from dotenv import load_dotenv
import json
load_dotenv()

#prompt runnable task
prompt1 = PromptTemplate(
    template='Give me 3 facts about {topic}',
    input_variables=['topic']
)

#llm runnable task
model = ChatOpenRouter(
    # model="google/gemini-2.5-flash",
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

#parser runnable task
parser = StrOutputParser()


prompt2 = PromptTemplate(
    template='What is the summary of the following facts? \n {facts}',
    input_variables=['facts']
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model,parser)

print(chain.invoke({'topic':'the impact of AI on society'}))






