# 👥 Agent-Skins: Production-Ready AI Agent Prompts & Tool Configs

> The "Shadcn UI" / "Tailwind UI" equivalent for AI Agents. A massive, high-performance database of **17,280+ copy-pasteable role profiles, framework blueprints, compliance guardrails, and model-optimized system instructions** tailored for specific business tasks.

---

## 🚀 Key Features

*   **120 Professional Roles:** Pre-tested prompts spanning Sales, Finance, HR, Marketing, Engineering, Support, Operations, Product, Legal, Security, IT, and Design.
*   **12 Industry Verticals:** Custom compliance guidelines injected dynamically per industry (e.g., HIPAA for HealthTech, PCI-DSS for FinTech, FERPA for EdTech, GDPR for SaaS).
*   **4 Mainstream Frameworks:** Copy-paste boilerplate setups for:
    *   **CrewAI** (Python)
    *   **LangGraph** (Python)
    *   **AutoGen** (Python)
    *   **Vercel AI SDK** (TypeScript)
*   **3 Model Optimizations:** Optimizations for specific model formatting needs:
    *   **Anthropic:** XML-tagged structured guidelines for Claude.
    *   **OpenAI:** System instructions tailored for JSON Schema outputs.
    *   **Llama:** Explicit system format blocks optimized for Llama 3 models.

---

## 📂 Repository Layout

The skins are organized cleanly by Department ➔ Industry ➔ Role:
```text
agent-skins/
├── compiler/
│   ├── skins_compiler.py       # Core combinatoric generator engine
│   └── test_skins.py           # Automated validator script
├── skins/
│   ├── sales/
│   │   ├── saas/
│   │   │   └── lead_qualifier/
│   │   │       ├── crewai_openai_optimized.py
│   │   │       ├── crewai_anthropic_optimized.py
│   │   │       ├── langgraph_openai_optimized.py
│   │   │       ├── vercel_ai_sdk_anthropic_optimized.ts
│   │   │       └── ... (12 combinations per role)
│   │   └── fintech/
│   ├── finance/
│   ├── marketing/
│   ├── engineering/
│   └── ... (12 departments total)
└── README.md
```

---

## 🛠️ Usage Example

Looking for a **Lead Qualifier** agent optimized for **SaaS** compliance (GDPR/SOC2) running on **CrewAI** using **OpenAI**?

Simply copy the content of `skins/sales/saas/lead_qualifier/crewai_openai_optimized.py`:

```python
from crewai import Agent, Task, Crew
# CrewAI Framework Skin Configuration
def initialize_agent(tools):
    return Agent(
        role="Lead Qualifier",
        goal="Analyze and score incoming leads based on professional rubrics and intent signals.",
        backstory="A seasoned Lead Qualifier with deep expertise in the SaaS vertical.",
        tools=tools,
        verbose=True,
        memory=True
    )

/*
--- System Prompt ---
System Role: Lead Qualifier
Goal: Analyze and score incoming leads based on professional rubrics and intent signals.

Core Prompt:
Identity: You are a professional Lead Qualifier working in the SaaS industry.
Core Goal: Analyze and score incoming leads based on professional rubrics and intent signals.
Industry Standard Terms: Multi-tenancy, churn rate, LTV, ARR, API limits, webhook retries.
Execution Steps:
1. Audit context data for SaaS industry parameters.
2. Verify compliance against GDPR & SOC2 Compliance.
3. Apply guardrail: Strictly block exposing raw PII (Personally Identifiable Information). Enforce data minimization.
4. Output structured results cleanly.
...
*/
```

---

## ⚡ Running the Compiler Locally

You can customize the base prompts, compliance guidelines, or framework boilerplates in `compiler/skins_compiler.py` and compile a fresh batch of 17,280 files:

1. Navigate to the project root:
   ```bash
   cd agent-skins
   ```

2. Compile the database:
   ```bash
   python compiler/skins_compiler.py
   ```

3. Run automated tests to verify file structure integrity:
   ```bash
   python compiler/test_skins.py
   ```
