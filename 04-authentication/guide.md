# Authentication for AI APIs

## Why This Matters

AI APIs are:
- Expensive (token costs)
- Powerful (can trigger actions)
- Abusable (bots love them)

If your auth is weak:
→ You don’t just get hacked  
→ You get billed

---

## Common Mistakes

- Exposing API keys in frontend
- No user-level authentication
- No rate limits per user
- Using one global key

---

## What You Need

1. API key protection
2. User authentication (JWT)
3. Authorization (RBAC)
4. Usage tracking

---

## Recommended Stack

- API Keys → for service-to-service
- JWT → for users
- RBAC → for permissions

---

## Golden Rule

> Every request must be identifiable and accountable.
