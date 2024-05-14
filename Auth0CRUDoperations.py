from flask import Flask, request, jsonify
import requests
import sys
import json
import os

app = Flask(__name__)

# Auth0 Management API details
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')

# Auth0 OAuth/Token endpoint details
AUTH0_CLIENT_ID = os.environ.get('client_id')
AUTH0_CLIENT_SECRET = os.environ.get('client_secret')
@app.route('/users', methods=['GET'])
def get_users():
    AUTH0_API_TOKEN=get_access_token()
    url = f'https://{AUTH0_DOMAIN}/api/v2/users'
    headers = {
        'Authorization': f'Bearer {AUTH0_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error retrieving users: {response.text}")
@app.route('/users', methods=['POST'])
def create_user():
    email = request.json.get('email')
    password = request.json.get('password')
    connection = request.json.get('connection')
    AUTH0_API_TOKEN=get_access_token()
    url = f'https://{AUTH0_DOMAIN}/api/v2/users'
    headers = {
        'Authorization': f'Bearer {AUTH0_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    user_data = {
        'email': email,
        'password': password,
        'connection': connection
    }
    response = requests.post(url, headers=headers, json=user_data)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Error creating user: {response.text}")
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    AUTH0_API_TOKEN=get_access_token()
    users=get_users()
    if user_id not in [user['user_id'] for user in users]:
        raise Exception(f"User with ID {user_id} not found")
    else:
       url = f'https://{AUTH0_DOMAIN}/api/v2/users/{user_id}'
       headers = {
        'Authorization': f'Bearer {AUTH0_API_TOKEN}',
        'Content-Type': 'application/json'
        }
       response = requests.delete(url, headers=headers)
       if response.status_code == 204:
            return "User deleted successfully"
       else:
            raise Exception(f"Error deleting user: {response.text}")

def get_access_token():
    url = f'https://{AUTH0_DOMAIN}/oauth/token'
    payload = {
        'client_id': AUTH0_CLIENT_ID,
        'client_secret': AUTH0_CLIENT_SECRET,
        'audience': f'https://{AUTH0_DOMAIN}/api/v2/',
        'grant_type': 'client_credentials'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Error retrieving access token: {response.text}")
AUTH0_API_TOKEN = get_access_token()
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) < 2:
            print("Usage: python Auth0CRUDoperations.py <action> [options]")
            sys.exit(1)
        action = sys.argv[1]
        if action == "get_users":
            print(get_users())
        elif action == "create_user":
            if len(sys.argv) != 5:
                print("Usage: python Auth0CRUDoperations.py create_user <email> <password> <connection>")
                sys.exit(1)
            email = sys.argv[2]
            password = sys.argv[3]
            connection = sys.argv[4]
            print(create_user(email, password, connection))
        elif action == "delete_user":
            if len(sys.argv) != 3:
                print("Usage: python Auth0CRUDoperations.py delete_user <user_id>")
                sys.exit(1)
            user_id = sys.argv[2]
            print(delete_user(user_id))
        elif action == "get_access_token":
            print(get_access_token())
        else:
            print("Invalid action. Please use 'get_users', 'create_user', 'delete_user', or 'get_access_token'.")
            sys.exit(1)
    else:
         app.run(debug=True)
   