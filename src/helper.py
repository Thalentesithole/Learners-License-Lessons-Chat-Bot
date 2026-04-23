from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from typing import List
from langchain.schema import Document
from typing import List
from langchain.schema import Document

# Extract text from PDF files
def load_pdf_files(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)

    documents = loader.load()
    return documents

from typing import List
from langchain.schema import Document

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """ 
    Given a list of Document objects, return a new list of Docmuent objects
    containing only 'source' in metadata and the original page_content.
    """

    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs

#Split the documents into smaller chunks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
        length_function=len
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk


def download_embedding():
    """ 
    Download and return the HuggingFace embedding model.
    """

    model_name = "BAAI/bge-small-en-v1.5"
    embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
    )
    return embeddings

embedding = download_embedding()