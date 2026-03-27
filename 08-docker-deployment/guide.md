# Secure Docker Deployment

## Why Docker Security Matters

Your container:
- Contains secrets
- Runs your API
- Is a target

Misconfigured Docker = instant compromise

---

## Common Mistakes

- Running as root
- Hardcoding secrets
- Open ports
- No network isolation

---

## Best Practices

- Use minimal base images
- Use non-root user
- Store secrets in env variables
- Scan images regularly

---

## Rule

> If someone breaks your container, they own your API.
