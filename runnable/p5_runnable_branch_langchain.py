from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv
import json
load_dotenv()
promp1 = PromptTemplate(
    template='Generate a tweet about {topic} in 3 sentences',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Summarize the following text {topic} in 3 sentences',
    input_variables=['topic']
)

model = ChatOpenRouter(
    model="google/gemma-3-12b-it",
    temperature=0.7,
)
parser = StrOutputParser()

sequential_chain = RunnableSequence(promp1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>30,RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

parallel_chain = RunnableParallel({
    'topic_original': sequential_chain,
    'topic_length_og': RunnableLambda(lambda x: len(x.split())),
    'modified_topic':branch_chain
})

final_chain = RunnableSequence(sequential_chain, branch_chain)

final_chain.get_graph().print_ascii()

result = final_chain.invoke({'topic':'the impact of AI on society'})

print(json.dumps(result,indent=4))


'''
                             +-------------+                           
                              | PromptInput |                           
                              +-------------+                           
                                      *                                 
                                      *                                 
                                      *                                 
                            +----------------+                          
                            | PromptTemplate |                          
                            +----------------+                          
                                      *                                 
                                      *                                 
                                      *                                 
                            +----------------+                          
                            | ChatOpenRouter |                          
                            +----------------+                          
                                      *                                 
                                      *                                 
                                      *                                 
                            +-----------------+                         
                            | StrOutputParser |                         
                            +-----------------+                         
                                      *                                 
                                      *                                 
                                      *                                 
                                +--------+                              
                                | Branch |                              
                                +--------+                              
                                      *                                 
                                      *                                 
                                      *                                 
      +--------------------------------------------------------------+  
      | Parallel<topic_original,topic_length_og,modified_topic>Input |  
      +--------------------------------------------------------------+  
                      ****            *           *****                 
                 *****                *                ****             
              ***                     *                    *****        
+----------------+                    *                         ***     
| PromptTemplate |                    *                           *     
+----------------+                    *                           *     
          *                           *                           *     
          *                           *                           *     
          *                           *                           *     
+----------------+                    *                           *     
| ChatOpenRouter |                    *                           *     
+----------------+                    *                           *     
          *                           *                           *     
          *                           *                           *     
          *                           *                           *     
+-----------------+             +--------+                  +--------+  
| StrOutputParser |             | Lambda |                 *| Branch |  
+-----------------+***          +--------+            ***** +--------+  
                      ****            *           ****                  
                          *****       *      *****                      
                               ***    *   ***                           
     +---------------------------------------------------------------+  
     | Parallel<topic_original,topic_length_og,modified_topic>Output |  
     +---------------------------------------------------------------+  
{
    "topic_original": "AI is rapidly reshaping society, offering incredible potential across industries! However, we must proactively tackle the ethical implications & biases that emerge with this powerful technology. Let's prioritize responsible & equitable AI development that benefits all of humanity. #AI #Ethics #ResponsibleAI #ArtificialIntelligence",
    "topic_length_og": 49,
    "modified_topic": "Artificial intelligence is rapidly changing society and holds great potential for progress. However, it's essential to carefully consider the ethical concerns and biases that can emerge from this technology. We must prioritize responsible and equitable development to ensure AI benefits everyone."
}

'''
