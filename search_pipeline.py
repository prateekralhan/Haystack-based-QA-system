from haystack.nodes import TfidfRetriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from haystack.document_stores import SQLDocumentStore
from pprint import pprint

document_store = SQLDocumentStore(url="sqlite:///qa.db")
retriever = TfidfRetriever(document_store=document_store)

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
reader.save('reader')

pipe = ExtractiveQAPipeline(reader, retriever)

sample_query = "Who is author of Wings of Fire ?"
params={"Retriever": {"top_k": 5}, # Top 5 relevant documents in document_store
        "Reader": {"top_k": 3} # Top 3 answers, searched in retrieved documents.
       }
prediction = pipe.run(query=sample_query, params=params)

pprint(prediction['answers'])
