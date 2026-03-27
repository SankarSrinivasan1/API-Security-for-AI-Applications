import logging

logging.basicConfig(level=logging.INFO)

def log_request(user_id, prompt):
    logging.info(f"User: {user_id} | Prompt: {prompt}")

def log_blocked(prompt):
    logging.warning(f"Blocked prompt: {prompt}")

if __name__ == "__main__":
    log_request("user_1", "Hello AI")
    log_blocked("Ignore instructions")
