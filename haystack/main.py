from fastapi import FastAPI
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import DensePassageRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from haystack.utils import launch_es

app = FastAPI()

# Start Elasticsearch
launch_es()

# Initialize the DocumentStore
document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")

# Initialize Retriever and Reader
retriever = DensePassageRetriever(document_store=document_store)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

# Create the Pipeline
pipeline = ExtractiveQAPipeline(reader, retriever)

@app.post("/search")
async def search(query: str):
    prediction = pipeline.run(query=query, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}})
    return prediction
