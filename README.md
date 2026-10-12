# 🧹 PR-Slop-Buster: AI Code Bloat & Dependency Auditor

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
  <img src="https://img.shields.io/badge/Focus-Code_Quality_%26_Review-blue?style=for-the-badge" alt="Code Quality" />
</p>

> An autonomous code review assistant for Cursor, Claude Code, and Copilot that strips AI-generated boilerplate, flags heavy dependency bloat, detects shallow tautological mock tests, and enforces minimalist clean architecture before human review.

---

## 📌 The Problem: The Rise of "AI Slop" in Pull Requests

With AI coding tools accelerating code generation, pull request volume has tripled. However, senior and staff engineers are burning out reviewing pull requests that look plausible on the surface but harbor hidden technical debt:

1. **Dependency Bloat:** AI assistants frequently import heavy 2MB external packages (`lodash`, `moment`, `request`) for trivial 3-line utility operations native to modern standard libraries.
2. **Fake / Tautological Mock Tests:** AI generates dozens of unit tests that mock out everything and assert nothing (e.g. `expect(true).toBe(true)`), giving teams a false sense of test coverage.
3. **Architectural Over-Engineering:** Prompts requesting simple features result in 300+ lines of redundant Abstract Factories, singletons, and complex wrapper classes where clean 20-line pure functions suffice.
4. **Review Fatigue:** Senior engineers spend hours wading through hundreds of lines of AI boilerplate trying to locate core business logic.

---

## 💡 The Solution: Autonomous Pre-Review Slop Gating

**PR-Slop-Buster** acts as a virtual Staff Architect reviewing code diffs before they reach human reviewers:

```mermaid
flowchart TD
    A["Pull Request Diff / AI-Generated Code"] --> B["PR-Slop-Buster Engine"]

    subgraph Deep_Code_Audits ["Deep Code Audits"]
        B --> C["Dependency Bloat Audit: Standard Library Replacements"]
        B --> D["Shallow Mock Test Detection: Flags Tautologies"]
        B --> E["Over-Engineering Decoupler: Strips Factory Boilerplate"]
        B --> F["Parrot Comment Pruner: Removes Obvious Rephrasing"]
    end

    C & D & E & F --> G["Slop Index Scorecard: 0% Clean to 100% Slop"]
    G --> H{"Review Gate Verdict"}
    H -->|Slop >= 30%| I["🚨 SLOP DETECTED: Actionable Refactor Advice"]
    H -->|Slop < 30%| J["✅ CLEAN: Ready for Human Code Review"]
```
---

## 🛡️ The 4 Slop Audits Enforced

| Audit Category | What It Detects | Staff Architect Remediation |
| :--- | :--- | :--- |
| **Dependency Bloat** | Importing `lodash`, `moment`, or heavy utilities for basic array/date math. | Drop-in replacements using native modern standard library APIs. |
| **Shallow Mock Tests** | Tautological assertions (e.g. `expect(true).toBe(true)`, `assert True`). | Forces tests to verify concrete state mutations and boundary conditions. |
| **Over-Engineering** | Premature Abstract Factory or Singleton design patterns on small features. | Simplifies complex class hierarchies into pure, decoupled functions. |
| **Parrot Comments** | Comments that simply restate function names (e.g. `// get user`). | Prunes comment noise to let self-documenting code speak for itself. |

---

## 🛠️ Tech Stack

* **Engine:** Python 3.9+, Pydantic v2, Regular Expression Syntax Parsers
* **Interactive Dashboard:** Streamlit
* **Agent Integration:** Universal `SKILL.md` format for Cursor, Claude Code, and Copilot
* **License:** MIT License

---

## 🚀 Quickstart

### 1. Clone & Set Up
```bash
git clone [https://github.com/soniran635/pr-slop-buster.git](https://github.com/soniran635/pr-slop-buster.git)
cd pr-slop-buster

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
