import storage  # Handles file-based storage
import os

USER_FILE = 'users.json'
users = storage.load_from_file(USER_FILE)

def add_user(name: str, user_id: int) -> None:
    """
    Add a new user to the system and save to file.
    """
    if any(user["user_id"] == user_id for user in users):
        print(f"User ID {user_id} already exists. Please use a unique ID.")
        return

    users.append({"name": name, "user_id": user_id})
    storage.save_to_file(USER_FILE, users)
    print(f"User '{name}' with ID {user_id} added successfully.")

def update_user(user_id: int, new_name: str = None) -> None:
    """
    Update a user's details and save to file.
    """
    for user in users:
        if user["user_id"] == user_id:
            if new_name:
                user["name"] = new_name
            storage.save_to_file(USER_FILE, users)
            print(f"User ID {user_id} updated successfully.")
            return
    print(f"User ID {user_id} not found.")

def delete_user(user_id: int) -> None:
    """
    Delete a user from the system and save changes to file.
    """
    global users
    users = [user for user in users if user["user_id"] != user_id]
    storage.save_to_file(USER_FILE, users)
    print(f"User ID {user_id} deleted successfully.")

def list_users() -> None:
    """
    List all users in the system.
    """
    if not users:
        print("No users available.")
        return
    for user in users:
        print(f"Name: {user['name']}, User ID: {user['user_id']}")

def search_users(attribute: str, value: str) -> None:
    """
    Search for users by a specific attribute.
    """
    results = [user for user in users if user.get(attribute) == value]
    if not results:
        print(f"No users found with {attribute} '{value}'.")
        return
    for user in results:
        print(f"Name: {user['name']}, User ID: {user['user_id']}")
