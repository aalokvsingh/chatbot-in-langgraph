from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv
import json
load_dotenv() 

#prompt runnable task
prompt1 = PromptTemplate(
    template='Generate a tweet about {topic} in 3 sentences',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a linkedin post about {topic} in 3 sentences',
    input_variables=['topic']
)

llm1 = ChatOpenRouter(
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

llm2 = ChatOpenRouter(
    model="google/gemini-2.5-flash",
    temperature=0.7,
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, llm1, parser),
    'linkedin_post': RunnableSequence(prompt2, llm2, parser)
})

result = parallel_chain.invoke({'topic':'the impact of AI on society'})

print(json.dumps(result, indent=2))
'''
output

{
  "tweet": "AI is rapidly transforming society, impacting everything from healthcare and education to jobs and entertainment. While offering incredible potential for progress and efficiency, it also raises crucial ethical questions about bias, privacy, and the future of work. Let's prioritize responsible development and ensure AI benefits everyone. #AI #ArtificialIntelligence #Society #FutureTech",
  "linkedin_post": "Here are a few options, choose the one you like best:\n\n**Option 1 (Focus on transformation):**\nAI is rapidly reshaping our world, bringing unprecedented advancements in healthcare, sustainability, and productivity. However, this transformation also demands critical conversations about ethics, job displacement, and equitable access. Let's engage in thoughtful dialogue to harness AI's power for a truly inclusive and prosperous future.\n\n**Option 2 (Focus on opportunity and responsibility):**\nThe impact of AI on society is undeniable, presenting immense opportunities for innovation and problem-solving across every sector. From personalized education to climate solutions, its potential is vast, but so is our responsibility to guide its development ethically. We must collectively ensure AI serves humanity's best interests, fostering progress while mitigating potential risks.\n\n**Option 3 (More direct and call to action):**\nAI's influence on society is profound, touching every aspect of our lives from how we work to how we interact. While it promises efficiency and groundbreaking discoveries, we must actively address its implications for privacy, bias, and the future of employment. What are your thoughts on navigating this powerful technological shift responsibly?"
}

'''