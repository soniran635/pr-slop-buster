import os
import sys

# Ensure project root is in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from src.slop_detector import PRSlopDetector

st.set_page_config(
    page_title="PR-Slop-Buster | AI Code Bloat Auditor",
    layout="wide",
    page_icon="🧹"
)

# Custom Styling for modern dark DevEx SaaS look
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0px;
    }
    .sub-narrative {
        font-size: 1.05rem;
        color: #A0AAB4;
        margin-bottom: 25px;
        line-height: 1.5;
        border-left: 3px solid #FF4B4B;
        padding-left: 15px;
    }
    .failure-box {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .cure-box {
        background-color: #0D281E;
        border: 1px solid #00C853;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧹 PR-Slop-Buster: AI Code Bloat & Dependency Auditor</div>', unsafe_allow_html=True)
st.markdown("""
<div class="sub-narrative">
<strong>The Reality of AI-Assisted Engineering in 2026:</strong><br>
Teams celebrated when Cursor, Claude Code, and Copilot tripled PR volume. Then reality hit: Senior and Staff engineers are drowning in review fatigue. When AI coding agents generate code without human constraints, they introduce <strong>four insidious failure modes</strong> that look plausible on the surface but poison production codebases.
</div>
""", unsafe_allow_html=True)

detector = PRSlopDetector()

nav_tab1, nav_tab2, nav_tab3 = st.tabs([
    "🔬 The 4 AI Failure Modes in Action",
    "⚡ Live PR Slop Auditor & Transformer",
    "💼 Engineering Burnout & ROI Calculator"
])

# =====================================================================
# TAB 1: THE 4 FAILURE MODES PLAYGROUND
# =====================================================================
with nav_tab1:
    st.subheader("Interactive Failure Mode Inspector")
    st.caption("Click any failure mode to see the code vulnerability AI introduces and how the Staff Engineer lens cures it.")

    mode = st.radio(
        "Select Failure Mode to Inspect:",
        [
            "1. 📦 Dependency Bloat (Importing 2MB libraries for 3-line utilities)",
            "2. 🧪 Tautological 'Fake' Tests (Mocks out everything and asserts nothing)",
            "3. 🏗️ Over-Engineered Boilerplate (300 lines of Factory classes for a simple function)",
            "4. 🦜 Parrot Comments & Ghost Noise (Echoes the code without architectural intent)"
        ],
        horizontal=False
    )

    f_col1, f_col2 = st.columns(2)

    if mode.startswith("1"):
        with f_col1:
            st.markdown('<div class="failure-box">', unsafe_allow_html=True)
            st.markdown("#### ❌ What AI Coding Agents Generate:")
            st.error("Imports external packages (`lodash`, `moment`) that bloat bundle sizes and create supply-chain CVE vulnerabilities.")
            st.code("""
import lodash from 'lodash';
import moment from 'moment';

export function getFormattedDate(d) {
    // Heavy 2MB moment library called for basic ISO formatting
    return moment(d).format('YYYY-MM-DD');
}

export function chunkList(arr, size) {
    // 70KB lodash package imported for basic array slicing
    return lodash.chunk(arr, size);
}
            """, language="typescript")
            st.markdown("</div>", unsafe_allow_html=True)

        with f_col2:
            st.markdown('<div class="cure-box">', unsafe_allow_html=True)
            st.markdown("#### ✅ How PR-Slop-Buster Cures It:")
            st.success("Replaces dependencies with native modern standard library APIs. Zero bundle bloat, zero dependencies.")
            st.code("""
// Zero dependencies: 100% native modern ES6+ APIs
export const getFormattedDate = (d: Date): string => 
    new Intl.DateTimeFormat('en-CA').format(d);

export const chunkList = <T>(arr: T[], size: number): T[][] =>
    Array.from({ length: Math.ceil(arr.length / size) }, (_, i) => 
        arr.slice(i * size, i * size + size));
            """, language="typescript")
            st.caption("🎉 Impact: -2.4MB node_modules payload eliminated, 0 supply-chain security surface.")
            st.markdown("</div>", unsafe_allow_html=True)

    elif mode.startswith("2"):
        with f_col1:
            st.markdown('<div class="failure-box">', unsafe_allow_html=True)
            st.markdown("#### ❌ What AI Coding Agents Generate:")
            st.error("Tautological 'fake' test that gives a false sense of test coverage while testing literally nothing.")
            st.code("""
describe('PaymentAuthService', () => {
    it('should authenticate payment transaction', () => {
        const mockAuth = jest.fn().mockReturnValue(true);
        const result = mockAuth();
        
        // TAUTOLOGY: Tests the mock itself, not production logic!
        expect(result).toBe(true);
        expect(true).toBe(true);
    });
});
            """, language="typescript")
            st.markdown("</div>", unsafe_allow_html=True)

        with f_col2:
            st.markdown('<div class="cure-box">', unsafe_allow_html=True)
            st.markdown("#### ✅ How PR-Slop-Buster Cures It:")
            st.success("Forces real assertional invariants against production state, input boundaries, and error rejection.")
            st.code("""
describe('PaymentAuthService', () => {
    it('authenticates valid ledger payload and rejects negative balances', async () => {
        const service = new PaymentAuthService();
        
        // Asserts real production business boundary validation
        await expect(service.authorize({ amount: -50 }))
            .rejects.toThrow('Invalid transaction amount');
            
        const auth = await service.authorize({ amount: 100, accountId: 'ACC-01' });
        expect(auth.transactionStatus).toBe('APPROVED');
    });
});
            """, language="typescript")
            st.caption("🎉 Impact: Real regression defense. Catches edge cases instead of rubber-stamping coverage.")
            st.markdown("</div>", unsafe_allow_html=True)

    elif mode.startswith("3"):
        with f_col1:
            st.markdown('<div class="failure-box">', unsafe_allow_html=True)
            st.markdown("#### ❌ What AI Coding Agents Generate:")
            st.error("Complex Abstract Factory and Singleton classes introduced for a simple 10-line calculation.")
            st.code("""
// Abstract base factory interface
abstract class AbstractDiscountCalculatorFactory {
    abstract createCalculator(): IDiscountCalculator;
}
class StandardDiscountCalculatorFactory extends AbstractDiscountCalculatorFactory {
    createCalculator(): IDiscountCalculator {
        return new DiscountCalculatorSingleton.getInstance();
    }
}
class DiscountCalculatorSingleton {
    private static instance: DiscountCalculatorSingleton;
    public static getInstance() {
        if (!this.instance) this.instance = new DiscountCalculatorSingleton();
        return this.instance;
    }
    public calculate(p: number, d: number) { return p * (1 - d); }
}
            """, language="typescript")
            st.markdown("</div>", unsafe_allow_html=True)

        with f_col2:
            st.markdown('<div class="cure-box">', unsafe_allow_html=True)
            st.markdown("#### ✅ How PR-Slop-Buster Cures It:")
            st.success("Decouples the over-engineering into a clean, testable pure function. Drops line count by 75%.")
            st.code("""
// Clean, idiomatic functional implementation
export const calculateDiscount = (price: number, discountRatio: number): number => {
    if (discountRatio < 0 || discountRatio > 1) {
        throw new RangeError('Discount ratio must be between 0.0 and 1.0');
    }
    return Math.round(price * (1 - discountRatio));
};
            """, language="typescript")
            st.caption("🎉 Impact: 32 lines reduced to 7 lines. Zero cognitive overhead for code reviewers.")
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        with f_col1:
            st.markdown('<div class="failure-box">', unsafe_allow_html=True)
            st.markdown("#### ❌ What AI Coding Agents Generate:")
            st.error("Parrot comments that explain the syntax verbatim while omitting architectural reasoning.")
            st.code("""
// function to get user
function getUser(userId) {
    // checks if userId exists
    if (!userId) {
        // returns null if no user
        return null;
    }
    // calls find user on database
    return db.findUser(userId);
}
            """, language="typescript")
            st.markdown("</div>", unsafe_allow_html=True)

        with f_col2:
            st.markdown('<div class="cure-box">', unsafe_allow_html=True)
            st.markdown("#### ✅ How PR-Slop-Buster Cures It:")
            st.success("Removes noise. Allows self-documenting code with meaningful architectural context to breathe.")
            st.code("""
/**
 * Retrieves authenticated user profile.
 * Falls back to null for unverified anonymous sessions.
 */
export const getUser = async (userId?: string): Promise<User | null> => {
    return userId ? await db.findUser(userId) : null;
};
            """, language="typescript")
            st.caption("🎉 Impact: Clean documentation. Reviewers read intent rather than redundant noise.")
            st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# TAB 2: LIVE PR AUDITOR & TRANSFORMER
# =====================================================================
with nav_tab2:
    st.subheader("Live Code Auditor & Transformer")
    st.caption("Paste any AI-generated PR diff to compute the Slop Index and generate an automated Staff Engineer review.")

    c1, c2 = st.columns(2)

    with c1:
        pr_id_input = st.text_input("Pull Request ID", "PR-CORE-1048")
        
        sample_code_raw = (
            "import lodash from 'lodash';\n"
            "import moment from 'moment';\n\n"
            "// Abstract factory pattern for simple user formatting\n"
            "class UserFormatterFactory {\n"
            "    createFormatter() {\n"
            "        return new UserFormatter();\n"
            "    }\n"
            "}\n\n"
            "class UserFormatter {\n"
            "    // function to format user date\n"
            "    formatDate(date) {\n"
            "        return moment(date).format('YYYY-MM-DD');\n"
            "    }\n"
            "}\n\n"
            "// Unit tests\n"
            "test('should format user correctly', () => {\n"
            "    // Fake tautological assertion generated by AI\n"
            "    expect(true).toBe(true);\n"
            "});\n"
        )
        diff_text_area = st.text_area("Inspect Pull Request Diff / Generated Code", sample_code_raw, height=280)
        run_audit_btn = st.button("🚀 Audit for AI Slop & Transform", type="primary", use_container_width=True)

    with c2:
        if run_audit_btn:
            card = detector.audit_diff(pr_id_input, diff_text_area)

            st.markdown("### 📊 Slop Telemetry Scorecard")
            
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("AI Slop Index", f"{card.slop_index_score}%", delta="Critical Bloat" if card.slop_index_score >= 30 else "Clean", delta_color="inverse")
            with m2:
                st.metric("Lines Analyzed", f"{card.lines_analyzed} lines")
            with m3:
                st.metric("Line Reduction Potential", f"-{card.estimated_lines_prunable} lines", delta="Prunable Bloat")

            st.progress(card.slop_index_score / 100.0)

            if card.verdict == "CLEAN_READY_FOR_REVIEW":
                st.success(f"### ✅ {card.verdict}")
            else:
                st.error(f"### 🚨 {card.verdict}")

            st.info(f"💡 **Staff Architect Directive:** {card.minimalist_refactoring_advice}")

            st.divider()

            st.markdown("### 🔍 Specific Bloat Findings Caught")
            for f in card.findings:
                st.warning(f"**[{f.severity}] {f.category}:** {f.description}\n\n*Actionable Fix:* `{f.remediation}`")

            st.divider()

            st.markdown("### 💬 Automated GitHub PR Review Comment")
            comment_text = (
                f"### 🧹 PR-Slop-Buster Pre-Flight Audit (`{card.pr_id}`)\n\n"
                f"**Slop Index Score:** `{card.slop_index_score}%` | **Status:** `{card.verdict}`\n\n"
                f"**Violations to Resolve Before Human Review:**\n"
                + "\n".join([f"- **[{item.severity}] {item.category}:** {item.description}\n  ↳ *Fix:* {item.remediation}" for item in card.findings])
                + f"\n\n**Pruning Target:** Remove approximately {card.estimated_lines_prunable} lines of boilerplate.\n"
                f"\n_Generated automatically via PR-Slop-Buster._"
            )
            st.text_area("Copy-Paste into GitHub PR Review:", comment_text, height=130)

# =====================================================================
# TAB 3: REVIEWER BURNOUT & ROI CALCULATOR
# =====================================================================
with nav_tab3:
    st.subheader("Engineering Review Fatigue & Organizational ROI Model")
    st.caption("Quantifying senior engineering hours saved by eliminating AI code bloat before human review.")

    r1, r2 = st.columns(2)

    with r1:
        dev_count = st.slider("Active Software Engineers", min_value=10, max_value=500, value=80, step=10)
        prs_per_dev = st.slider("PRs Submitted per Developer per Week", min_value=1, max_value=10, value=4)
        review_mins_saved = st.slider("Review Time Saved per PR by Stripping Slop (Minutes)", min_value=5, max_value=45, value=20)
        senior_hourly_rate = st.slider("Average Senior Engineer Blended Rate ($/hr)", min_value=75, max_value=250, value=125, step=5)

    with r2:
        total_weekly_prs = dev_count * prs_per_dev
        total_monthly_prs = total_weekly_prs * 4
        hours_saved_monthly = round((total_monthly_prs * review_mins_saved) / 60, 1)
        dollars_saved_monthly = round(hours_saved_monthly * senior_hourly_rate, 2)
        annual_savings = round(dollars_saved_monthly * 12, 2)

        st.markdown("### 💰 Operational Return on Investment (ROI)")
        st.metric(
            label="Senior Reviewer Hours Saved Monthly",
            value=f"{hours_saved_monthly:,.0f} Hours",
            delta="Freed up for strategic architecture"
        )
        st.metric(
            label="Monthly Engineering Payroll Waste Avoided",
            value=f"${dollars_saved_monthly:,.2f}",
            delta=f"${annual_savings:,.2f} Annualized Value"
        )
        st.success(
            f"By filtering AI bloat before human code review, an engineering organization of **{dev_count} developers** "
            f"unlocks **{hours_saved_monthly:,.0f} hours** of senior engineering capacity every month."
        )
