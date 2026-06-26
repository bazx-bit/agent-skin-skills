# Contributing to Agent-Skins

We are excited to build the world's largest database of AI Agent prompts and configurations! Here is how you can help.

---

## ⚡ Adding New Skins

We accept contributions for new roles, industries, and framework setups. Since configurations are structured statically, please follow these guidelines when adding files.

### Folder Structure
All configurations are placed using the following path formula:
```text
skins/{department}/{industry}/{role_id}/
```

For example, to add an AI agent for a **Lead Qualifier** in **SaaS** within the **Sales** department:
* Directory: `skins/sales/saas/lead_qualifier/`

### 1. Adding a Universal Prompt
Create a `raw_prompt.md` file inside the target directory following this outline:
- **Identity & Backstory**: Professional profile, tone, and system boundaries.
- **Core Objective**: The main goal statement of the agent.
- **Compliance standard**: Checklists for safety limits (e.g. HIPAA, PCI-DSS, GDPR).
- **Workflow**: Explicit step-by-step reasoning.
- **Worked Examples**: Clear few-shot scenarios demonstrating inputs and expected outputs.

### 2. Adding Framework Configurations
If you want to provide pre-configured setups for popular frameworks, add files named:
* `crewai_openai_optimized.py` / `crewai_anthropic_optimized.py`
* `langgraph_openai_optimized.py` / `langgraph_anthropic_optimized.py`
* `autogen_openai_optimized.py` / `autogen_anthropic_optimized.py`
* `vercel_ai_sdk_openai_optimized.ts` / `vercel_ai_sdk_anthropic_optimized.ts`

---

## 🧪 Submission Checklist

Before submitting a Pull Request:
1. Ensure files are correctly formatted and placed under the correct department/industry path.
2. Confirm prompts do not contain any private credentials, API keys, or personal details.
3. Test your configuration templates locally with the respective agent frameworks.
