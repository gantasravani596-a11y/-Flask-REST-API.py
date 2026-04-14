from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = []

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# POST (add new user)
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added"}), 201

# PUT (update user)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    for user in users:
        if user["id"] == user_id:
            user.update(request.json)
            return jsonify({"message": "User updated"}), 200
    return jsonify({"message": "User not found"}), 404

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
