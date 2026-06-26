# 👥 Agent-Skins

### 18,720+ Production-Ready AI Agent Prompts, Tool Schemas & Framework Configs

Stop spending weeks debugging prompts. Pick a role, pick your industry, pick your framework — and ship.

---

## What is this?

Every file in this repository is a complete, ready-to-use AI agent configuration. Each folder contains:

- ✅ **Framework configurations**: Copy-pasteable boilerplate for CrewAI, LangGraph, AutoGen, or Vercel AI SDK.
- ✅ **Universal raw prompts (`raw_prompt.md`)**: A framework-agnostic system prompt with **2,100+ lines of production-grade depth** for ChatGPT, Claude, Gemini, Ollama, or any API.
- ✅ **Multi-Point Audit Matrix (`AUD-01` to `AUD-05`)**: Adherence checklists for compliance (HIPAA, GDPR, PCI-DSS, etc.).
- ✅ **Zero-Trust Logic**: Strict separation of facts (`[FACT]`) and inferences (`[INFERENCE]`) to prevent hallucinations.
- ✅ **Interactive Self-Evaluation**: Built-in 1-10 scoring check with self-correction logic.
- ✅ **15 worked few-shot scenarios**: Covering standard runs, edge cases, out-of-scope requests, and validation failures.
- ✅ **55-case appendix**: Context-rich manual pages to help models maintain their persona during long execution sessions.

No setup. No API keys. No dependencies. Just find what you need and use it.

---

## 📊 What's Inside

| Dimension | Count | Details |
| :--- | :--- | :--- |
| **Departments** | 12 | Sales, Finance, HR, Marketing, Engineering, Customer Support, Operations, Product, Legal, Security, IT Admin, Design |
| **Roles per Dept** | 10 | 120 unique professional agent profiles |
| **Industry Verticals** | 12 | SaaS, FinTech, E-commerce, HealthTech, Real Estate, EdTech, Logistics, PropTech, AgTech, BioTech, CyberSecurity, InsurTech |
| **Framework-Agnostic Prompts** | **1,440** | `raw_prompt.md` files (2,100+ lines each) for any LLM or client |
| **Framework & Model Configs** | **17,280** | Optimized files for CrewAI, LangGraph, AutoGen, and Vercel AI SDK |
| **Total Configurations** | **18,720** | Every combination of the above |

---

## 📂 How Files Are Organized

```text
skins/
├── sales/
│   ├── saas/
│   │   └── lead_qualifier/
│   │       ├── crewai_openai_optimized.py
│   │       ├── crewai_anthropic_optimized.py
│   │       ├── langgraph_llama_optimized.py
│   │       ├── autogen_openai_optimized.py
│   │       ├── vercel_ai_sdk_anthropic_optimized.ts
│   │       └── ... (12 files per role)
│   ├── fintech/
│   ├── healthtech/
│   └── ... (12 industries)
├── finance/
├── hr/
├── marketing/
├── engineering/
├── customer_support/
├── operations/
├── product/
├── legal/
├── security/
├── it_admin/
└── design/
```

**Path formula:** `skins/{department}/{industry}/{role}/{framework}_{model}_optimized.{py|ts}`

---

## ⚡ Quick Start

### Option 1: Browse and Copy
Navigate the `skins/` folder, find the file matching your use case, and copy the contents into your project.

### Option 2: Use the Interactive CLI
We ship a zero-dependency search tool at the root of this repo:

**List all departments:**
```bash
python skins.py list departments
```

**List all industries:**
```bash
python skins.py list industries
```

**Search by keyword:**
```bash
python skins.py search expense
python skins.py search vulnerability
python skins.py search onboard
```

**Fetch a specific skin:**
```bash
python skins.py get sales saas lead_qualifier crewai openai
python skins.py get security healthtech vulnerability_auditor langgraph anthropic
python skins.py get hr edtech candidate_screener autogen llama
```

---

## 🛠️ Example Output

Running `python skins.py get finance fintech expense_reconciler crewai anthropic` gives you:

```python
from crewai import Agent, Task, Crew

def initialize_agent(tools):
    return Agent(
        role="Expense Reconciler",
        goal="Validate employee expense submissions against company travel and spend policies.",
        backstory="A seasoned Expense Reconciler with deep expertise in the FinTech vertical.",
        tools=tools,
        verbose=True,
        memory=True
    )

# Full system prompt with PCI-DSS compliance guardrails,
# FinTech domain vocabulary, and Anthropic XML-tag formatting
# is included in the file footer.
```

---

## 🏗️ Supported Frameworks

| Framework | Language | Use Case |
| :--- | :--- | :--- |
| **CrewAI** | Python | Multi-agent teams with role-based collaboration |
| **LangGraph** | Python | Stateful graph-based agent orchestration |
| **AutoGen** | Python | Conversational multi-agent systems |
| **Vercel AI SDK** | TypeScript | Edge-deployed AI applications |

---

## 🔒 Built-In Compliance Standards

Every skin includes industry-appropriate guardrails:

| Industry | Standard | What the Guardrail Does |
| :--- | :--- | :--- |
| SaaS | GDPR & SOC2 | Blocks PII exposure, enforces data minimization |
| FinTech | PCI-DSS & SEC | Blocks raw credit card numbers, enforces transaction audits |
| HealthTech | HIPAA & HITECH | Blocks PHI in logs, enforces encryption rules |
| EdTech | FERPA & COPPA | Blocks minor profiles without parent auth |
| E-commerce | PCI-DSS | Verifies price formats, blocks negative stock |
| BioTech | FDA Part 11 | Blocks modification of locked trial records |
| CyberSecurity | ISO 27001 & NIST | Enforces log integrity, blocks write to event archives |
| InsurTech | NAIC Rules | Audits claim calculations against policies |
| Real Estate | Fair Housing Act | Enforces zero-bias descriptions |
| Logistics | FMCSA | Enforces weight limits and transport regulations |
| PropTech | Tenant Rights | Blocks unsigned lease modifications |
| AgTech | USDA & EPA | Enforces chemical and pesticide tracking |

---

## 🤝 Contributing

Want to add a new role, industry, or framework? See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

MIT — use it however you want. See [LICENSE](LICENSE).
