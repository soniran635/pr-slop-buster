from pydantic import BaseModel, Field
from typing import List, Optional

class SlopFinding(BaseModel):
    category: str  # 'DEPENDENCY_BLOAT', 'SHALLOW_MOCK_TEST', 'OVER_ENGINEERING', 'PARROT_COMMENTS'
    severity: str  # 'CRITICAL', 'HIGH', 'MEDIUM'
    line_reference: Optional[str] = None
    description: str
    remediation: str

class SlopScorecard(BaseModel):
    pr_id: str
    slop_index_score: int  # 0 to 100%
    verdict: str  # 'CLEAN_READY_FOR_REVIEW' or 'SLOP_DETECTED_REFACTOR_REQUIRED'
    lines_analyzed: int
    estimated_lines_prunable: int
    findings: List[SlopFinding] = []
    minimalist_refactoring_advice: str
