import re
from typing import List
from src.models import SlopFinding, SlopScorecard

class PRSlopDetector:
    """Detects AI-generated code bloat, dependency inflation, and shallow mock tests."""

    BLOATED_DEPENDENCIES = {
        "lodash": "Use native JavaScript Array/Object methods (e.g., Array.prototype.map, filter, reduce).",
        "moment": "Use native Intl.DateTimeFormat or lightweight Dayjs/date-fns.",
        "request": "Deprecated. Use native fetch() API.",
        "left-pad": "Use native String.prototype.padStart().",
        "underscore": "Use modern ES6+ native utilities."
    }

    def audit_diff(self, pr_id: str, diff_text: str) -> SlopScorecard:
        findings = []
        lines = diff_text.split("\n")
        total_lines = len(lines)
        prunable_lines = 0

        # 1. Audit Dependency Bloat
        for pkg, fix in self.BLOATED_DEPENDENCIES.items():
            pattern = rf"(import .*? from ['\"]{pkg}['\"]|require\(['\"]{pkg}['\"]\))"
            if re.search(pattern, diff_text):
                findings.append(SlopFinding(
                    category="DEPENDENCY_BLOAT",
                    severity="HIGH",
                    description=f"Imported heavy external library '{pkg}' for basic utility operations.",
                    remediation=fix
                ))
                prunable_lines += 5

        # 2. Audit Shallow / Fake Mock Tests
        if re.search(r"(expect\(true\)\.toBe\(true\)|assert True|expect\(1\)\.toBe\(1\))", diff_text):
            findings.append(SlopFinding(
                category="SHALLOW_MOCK_TEST",
                severity="CRITICAL",
                description="Tautological test assertion detected. Test asserts truth without verifying production state mutations.",
                remediation="Remove tautological assertion; assert real function outputs against boundary invariants."
            ))
            prunable_lines += 8

        # 3. Detect Over-Engineering: Abstract Factory / Singleton Boilerplate
        if re.search(r"class .*?Factory.*?|class .*?Singleton.*?", diff_text):
            if total_lines < 150:  # Small feature over-engineered with heavy design patterns
                findings.append(SlopFinding(
                    category="OVER_ENGINEERING",
                    severity="MEDIUM",
                    description="Heavy OOP design pattern (Factory/Singleton) introduced for low-complexity feature logic.",
                    remediation="Simplify to a pure functional module or plain object map to reduce indirection."
                ))
                prunable_lines += 25

        # 4. Detect Parrot Comments
        parrot_count = 0
        for i, line in enumerate(lines):
            # Matches comments like: // function to get user or # sets value to value
            if re.search(r"(//|#)\s*(get|set|check|return|calls?)\s+(\w+)\s*$", line, re.IGNORECASE):
                parrot_count += 1
                prunable_lines += 1
        
        if parrot_count >= 2:
            findings.append(SlopFinding(
                category="PARROT_COMMENTS",
                severity="MEDIUM",
                description=f"Detected {parrot_count} parrot comments that explain the obvious without providing architectural context.",
                remediation="Remove redundant inline comments; let clear self-documenting code speak for itself."
            ))

        # Calculate Slop Index Score (0 to 100%)
        severity_weights = {"CRITICAL": 35, "HIGH": 25, "MEDIUM": 15}
        raw_score = sum(severity_weights.get(f.severity, 10) for f in findings)
        slop_index = min(raw_score, 100)

        verdict = "CLEAN_READY_FOR_REVIEW" if slop_index < 30 else "SLOP_DETECTED_REFACTOR_REQUIRED"

        advice = (
            "Code is lean, idiomatic, and adheres to clean architecture principles."
            if slop_index < 30 else
            f"PR contains AI-generated bloat. Prune approximately {prunable_lines} redundant lines and remove shallow mocks before requesting human review."
        )

        return SlopScorecard(
            pr_id=pr_id,
            slop_index_score=slop_index,
            verdict=verdict,
            lines_analyzed=total_lines,
            estimated_lines_prunable=prunable_lines,
            findings=findings,
            minimalist_refactoring_advice=advice
        )
