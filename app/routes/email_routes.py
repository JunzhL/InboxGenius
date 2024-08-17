from flask import Blueprint, request, jsonify, Flask
from app.services.email_service import (
    create_email,
    get_email_by_id,
    get_all_emails,
    update_email,
    delete_email,
)
from app.services.vector_search import find_emails
from app.services.embedding_service import get_text_embedding
from app.services.generate_email import generate_email, classify_email

email_routes = Blueprint("emails", __name__)

# @email_routes.route("/email/<int:email_id>")
# def get_email(email_id):
#     for category, email_list in emails.items():
#         for email in email_list:
#             if email["id"] == email_id:
#                 return jsonify(email)
#     return jsonify({"error": "Email not found"}), 404


@email_routes.route("/emails", methods=["POST"])
def create_email_route():
    email_data = request.json
    email_id = create_email(email_data)
    if email_id:
        return jsonify({"_id": email_id}), 201
    else:
        return jsonify({"error": "Email could not be created"}), 400

@email_routes.route("/emails/flagged", methods=["GET"])
def get_flagged_emails_route():
    emails = get_all_emails()
    flagged_emails = [email for email in emails if email["flagged"]]
    if flagged_emails:
        return jsonify(flagged_emails), 200
    else:
        return jsonify({"error": "No flagged emails found"}), 404 


@email_routes.route("/emails/<email_id>", methods=["GET"])
def get_email_by_id_route(email_id):
    email = get_email_by_id(email_id)
    if email:
        return jsonify(email), 200
    else:
        return jsonify({"error": "Email not found"}), 404


@email_routes.route("/emails", methods=["GET"])
def get_all_emails_route():
    emails = get_all_emails()
    return jsonify(emails), 200


@email_routes.route("/emails/<email_id>", methods=["PUT"])
def update_email_route(email_id):
    email_data = request.json
    email = update_email(email_id, email_data)
    if email:
        return jsonify(email), 200
    else:
        return jsonify({"error": "Email not found"}), 404


@email_routes.route("/emails/<email_id>", methods=["DELETE"])
def delete_email_route(email_id):
    result = delete_email(email_id)
    if result:
        return jsonify({"message": "Email deleted"}), 200
    else:
        return jsonify({"error": "Email not found"}), 404

@email_routes.route("/emails/generated", methods=["GET"])
def generate_email_route():
    email = generate_email()
    # print("Generated email", email)
    # print("\n")
    if email:
        try:
            email = classify_email(email)
            # print("Classified email", email)
            print("\n")
        except Exception as e:
            print(f"Error classifying email: {e}")
        update_email(email["_id"], email)
        print("Updated email", email)
        print("\n")
        return jsonify(email), 200
    else:
        return jsonify({"error": "Emails could not be generated"}), 400
    
@email_routes.route('/find_emails', methods=['POST'])
def vector_search_emails():
    data = request.json
    text = data.get('search_text')
    limit = data.get('limit')
    print("Limit", limit)
    if not text:
        return jsonify({'error': 'Search text not provided'}), 400
    
    print("Search text", text)

    query_vec = get_text_embedding(text)

    # print("Query embedding vec", query_vec)

    if not query_vec:
        return jsonify({'error': 'Generating embedding failed'}), 500
    else:
        query_vec = query_vec['embedding']
        # print("Query embedding vec type", type(query_vec))

        emails = find_emails(query_vec, limit)
        # print("Emails matched in Routes", emails)
        return jsonify(emails), 200
