from fastapi import FastAPI
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline

app = FastAPI()

# Initialize Elasticsearch document store
document_store = ElasticsearchDocumentStore(host="elasticsearch", port=9200, username="", password="", index="document")

# Initialize the reader (question-answering model)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

# Initialize the pipeline
pipeline = ExtractiveQAPipeline(reader, document_store)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/add-document/")
def add_document(content: str):
    document_store.write_documents([{"content": content}])
    return {"message": "Document added"}


@app.get("/search/")
def search(query: str):
    results = pipeline.run(query=query, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}})
    return results
