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
                'embedding': 1,
                'score': {
                    '$meta': 'searchScore'
                }
            }
        }
    ]

    results = db['emails'].aggregate(pipeline)

    results_list = []

    for result in results:
        results_list.append(result)
        # print("Result", result)

    # print("Type of result: ", type(results))
    # print("Emails matched", list(results))
    # print("Length of emails matched", len(list(results)))
    # print("Type of result in list: ", type(list(results)))

    return results_list
