from flask import current_app as app
import google.generativeai as genai
import os

# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
table = os.getenv('TABLE')

def create_email(email_data):
    try:
        result = app.db[table].insert_one(email_data)
        return str(result.inserted_id)
    except Exception as e:
        app.logger.error(f"Error creating email: {e}")
        print(f"Error creating email: {e}")
        return None


def get_email_by_id(email_id):
    try:
        email = list(app.db[table].find({"_id": email_id}))
        if email:
            return email[0]
        else:
            return None
    except Exception as e:
        app.logger.error(f"Error getting email by id: {e}")
        print(f"Error getting email by id: {e}")
        return None


def get_all_emails():
    try:
        emails = list(app.db[table].find({}))
        return emails
    except Exception as e:
        app.logger.error(f"Error getting all emails: {e}")
        print(f"Error getting all emails: {e}")
        return []


def update_email(email_id, update_fields):
    try:
        result = app.db[table].update_one(
            {"_id": email_id}, 
            {"$set": update_fields},
            upsert=True
        )
        if result.modified_count > 0:
            return get_email_by_id(email_id)
        else:
            return None
    except Exception as e:
        app.logger.error(f"Error updating email: {e}")
        print(f"Error updating email: {e}")
        return None


def delete_email(email_id):
    try:
        result = app.db[table].delete_one({"_id": email_id})
        if result.deleted_count > 0:
            return True
        else:
            return False
    except Exception as e:
        app.logger.error(f"Error deleting email: {e}")
        print(f"Error deleting email: {e}")
        return False
