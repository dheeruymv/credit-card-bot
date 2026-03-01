import chromadb
from chromadb.config import Settings
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter


DATA_PATH = ".\..\data\hdfc"

def _read_data():
    return Path(DATA_PATH).read_text()

def _perform_chunking(data_to_chunk):
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=5
    )
    chunks = splitter.split_text(data_to_chunk)
    return chunks

class ChromaDB:

    def __init__(self, collection_name, metadata, chunks):
        self._collection_name = collection_name
        self._metadata = metadata
        self._chunks = chunks


    def generate_embeddings(self):
        client = self.get_client()
        self.collection = client.create_collection(name=self._collection_name)
        self.collection.add(documents=self._chunks, 
                            metadatas=[{"source": "hdfc"} for _ in self._chunks], 
                            ids=[f"id_{i}" for i in range(len(self._chunks))])


    def get_client(self):
        return chromadb.PersistentClient(path="./creditcard_db")
        #chromadb.Client(Settings(persistent_directory="./creditcard_db"))


    def query_results(self, query_text):
        return self.collection.query(query_texts=query_text, n_results=2 , include=["embeddings", "documents", "metadatas"])


def main():
    # First we will do chunking
    # Then Embedding
    cc_data = _read_data()
    chunks = _perform_chunking(cc_data)
    chromadb_obj = ChromaDB("HDFC_Credit_Card", [{"source":"internet"}], chunks)
    chromadb_obj.generate_embeddings()
    print(f"Embeddings are : {chromadb_obj.query_results('Can I apply for Credit Card?')}")


if __name__ == '__main__':
    main()