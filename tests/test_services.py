import pytest
from app import create_app
from pymongo import MongoClient
import certifi
import os

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    
    # Set up MongoDB connection for testing
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    db = client[os.getenv('DATABASE')]
    app.db = db
    
    with app.test_client() as testing_client:
        yield testing_client

    # Clean up
    client.close()

# def test_create_email(test_client):
#     email_data = {
#         "_id": "123",
#         "sender_info": {"name": "John Doe", 
#                         "organization": "Example Inc.",
#                         "email": "john@example.com"},
#         "subject": "Test Email 1",
#         "preview": "This is a test",
#         "date": "2024-08-16",
#         "content": "This is the content",
#         "attachments": [],
#         "flagged": False,
#         "embedding": [0.1, 0.2]
#     }
#     response = test_client.post('/emails', json=email_data)
#     assert response.status_code == 201
#     assert '_id' in response.json

# def test_get_email_by_id(test_client):
#     email_data = {
#         "_id": "124",
#         "sender_info": {"name": "Harry Alex", 
#                         "organization": "Example Inc.",
#                         "email": "Harry@example.com"},
#         "subject": "Test Email 2",
#         "preview": "This is a test",
#         "date": "2024-08-16",
#         "content": "This is the content",
#         "attachments": [],
#         "flagged": False,
#         "embedding": [0.1, 0.2]
#     }
#     response1 = test_client.post('/emails', json=email_data)
#     print(response1.json)
#     assert response1.status_code == 201
#     response = test_client.get('/emails/124')
#     assert response.status_code == 200
#     assert response.json['subject'] == 'Test Email 2'
#     test_client.delete('/emails/124')

# def test_get_all_emails(test_client):
#     email_data1 = {
#         "_id": "125",
#         "sender_info": {"name": "David", 
#                         "organization": "Example Inc.",
#                         "email": "David@example.com"},
#         "subject": "Test Email 3-1",
#         "preview": "This is a test",
#         "date": "2024-08-16",
#         "content": "This is the content",
#         "attachments": [],
#         "flagged": False,
#         "embedding": [0.1, 0.2]
#     }
#     email_data2 = {
#         "_id": "126",
#         "sender_info": {"name": "Yash", 
#                         "organization": "Example Inc.",
#                         "email": "Yash@example.com"},
#         "subject": "Test Email 3-2",
#         "preview": "This is another test",
#         "date": "2024-08-16",
#         "content": "This is another content",
#         "attachments": [],
#         "flagged": True,
#         "embedding": [0.3, 0.4]
#     }
#     test_client.post('/emails', json=email_data1)
#     test_client.post('/emails', json=email_data2)
#     response = test_client.get('/emails')
#     assert response.status_code == 200
#     assert len(response.json) == 4

def test_update_email(test_client):
    email_data = {
        "_id": "128",
        "sender_info": {"name": "Alice", 
                        "organization": "Example Inc.",
                        "email": "alice@example.com"},
        "subject": "Old Subject",
        "preview": "Old preview",
        "date": "2024-08-16",
        "content": "Old content",
        "attachments": [],
        "flagged": False,
        "embedding": [0.5, 0.6]
    }
    response1 = test_client.post('/emails', json=email_data)
    assert response1.status_code == 201
    update_data = {"flagged": True}
    response = test_client.put('/emails/128', json=update_data)
    print(response)
    # response = test_client.get('/emails/128')
    assert response.status_code == 200
    assert response.json['flagged'] == True
    test_client.delete('/emails/128')


# def test_delete_email(test_client):
#     response = test_client.delete('/emails/127')
#     assert response.status_code == 200
#     response = test_client.get('/emails/127')
#     assert response.status_code == 404
#     test_client.delete('/emails/126')
#     test_client.delete('/emails/125')
#     test_client.delete('/emails/124')
#     test_client.delete('/emails/123')
        