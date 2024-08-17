from flask import Blueprint, request, jsonify, Flask
from app.services.email_service import (
    create_email,
    get_email_by_id,
    get_all_emails,
    update_email,
    delete_email,
)
from app.services.vector_search import find_emails
from app.services.generate_email import generate_email

email_routes = Blueprint("emails", __name__)

@email_routes.route("/email/<int:email_id>")
def get_email(email_id):
    for category, email_list in emails.items():
        for email in email_list:
            if email["id"] == email_id:
                return jsonify(email)
    return jsonify({"error": "Email not found"}), 404


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
        return jsonify(flagged_emails[:10]), 200
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
    return jsonify(emails[:10]), 200


@email_routes.route("/emails/<email_id>", methods=["PATCH"])
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
    if email:
        return jsonify(email), 200
    else:
        return jsonify({"error": "Emails could not be generated"}), 400
    
@email_routes.route('/find-emails', methods=['POST'])
def vector_search_emails():
    data = request.json
    query_vec = data.get('query_vector')
    limit = data.get('limit', 1)

    if not query_vec:
        return jsonify({'error': 'Query vector not provided'}), 400
    else:
        emails = find_emails(query_vec, limit)
        return jsonify(emails), 200
