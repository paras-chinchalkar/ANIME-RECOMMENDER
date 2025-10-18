import sys
import os

# Add the project root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, os.path.dirname(project_root))  # Add parent of project root
sys.path.insert(0, project_root)  # Add project root

from config.config import GROQ_API_KEY, MODEL_NAME
from pipeline.anime_pipeline import AnimeRecommendationPipeline
import streamlit as st

st.set_page_config(page_title="Anime Recommender", layout='wide')

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline(csv_path="data/updated_anime.csv")

pipeline = init_pipeline()

st.title("🎥 Anime Recommender System")

query = st.text_input("Enter your anime preference (e.g., thriller, romance, action):")

if query:
    with st.spinner("Fetching recommendation for you..."):
        try:
            response = pipeline.recommend(query)
            st.markdown("### ✅ Recommendations:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
