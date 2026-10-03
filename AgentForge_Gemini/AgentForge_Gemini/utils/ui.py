import streamlit as st


def show_agent_status(statuses):
    st.subheader("🤖 AI Team")

    columns = st.columns(5)

    for column, (name, status) in zip(columns, statuses.items()):
        with column:
            icon = "🟢" if status == "Completed" else "🟡" if status == "Working" else "⚪"
            st.metric(name, f"{icon} {status}")


def show_debate(debate):
    st.subheader("⚔️ AI Debate")
    st.markdown(debate)


def show_final_plan(final_plan):
    st.subheader("🚀 Improved Startup Plan")
    st.markdown(final_plan)
