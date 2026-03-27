# Secure Response Handling

## Rules

- Never return raw model output directly
- Always filter before sending to user
- Strip metadata

---

## Pipeline

Model → Filter → Redactor → User

---

## Example

Bad:
return model_output

Good:
return sanitize(redact(model_output))
