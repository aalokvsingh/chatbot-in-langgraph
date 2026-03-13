from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
import json
load_dotenv()   

promp1 = PromptTemplate(
    template='Generate a tweet about {topic} in 3 sentences',
    input_variables=['topic']
)
model = ChatOpenRouter(
    model="google/gemma-3-12b-it",
    temperature=0.7,
)
parser = StrOutputParser()

sequential_chain = RunnableSequence(promp1, model, parser)

# print(sequential_chain.invoke({'topic':'the impact of AI on society'}))

parallel_chain = RunnableParallel({
    'tweet': RunnablePassthrough(),
    'count_word': RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(sequential_chain, parallel_chain)    

result = final_chain.invoke({'topic':'the impact of AI on society'}) 

print(result)

'''
ootput:

{'tweet': "AI is rapidly transforming society, impacting everything from healthcare and education to jobs and creative industries. While offering incredible potential for progress and efficiency, we must proactively address ethical concerns & potential biases. Let's ensure AI benefits all of humanity and shapes a future we want to live in. #AI #ArtificialIntelligence #FutureofWork #Ethics",
'count_word': 53}


'''