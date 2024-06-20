from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search")
def search(query: str):
    # Integrate with Haystack and Elasticsearch here
    return {"query": query}
