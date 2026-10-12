import re
import sys

def audit_text(diff_text: str):
    issues = []
    if re.search(r"(import .*? from ['"]lodash['"]|require\(['"]lodash['"]\))", diff_text):
        issues.append("HIGH [DEPENDENCY_BLOAT]: lodash imported. Use native ES6+ Array/Object methods.")
    if re.search(r"(expect\(true\)\.toBe\(true\)|assert True)", diff_text):
        issues.append("CRITICAL [FAKE_TEST]: Tautological test assertion detected. Does not verify production state.")
    return issues

if __name__ == "__main__":
    print("PR-Slop-Buster Scanner active.")
