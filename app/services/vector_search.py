from pymongo import MongoClient
import os
import certifi

client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
db = client[os.getenv('DATABASE')]

def find_emails(query_vec, limit=1):
    pipeline = [
        {
            '$vectorSearch': {
                'index': 'vector_index',
                'path': 'embedding',
                'queryVector': query_vec,
                'limit': limit
            }
        }, {
            '$project': {
                '_id': 1,
                'sender_info': 1,
                'subject': 1,
                'preview': 1,
                'created_at': 1,
                'content': 1,
                'attachments': 1,
                'flagged': 1,
                'embedding': 1,
                'score': {
                    '$meta': 'searchScore'
                }
            }
        }
    ]

    results = db.aggregate(pipeline)

    print(f"Found {results.count()} emails")
    print(list(results))

    return list(results)
