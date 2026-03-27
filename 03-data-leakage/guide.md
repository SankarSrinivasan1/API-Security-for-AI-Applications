# Data Leakage in AI APIs

## What Is Data Leakage?

When the model exposes:
- Sensitive user data
- Internal prompts
- API keys
- Hidden context

---

## Why It Happens

LLMs:
- Predict text
- Not designed for confidentiality
- Can "accidentally" reveal data

---

## Common Sources

- Logs passed into prompt
- Full documents in context
- Debug info
- Poor filtering

---

## Real Risk

> One bad response can expose your entire system.

---

## Prevention Strategy

- Minimize context
- Redact sensitive data
- Filter outputs
- Avoid passing secrets
