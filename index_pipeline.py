from haystack.nodes import TextConverter
from haystack.nodes import PreProcessor
from haystack.document_stores import SQLDocumentStore
import os

converter = TextConverter(remove_numeric_tables=True, valid_languages=["en"])
document_store = SQLDocumentStore(url="sqlite:///qa.db")

preprocessor = PreProcessor(clean_empty_lines=True,
                            clean_whitespace=True,
                            clean_header_footer=False,
                            split_by="word",
                            split_length=100,
                            split_respect_sentence_boundary=True
                           )


for filename in os.listdir("txt_files/"):
    doc_txt = converter.convert(file_path=os.path.abspath(os.path.join("txt_files/", filename)), meta=None)[0]
    docs = preprocessor.process([doc_txt])
    document_store.write_documents(docs)
