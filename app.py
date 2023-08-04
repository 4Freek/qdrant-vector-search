from fastapi import FastAPI
import numpy as np
from qdrant_client import QdrantClient

from qdrant import create_tokenizer, search

# The file where NeuralSearcher is stored
# from neural_searcher import NeuralSearcher

app = FastAPI()

# Create a neural searcher instance
# neural_searcher = NeuralSearcher(collection_name='startups')

@app.get("/api/search")
def search_startup(q: str):
    tokenizer = create_tokenizer()
    vectors = np.array(tokenizer.encode(q)).tolist()
    metadata = search(vectors, collection_name='image384', filters={}, options={})
    return {
        "result": metadata
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)