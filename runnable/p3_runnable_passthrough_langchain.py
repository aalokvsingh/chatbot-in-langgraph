from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnablePassthrough,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import json
load_dotenv()   

#prompt runnable task
prompt1 = PromptTemplate(
    template='Give me 3 facts about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='What is the summary of the following facts in 2 sentences? \n {summary}',
    input_variables=['summary']
)

#llm runnable task
model = ChatOpenRouter(
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

parser = StrOutputParser()

sequential_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'topic': RunnablePassthrough(),
    'summary': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(sequential_chain, parallel_chain)

result = final_chain.invoke({'topic':'the impact of AI on society'})

print(json.dumps(result, indent=2))

'''
output

{
  "topic": "Okay, here are 3 facts about the impact of AI on society, covering different angles:\n\n1. **AI is reshaping the job market, both creating and displacing roles:** While AI is often feared as a job-killer, the reality is more nuanced.  AI is automating some tasks currently done by humans (leading to potential job displacement in areas like data entry and customer service), *but* it's also creating new jobs in fields like AI development, data science, AI ethics, and roles focused on managing and maintaining AI systems.  The net effect on employment is still being studied and debated, but significant workforce shifts are undeniable.\n2. **AI is amplifying existing biases:** AI systems learn from the data they are trained on. If that data reflects societal biases (related to gender, race, socioeconomic status, etc.), the AI will likely perpetuate and even amplify those biases in its outputs \u2013 affecting things like loan applications, hiring decisions, and even criminal justice. This is a major ethical concern and area of active research.\n3. **AI is transforming healthcare, leading to improved diagnostics and treatment:** AI is being used to analyze medical images (like X-rays and MRIs) to detect diseases earlier and with greater accuracy, personalize treatment plans based on individual patient data, and accelerate drug discovery. This has the potential to significantly improve patient outcomes and reduce healthcare costs.\n\n\n\nHopefully, those give you a good overview of some key impacts!",
  "summary": "AI is significantly impacting society by reshaping the job market, creating new opportunities while also potentially displacing existing roles. Furthermore, while AI offers transformative advancements in areas like healthcare through improved diagnostics, it also presents ethical challenges due to its potential to amplify societal biases."
}

'''

