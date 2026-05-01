# Simple Role-Based Access Control system

users = {
    "alice": "admin",
    "bob": "staff",
    "charlie": "user"
}

permissions = {
    "admin": ["view_logs", "delete_user", "view_dashboard", "edit_settings"],
    "staff": ["view_dashboard"],
    "user": ["view_dashboard"]
}

def access_control(username, action):
    role = users.get(username)

    if not role:
        return "Access Denied: User does not exist"

    if action in permissions[role]:
        return f"Access Granted: {username} performed {action}"
    else:
        return f"Access Denied: {username} not allowed to perform {action}"


# TEST CASES
print(access_control("alice", "delete_user"))
print(access_control("bob", "delete_user"))
print(access_control("charlie", "view_dashboard"))
print(access_control("charlie", "edit_settings"))