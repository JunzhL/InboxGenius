import google.generativeai as genai
import os 

genai.configure(api_key=os.getenv('API_KEY'))

def get_text_embedding(text, output_dim=256, model_name="models/text-embedding-004"):

    try:
        embedding = genai.embed_content(
            model=model_name,
            content=text,
            output_dimensionality=output_dim
        )
        return embedding
    except Exception as e:
        print(f"Error getting text embedding: {e}")
        return None
    

print(get_text_embedding("Hello, how are you?"))

