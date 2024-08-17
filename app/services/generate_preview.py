import google.generativeai as genai
import os 

genai.configure(os.getenv('API_KEY'))

def get_preview(name, organization, email, subject, content, created_at, attachments):

    instruction = """
        Please generate a summary of the email below, please keep key information, should be around 100-150 characters.
        For Attachments, please analyze the purpose of the attachments by looking at the file names and summarize the purpose of the attachments.
        Sender: {name} ({organization})
        Sender_Email: {email}
        Subject: {subject}
        Date: {created_at}
        Email_Body: {content}
        Attachments: {attachments}
        The output should be string.
    """

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "top_p": 0.4,
            "top_k": 40,
            "temperature": 0.7
        },
        system_instruction=instruction
        )
    response = model.generate_content("Generate the summary please.")
    return response
