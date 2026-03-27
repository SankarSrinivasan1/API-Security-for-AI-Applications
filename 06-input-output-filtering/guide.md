# Input and Output Filtering

## Why Filtering Matters

AI models:
- Don’t know what is sensitive
- Will happily output secrets

---

## Two Layers

1. Input filtering → block attacks
2. Output filtering → prevent leaks

---

## Examples

Input:
"Ignore instructions"

Output:
"API key is sk-xxx"

Both must be handled.

---

## Rule

> Filter before AND after the model.
