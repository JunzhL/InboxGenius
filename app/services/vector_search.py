from pymongo import MongoClient
import os
import certifi

client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
db = client[os.getenv('DATABASE')]

def find_emails(query_vec, limit=2):
    pipeline = [
        {
            '$vectorSearch': {
                'index': 'vectorIndex',
                'path': 'embedding',
                'queryVector': query_vec,
                'numCandidates': 10 * limit,
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
                'category': 1,
                'embedding': 1,
                'score': {
                    '$meta': 'vectorSearchScore'
                }
            }
        }
    ]

    results = db[os.getenv('TABLE')].aggregate(pipeline)

    results_list = []

    for result in results:
        results_list.append(result)
        print(result['score'])


    return results_list
