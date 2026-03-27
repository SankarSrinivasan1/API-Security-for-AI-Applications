import time
from collections import defaultdict

RATE_LIMIT = 5  # requests
WINDOW = 10     # seconds

requests_log = defaultdict(list)

def is_allowed(user_id: str) -> bool:
    now = time.time()
    window_start = now - WINDOW

    requests = requests_log[user_id]
    
    # Remove old requests
    requests = [req for req in requests if req > window_start]
    requests_log[user_id] = requests

    if len(requests) >= RATE_LIMIT:
        return False

    requests.append(now)
    return True

if __name__ == "__main__":
    user = "user_1"

    for i in range(10):
        if is_allowed(user):
            print(f"Request {i}: Allowed")
        else:
            print(f"Request {i}: Blocked")
        time.sleep(1)
