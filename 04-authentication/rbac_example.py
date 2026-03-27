from typing import Dict

# Mock user database
USERS = {
    "user_1": {"role": "user"},
    "admin_1": {"role": "admin"}
}

PERMISSIONS = {
    "user": ["read"],
    "admin": ["read", "write", "delete"]
}

def has_permission(user_id: str, action: str) -> bool:
    user = USERS.get(user_id)
    if not user:
        return False
    
    role = user["role"]
    allowed = PERMISSIONS.get(role, [])
    
    return action in allowed

if __name__ == "__main__":
    print(has_permission("user_1", "delete"))  # False
    print(has_permission("admin_1", "delete")) # True
