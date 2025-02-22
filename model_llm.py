from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
import os


load_dotenv()

API_KEY=os.getenv('GROQ_API')

model=ChatGroq(
    model='deepseek-r1-distill-llama-70b',
    api_key=API_KEY,
    temperature=0.7
)

def get_responce(query,retriver):

    prompt=PromptTemplate(
        input_variables=['query','retriver'],
        template="""
                ## You are an helpfull assistant.

            # Instructions: 
                -> we are designing a RAG model based on various research like Attention is all you need,DDPM,GAN and Deepseek r1.
                -> Don't Hallusinate while generating.
                -> Generate the only what required.
                -> If some of the retrived Text is not useful for query then Don't include it for generation.
                -> Requires High quality text generation.

            retrived data : {retriver}
            
            User : {query}

            ## NO PREAMBLE.
"""
    )

    chain=LLMChain(llm=model,prompt=prompt)

    inputs={
        'query':query,
        'retriver':retriver
    }

    gen=chain.run(inputs)

    reasoning,generated=gen.split('</think>')[0],gen.split('</think>')[1]

    return reasoning,generated 