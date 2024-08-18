import random
import google.generativeai as genai
import os
import json
import random
from app.services.email_service import update_email
from app.services.generate_preview import get_preview
from app.services.embedding_service import get_text_embedding

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

    name = response_json.get("sender_name")
    organization = response_json.get("organization_name")
    email = response_json.get("sender_email")

    subject = response_json.get("subject")
    content = response_json.get("email_body")
    created_at = response_json.get("created_at_time")
    attachments = [
        response_json.get("attachment").split(" ")
        if response_json.get("attachment")
        else None
    ]

    preview = get_preview(
        name, 
        organization, 
        email, 
        subject, 
        content, 
        created_at, 
        attachments
    )

    preview = preview.text

    embedding = get_text_embedding(preview)

    embedding = embedding["embedding"]

    email = {
        "_id": str(id),
        "sender_info": {
            "name": name,
            "organization": organization,
            "email": email,
        },
        "subject": subject,
        "preview": preview,
        "created_at": created_at,
        "content": content,
        "attachments": attachments,
        "flagged": random.choice([True, False]),
        "embedding": embedding,
    }

    # print("Email", email)

    return email

def classify_email(formatted_email):
    instruction = (
        """
            Please classify the email based on the following categories: Family, Social, Friends, Work.
            If the email does not fit any of the categories, please classify it as other. Answer in a JSON format.
        """
    )
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"top_p": 0.5, "top_k": 50, "temperature": 0.6},
        system_instruction=instruction,
    )
    
    response = model.generate_content(formatted_email.get("preview"))
    response_text = response.text
    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    category = json.loads(response_text).get("category")
    
    formatted_email["category"] = category
    
    return formatted_email

def generate_email():
    email_id = random.randint(1, 1000)

    instruction = (
        """
            Please generate an email on """
        + generate_topic()
        + """.
            Can be all kinds of email, for example, personal emails, team collaboration, etc. Be creative.
            Generate all types of emails equally. No grammar error is allowed. Date should be random around the 2024 year.
            Do not inlucde emoji.
            Please don't use "example company" or "example name" in the email. Use a real company name and a real person name as needed. Also, don't use [ ] or < > as a placeholder in the email.
            Please generate a random replacement for any placeholder in the email, such as "Dear [name]" or "Hello <name>", and project names as well. 
            Please generate email in JSON format, including information about sender_name, sender_email, organization_name (optional), subject, email_body, created_at_time (around the 2024 year), and attachments (optional, could be multiple, in a list of string format (split by space)).
            If the optional information section is empty, leave it null. Generate 1 emails at a time.
            """
    )

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"top_p": 0.9, "top_k": 100, "temperature": 1},
        system_instruction=instruction,
    )
    response = model.generate_content("Generate an email.")
    # remove ```json``` from the response
    response_text = response.text
    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    # parse the response as json
    response_json = json.loads(response_text)
    formatted_email = format_email(response_json, email_id)
    # update_email(email_id, formatted_email)

    return formatted_email
