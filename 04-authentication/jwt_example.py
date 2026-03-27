import jwt
import datetime

SECRET = "supersecretkey"

def generate_token(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return token

def verify_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

if __name__ == "__main__":
    token = generate_token("user_123")
    print("Token:", token)

    decoded = verify_token(token)
    print("Decoded:", decoded)
