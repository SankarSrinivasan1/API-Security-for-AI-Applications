# Threat Modeling for AI APIs

## What Is Different About AI?

Traditional APIs:
- Deterministic
- Predictable outputs

AI APIs:
- Non-deterministic
- Influenced by user input (dangerous)
- Can leak internal context

---

## Key Risks

- Prompt injection
- Data exfiltration
- Context poisoning
- Unauthorized usage

---

## Basic Model

Assets:
- API keys
- Model prompts
- User data

Actors:
- Legit users
- Malicious users
- Bots

Entry Points:
- API requests
- Prompt input
- File uploads

---

## Simple Flow

User → API → Prompt Builder → LLM → Response → User

Each step is attackable.

---

## Golden Rule

> Never trust user input inside prompts.
