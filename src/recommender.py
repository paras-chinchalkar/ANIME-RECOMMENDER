from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt
from dotenv import load_dotenv
import os

load_dotenv()

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()

        # ✅ Corrected call — use RetrievalQA instead of retrieval_qa
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever
        )

    def get_recommendation(self, query: str):
        result = self.qa_chain({"query": query})
        return result["result"]
