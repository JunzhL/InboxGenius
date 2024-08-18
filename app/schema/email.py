email_schema = {
    "_id": str,
    "sender_info": {
        "name": str,
        "organization": str,
        "email": str
    },
    "subject": str,
    "preview": str,
    "created_at": str,
    "content": str,
    "attachments": [str],
    "flagged": bool,
    "embedding": [float],
    "category": str
}
