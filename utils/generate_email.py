import google.generativeai as genai
import os
import json
import random
from time import sleep
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
db = client[os.getenv('DATABASE')]

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


def generate_topic():
    topics = [
        "life",
        "love",
        "happiness",
        "success",
        "failure",
        "dreams",
        "goals",
        "motivation",
        "inspiration",
        "change",
        "time",
        "money",
        "power",
        "knowledge",
        "wisdom",
        "fear",
        "anger",
        "sadness",
        "joy",
        "peace",
        "beauty",
        "truth",
        "justice",
        "freedom",
        "equality",
        "existence",
        "consciousness",
        "reality",
        "perception",
        "illusion",
        "universe",
        "space",
        "time",
        "dimension",
        "infinity",
        "chaos",
        "order",
        "balance",
        "harmony",
        "discord",
        "mystery",
        "magic",
        "wonder",
        "awe",
        "intrigue",
        "technology",
        "science",
        "art",
        "music",
        "literature",
        "history",
        "philosophy",
        "religion",
        "politics",
        "economics",
        "health",
        "fitness",
        "nutrition",
        "environment",
        "nature",
        "travel",
        "food",
        "fashion",
        "sports",
        "games",
        "relationships",
        "family",
        "friendships",
        "marriage",
        "parenting",
        "artificial intelligence",
        "climate change",
        "social media",
        "cryptocurrency",
        "virtual reality",
        "mental health",
        "cybersecurity",
        "sustainable living",
        "remote work",
        "work-life balance",
    ]
    randomTopic = random.choice(topics)
    return randomTopic


def format_email(response_json, id: int):
    email = {
        "_id": id,
        "sender_info": {
            "name": response_json.get("sender_name"),
            "organization": response_json.get("organization_name"),
            "email": response_json.get("sender_email"),
        },
        "subject": response_json.get("subject"),
        "preview": None,
        "created_at": response_json.get("created_at_time"),
        "content": response_json.get("email_body"),
        "attachments": (
            response_json.get("attachment").split(" ")
            if response_json.get("attachment")
            else None
        ),
        "flagged": random.choice([True, False]),
        "embedding": None,
    }

    return email


instruction = (
    """
        Please generate an email on """
    + generate_topic()
    + """.
        Can be all kinds of email, for example, personal emails, team collaboration, etc. Be creative.
        Generate all types of emails equally. No grammar error is allowed. 
        Please don't use "example company" or "example name" in the email. Use a real company name and a real person name as needed. Also, don't use [ ] or < > as a placeholder in the email.
        Please generate email in JSON format, including information about sender_name, sender_email, organization_name (optional), subject, email_body, created_at_time (around the 2024 year), and attachments (optional, could be multiple, in a list of string format (split by space)).
        If the optional information section is empty, leave it null. Generate 7-15 emails at a time.
        """
)


def generate_emails():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"top_p": 0.9, "top_k": 100, "temperature": 1},
        system_instruction=instruction,
    )
    response = model.generate_content("Generate emails")
    # remove ```json``` from the response
    response_text = response.text
    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    # parse the response as json
    response_jsons = json.loads(response_text)
    return response_jsons

id = 19

while True:
    try:
        response_jsons = generate_emails()
    except Exception as e:
        print(e)
        continue
    if id > 1000:
        break
    for response_json in response_jsons:
        if id % 100 == 0:
            sleep(7)
        id += 1
        try:
            formatted_email = format_email(response_json, id)
            print(formatted_email)
            db["emails"].update_one({"_id": id}, {"$set": formatted_email})
        except Exception as e:
            print(e)
            pass
