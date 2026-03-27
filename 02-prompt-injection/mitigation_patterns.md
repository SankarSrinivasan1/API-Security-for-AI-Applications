# Prompt Injection Mitigation Patterns

## 1. Instruction Separation

Never mix:
- System instructions
- User input

Bad:
System + User → One prompt

Good:
Use structured input:
{
  "system": "...",
  "user": "..."
}

---

## 2. Input Validation

Reject inputs containing:
- "ignore previous instructions"
- "reveal system prompt"
- "developer mode"

---

## 3. Output Filtering

Scan model output for:
- Secrets
- Internal instructions
- Tokens

---

## 4. Allowlist Approach

Only allow:
- Defined commands
- Safe queries

Everything else → reject

---

## 5. Context Limiting

Do NOT pass:
- Full documents
- Sensitive logs
- API keys

---

## 6. Tool Isolation

If using tools:
- Validate tool inputs
- Restrict tool access
- Log every call

---

## Final Rule

> Treat the model like an untrusted employee.
