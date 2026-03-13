from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda,RunnableSequence
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import json
load_dotenv()

#llm runnable task
model = ChatOpenRouter(
    # model="google/gemini-2.5-flash",
    model="google/gemma-3-12b-it",
    temperature=0.7,
)
parser = StrOutputParser()

tweet_prompt = PromptTemplate.from_template("Write a tweet on {topic} in 3 sentences")
linkedin_prompt = PromptTemplate.from_template("Write a LinkedIn post on {topic} 3 sentences")

tweet_chain = tweet_prompt | model | parser
linkedin_chain = linkedin_prompt | model | parser

final_chain = RunnableParallel({
    "tweet": tweet_chain,
    "linkedin": linkedin_chain,
    "tweet_length": tweet_chain | RunnableLambda(lambda x: len(x.split()))
})



final_chain.get_graph().print_ascii()

print(final_chain.invoke({"topic": "AI in telecom"}))


'''
output:

+--------------------------------------------+                  
               | Parallel<tweet,linkedin,tweet_length>Input |                  
               +--------------------------------------------+                  
                      ****            *            *****                       
                 *****                *                 ****                   
              ***                     *                     *****              
+----------------+                    *                          ***           
| PromptTemplate |                    *                            *           
+----------------+                    *                            *           
          *                           *                            *           
          *                           *                            *           
          *                           *                            *           
+----------------+           +----------------+           +----------------+   
| ChatOpenRouter |           | PromptTemplate |           | PromptTemplate |   
+----------------+           +----------------+           +----------------+   
          *                           *                            *           
          *                           *                            *           
          *                           *                            *           
+-----------------+          +----------------+           +----------------+   
| StrOutputParser |          | ChatOpenRouter |           | ChatOpenRouter |   
+-----------------+          +----------------+           +----------------+   
          *                           *                            *           
          *                           *                            *           
          *                           *                            *           
    +--------+              +-----------------+           +-----------------+  
    | Lambda |***           | StrOutputParser |           | StrOutputParser |  
    +--------+   *****      +-----------------+        ***+-----------------+  
                      ****            *            ****                        
                          *****       *       *****                            
                               ***    *    ***                                 
               +---------------------------------------------+                 
               | Parallel<tweet,linkedin,tweet_length>Output |                 
               +---------------------------------------------+                 
{'tweet': "AI is revolutionizing telecom! From predictive maintenance & network optimization to personalized customer experiences & fraud detection, it's boosting efficiency and driving innovation. Expect to see even more AI-powered solutions transforming the industry in the years to come. #AI #Telecom #Innovation #DigitalTransformation", 'linkedin': "Here's a LinkedIn post on AI in telecom, tailored for a professional audience:\n\n**Option 1 (Focus on Efficiency):**\n\nAI is rapidly transforming the telecom industry, driving unprecedented operational efficiency through automation and predictive maintenance. From network optimization to enhanced customer service chatbots, AI is helping providers reduce costs and improve performance. Let's discuss how AI can unlock even greater possibilities for telecom businesses! #AI #Telecom #DigitalTransformation #Innovation\n\n**Option 2 (Focus on Customer Experience):**\n\nTelecom companies are leveraging AI to personalize customer experiences and proactively address their needs. AI-powered analytics provide deeper insights into user behavior, enabling targeted offers and faster issue resolution.  It’s an exciting time to see how AI enhances connectivity and satisfaction! #AIinTelecom #CustomerExperience #Telecom #ArtificialIntelligence\n\n\n\n**To help me tailor it even further, could you tell me:**\n\n*   **What's the specific angle you want to emphasize?** (e.g., security, 5G, specific AI application)\n*   **Who is your target audience?** (e.g., telecom executives, engineers, general audience)", 'tweet_length': 43}
'''