Langchain Runnable
1. Runnable Category
    Task Specific Runnable e.g: llm, prompttemplate, retriever, parser
    Primitive Runnamble e.g: runnableparaller, runnableBranch, sequenticalrullable There runnable are used to orchestrate task specific runnable to create complex workflow in langchain.
2. RunnableSequence
    R1(prompt) -> R2(llm)->R3(parser)
3. RunnableParallel:
RunnableParallel is a runnable primitive that allow multiple runnable to run in parallel. Each runnable recevice same input and process it independently, producing a dictionary of outputs.
Prompt--llm1->parser
      --llm2->parser
4. RunnablePassthrough
It is a special runnable primitive that simply returns the input as output without modifying it.
5. RunnableLambda
    This is a primitive runnable that allow any python function to run with in pipeline.
6. RunnableBranch:
It is a primitive runnable that allow to create a condition chain. it is if else statement in langchain
7. LCEL
