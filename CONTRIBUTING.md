# Contributing to Agent-Skins

We are excited to build the world's largest, high-performance database of AI Agent prompts and configurations! Here is how you can help.

---

## 🛠️ How the Prompts are Generated

All configurations inside the `skins/` directory are generated programmatically using the compiler located at `compiler/skins_compiler.py`. 

**Please do not edit files in the `skins/` directory directly.** They will be overwritten the next time the compiler is executed.

---

## ⚡ Adding New Skins

### 1. Adding a New Role
To add a new role to an existing department, open `compiler/skins_compiler.py`, locate the target department inside the `DEPARTMENTS` dictionary, and append your role details:

```python
{
    "role": "New Role Name",
    "goal": "Clear actionable goal statement."
}
```

### 2. Adding a New Industry Vertical
To introduce a new industry compliance or vocabulary guideline, add an entry to the `INDUSTRIES` dictionary:

```python
"Your_Industry": {
    "standard": "Compliance Standards (e.g. HIPAA, SOC2)",
    "guardrail": "Specific safety guardrails.",
    "terms": "Comma-separated list of domain specific terms."
}
```

---

## 🧪 Compiling and Testing

Once you make changes to the compiler configuration:

1. Recompile the database:
   ```bash
   python compiler/skins_compiler.py
   ```

2. Run automated validation tests:
   ```bash
   python compiler/test_skins.py
   ```

3. Ensure all tests pass before opening a Pull Request!
