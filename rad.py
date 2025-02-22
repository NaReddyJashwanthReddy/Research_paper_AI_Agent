import chromadb
from chromadb.config import Settings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import random

#sent_tran=SentenceTransformer('all-MiniLM-L6-v2')
st_emb=SentenceTransformerEmbeddingFunction(model_name='all-MiniLM-L6-v2')

client=chromadb.PersistentClient(path="./my_chroma_db")

collector=client.get_or_create_collection('my_collector',embedding_function=st_emb)

lil=['2501.12948v1.pdf',
     'NeurIPS-2020-denoising-diffusion-probabilistic-models-Paper.pdf',
     'NIPS-2014-generative-adversarial-nets-Paper.pdf',
     'NIPS-2017-attention-is-all-you-need-Paper.pdf']

def add_Data(lil,DATA=''):

    for i in lil:
        loader=PyPDFLoader(f'../{i}')
        load=loader.load()
        for datai in load:
            DATA+=datai.page_content

    text_split_par=DATA.split('\n\n')

    splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)

    list_of_data=[]

    for paragraphs in text_split_par:

        t1=splitter.split_text(paragraphs)

        list_of_data+=t1 


    for i,text in enumerate(list_of_data):
        collector.add(
            ids=str(i),
            documents=text
        )

if collector.count() > 0:
    print(f"Data already exists in the database ({collector.count()} documents). Skipping ingestion.")
else:
    add_Data(lil)

def retrive_data(query):
    num=random.randint(20,30)
    retrive=collector.query(
        query_texts=query,
        n_results=num
    )

    return retrive
