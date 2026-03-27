# Example Threat Model

## System

AI chatbot for customer support

## Assets

- Customer data
- Internal instructions
- API keys

## Threats

| Threat | Impact | Mitigation |
|------|--------|-----------|
| Prompt injection | Data leak | Input filtering |
| API abuse | Cost spike | Rate limiting |
| Token leak | Full compromise | Secrets management |

---

## Conclusion

Biggest risk: model manipulation via input.
