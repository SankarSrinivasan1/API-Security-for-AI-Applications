# API Key Security

## Rules

- Never expose keys in frontend
- Store in environment variables
- Rotate regularly
- Scope keys (read-only, write-only)

---

## Example (Bad)

const API_KEY = "sk-123456"

---

## Example (Good)

import os
API_KEY = os.getenv("API_KEY")

---

## Extra Protection

- IP allowlisting
- Usage quotas
- Key expiration

---

## Tip

Treat API keys like passwords. Not like config.
