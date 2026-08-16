import streamlit as st
import json
import pandas as pd


# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="GenAR Safety Intelligence",
    page_icon="🧬",
    layout="wide"
)


# -----------------------------------------
# LOAD DATA
# -----------------------------------------

@st.cache_data
def load_data():
    with open("output/evidence.json", "r", encoding="utf-8") as file:
        evidence = json.load(file)

    with open("output/analysis_results.json", "r", encoding="utf-8") as file:
        analysis = json.load(file)

    with open("output/generated_report.md", "r", encoding="utf-8") as file:
        report = file.read()

    return evidence, analysis, report


evidence, analysis, report = load_data()


# -----------------------------------------
# HEADER
# -----------------------------------------

st.title("🧬 GenAR Safety Intelligence Platform")

st.markdown(
    """
    **AI Engineering Challenge | Pharmacovigilance & Safety Analytics**

    An evidence-driven system for analyzing Individual Case Safety Reports
    (ICSRs) and generating a structured Periodic Adverse Drug Experience
    Report (PADER).
    """
)

st.divider()


# -----------------------------------------
# SIDEBAR
# -----------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Case Analysis",
        "Reaction Analysis",
        "Trends",
        "Generated Report"
    ]
)


# -----------------------------------------
# OVERVIEW
# -----------------------------------------

if page == "Overview":

    st.header("Safety Dataset Overview")

    dataset = evidence["dataset_evidence"]
    case_data = evidence["case_evidence"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Records",
        dataset["total_rows"]
    )

    col2.metric(
        "Unique Safety Cases",
        dataset["total_unique_cases"]
    )

    col3.metric(
        "Serious Cases",
        case_data["serious_cases"]
    )

    col4.markdown("### Reporting Period")

    col4.write(
        f"{dataset['reporting_period']['start_date']}"
    )

    col4.write("to")

    col4.write(
        f"{dataset['reporting_period']['end_date']}"
    )

    st.divider()

    st.subheader("Project Workflow")

    st.code(
        """
Excel / ICSR Dataset
        ↓
Python Data Processing
        ↓
Safety Analytics
        ↓
Evidence Layer
        ↓
Automated PADER Report
        ↓
Safety Intelligence Dashboard
        """
    )

    st.info(
        "This platform performs descriptive analysis of the supplied "
        "pharmacovigilance dataset. Findings do not establish causality "
        "or incidence rates."
    )


# -----------------------------------------
# CASE ANALYSIS
# -----------------------------------------

elif page == "Case Analysis":

    st.header("Case & Patient Analysis")

    patient = evidence["patient_evidence"]

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Patient Sex Distribution")

        sex_data = pd.DataFrame(
            patient["sex_distribution"].items(),
            columns=["Sex", "Cases"]
        )

        st.bar_chart(
            sex_data.set_index("Sex")
        )

        st.dataframe(sex_data, use_container_width=True)

    with col2:

        st.subheader("Age Group Distribution")

        age_data = pd.DataFrame(
            patient["age_distribution"].items(),
            columns=["Age Group", "Cases"]
        )

        st.bar_chart(
            age_data.set_index("Age Group")
        )

        st.dataframe(age_data, use_container_width=True)

    st.divider()

    st.subheader("Geographic Distribution")

    country_data = pd.DataFrame(
        patient["top_countries"].items(),
        columns=["Country / Region", "Cases"]
    )

    st.bar_chart(
        country_data.set_index("Country / Region")
    )

    st.dataframe(country_data, use_container_width=True)


# -----------------------------------------
# REACTION ANALYSIS
# -----------------------------------------

elif page == "Reaction Analysis":

    st.header("Adverse Reaction Analysis")

    reactions = evidence["reaction_evidence"]

    st.subheader("Top Reported Reactions")

    reaction_data = pd.DataFrame(
        reactions["top_reactions"].items(),
        columns=["Reaction", "Reports"]
    )

    st.bar_chart(
        reaction_data.set_index("Reaction")
    )

    st.dataframe(reaction_data, use_container_width=True)

    st.divider()

    st.subheader("Reaction Outcomes")

    outcome_data = pd.DataFrame(
        reactions["outcome_distribution"].items(),
        columns=["Outcome", "Records"]
    )

    st.bar_chart(
        outcome_data.set_index("Outcome")
    )

    st.dataframe(outcome_data, use_container_width=True)


# -----------------------------------------
# TRENDS
# -----------------------------------------

elif page == "Trends":

    st.header("Monthly Safety Case Trend")

    trends = evidence["trend_evidence"]

    trend_data = pd.DataFrame(
        trends["monthly_case_counts"].items(),
        columns=["Month", "Cases"]
    )

    trend_data["Month"] = pd.to_datetime(
        trend_data["Month"]
    )

    trend_data = trend_data.sort_values("Month")

    st.line_chart(
        trend_data.set_index("Month")
    )

    st.dataframe(
        trend_data,
        use_container_width=True
    )

    st.info(
        "The chart represents the number of unique safety cases "
        "reported per month in the supplied dataset."
    )


# -----------------------------------------
# GENERATED REPORT + HUMAN REVIEW
# -----------------------------------------

elif page == "Generated Report":

    st.header("Automated PADER Report")

    st.markdown(report)

    st.divider()

    # -----------------------------------------
    # HUMAN REVIEW
    # -----------------------------------------

    st.header("Human Review & Approval")

    reviewer_name = st.text_input(
        "Reviewer Name"
    )

    review_comments = st.text_area(
        "Reviewer Comments"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Approve Report"):

            if reviewer_name.strip():

                st.success(
                    f"Report approved by {reviewer_name}"
                )

                if review_comments.strip():
                    st.info(
                        f"Reviewer Comments: {review_comments}"
                    )

            else:
                st.warning(
                    "Please enter the reviewer name before approval."
                )

    with col2:

        if st.button("Flag for Review"):

            st.warning(
                "Report has been flagged for additional review."
            )

            if review_comments.strip():
                st.info(
                    f"Reviewer Comments: {review_comments}"
                )

    st.divider()

    # -----------------------------------------
    # DOWNLOAD REPORT
    # -----------------------------------------

    st.download_button(
        label="Download Generated Report",
        data=report,
        file_name="Bisoprolol_PADER_Report.md",
        mime="text/markdown"
    )