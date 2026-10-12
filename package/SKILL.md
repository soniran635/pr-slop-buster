---
name: pr-slop-buster
description: Autonomous code review assistant that detects AI-generated code bloat, heavy dependency inflation, over-engineered factory boilerplate, and shallow tautological mock tests in pull requests. Enforces minimalist, clean architecture before human review.
---

# PR-Slop-Buster: AI Code Bloat & Dependency Auditor

Equips AI coding assistants (Claude Code, Cursor, Copilot, Codex) with a ruthless Staff Engineer review lens to strip out AI-generated boilerplate, fake tests, and dependency bloat.

## When to Activate This Skill
Activate this skill whenever:
1. You finish generating code with an AI assistant and want to audit it for bloat before opening a PR.
2. You are reviewing an AI-assisted pull request diff.
3. You want to check for unnecessary npm/pip dependencies or shallow tautological mock tests.

## 4 Core Slop Audits Enforced

### 1. Dependency Bloat Audit
- Flags importing heavy external libraries (e.g., lodash, moment, request, left-pad) when native standard library one-liners exist.
- Provides immediate drop-in native standard-library replacements.

### 2. Tautological / Fake Mock Test Detection
- Catches tests that assert truth without verifying production state mutations (e.g., expect(true).toBe(true) or assert True).
- Detects mock abuse where dependencies are over-mocked to artificially inflate test coverage.

### 3. Over-Engineering & Boilerplate Decoupling
- Flags premature abstractions (Abstract Factory, Singleton, multi-layer wrappers) on low-complexity feature code.
- Suggests pure functional modules or plain object maps to minimize cognitive load.

### 4. Parrot Comment Pruning
- Identifies comments that simply rephrase function or variable names without providing architectural context.

## Workflow Execution
1. Analyze the git diff or file changes.
2. Calculate the Slop Index Score (0% Clean to 100% High Slop).
3. Generate the structured PR Slop Scorecard with actionable minimalist refactoring advice.
