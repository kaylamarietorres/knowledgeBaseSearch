from haystack_integrations.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack import Pipeline
from haystack.components.converters import SentenceTransformersDocumentEmbedder
from haystack.components.converters import TextFileToDocument
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter

document_store = ElasticsearchDocumentStore(hosts="http://localhost:9200")
converter = TextFileToDocument()
splitter = DocumentSplitter()
doc_embedder = SentenceTransformersDocumentEmbedder(model="sentence-transformers/multi-qa-mpnet-base-dot-v1")
writer = DocumentWriter(document_store)

indexing_pipeline = Pipeline()
indexing_pipeline.add_component("converter", converter)
indexing_pipeline.add_component("splitter", splitter)
indexing_pipeline.add_component("doc_embedder", doc_embedder)
indexing_pipeline.add_component("writer", writer)

indexing_pipeline.connect("converter", "splitter")
indexing_pipeline.connect("splitter", "doc_embedder")
indexing_pipeline.connect("doc_embedder", "writer")

indexing_pipeline.run({
    "converter": {"sources": ["filename.txt"]}
    })
