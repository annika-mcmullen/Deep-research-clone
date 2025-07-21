import streamlit as st
import json
import itertools
from dotenv import load_dotenv
import os
from research_engine import DeepResearchEngine

# Load environment variables
load_dotenv()

# Initialize research engine
research_engine = DeepResearchEngine()

def initialize_session_state():
    """Initialize session state variables"""
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 'topic_input'
    if 'topic' not in st.session_state:
        st.session_state.topic = ''
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    if 'goal' not in st.session_state:
        st.session_state.goal = ''
    if 'queries' not in st.session_state:
        st.session_state.queries = []
    if 'collected_data' not in st.session_state:
        st.session_state.collected_data = []
    if 'final_report' not in st.session_state:
        st.session_state.final_report = ''

def get_clarifying_questions(topic):
    """Get 5 clarifying questions from OpenAI"""
    return research_engine.get_clarifying_questions(topic)

def get_goal_and_queries(topic, answers, questions):
    """Get research goal and search queries"""
    return research_engine.get_goal_and_queries(topic, answers, questions)

def run_search(query):
    """Run a web search for a given query"""
    return research_engine.run_search(query)

def evaluate_collected_data(collected_data, goal):
    """Evaluate if collected data satisfies the research goal"""
    return research_engine.evaluate_collected_data(collected_data, goal)

def generate_final_report(collected_data, goal):
    """Generate the final research report"""
    return research_engine.generate_final_report(collected_data, goal)

def main():
    st.set_page_config(
        page_title="Deep Research Clone",
        page_icon="🔍",
        layout="wide"
    )
    
    st.title("🔍 Deep Research Clone")
    st.markdown("An AI-powered research assistant that conducts comprehensive web research")
    
    initialize_session_state()
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        st.error("⚠️ Please set your OPENAI_API_KEY in the .env file")
        st.stop()
    
    # Step 1: Topic Input
    if st.session_state.current_step == 'topic_input':
        st.header("Step 1: Research Topic")
        st.write("Enter the topic you want to research:")
        
        topic = st.text_input("Research Topic:", value=st.session_state.topic)
        
        if st.button("Start Research") and topic:
            st.session_state.topic = topic
            st.session_state.questions = get_clarifying_questions(topic)
            st.session_state.current_step = 'questions'
            st.rerun()
    
    # Step 2: Answer Questions
    elif st.session_state.current_step == 'questions':
        st.header("Step 2: Clarifying Questions")
        st.write("Please answer these questions to help us understand your research needs:")
        
        answers = []
        for i, question in enumerate(st.session_state.questions):
            answer = st.text_input(f"Question {i+1}:", value=question, key=f"q{i}")
            if answer and answer != question:  # Don't include the question text as answer
                answers.append(answer)
        
        if len(answers) == len(st.session_state.questions):
            if st.button("Continue to Research"):
                st.session_state.answers = answers
                goal_queries = get_goal_and_queries(st.session_state.topic, answers, st.session_state.questions)
                st.session_state.goal = goal_queries["goal"]
                st.session_state.queries = goal_queries["queries"]
                st.session_state.current_step = 'research'
                st.rerun()
    
    # Step 3: Research
    elif st.session_state.current_step == 'research':
        st.header("Step 3: Conducting Research")
        st.write(f"**Research Goal:** {st.session_state.goal}")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Conduct initial searches
        collected_data = []
        for i, query in enumerate(st.session_state.queries):
            status_text.text(f"Searching: {query}")
            result = run_search(query)
            if result:
                collected_data.append(result)
            progress_bar.progress((i + 1) / len(st.session_state.queries))
        
        # Evaluate if we have enough data
        if evaluate_collected_data(collected_data, st.session_state.goal):
            st.session_state.collected_data = collected_data
            st.session_state.current_step = 'report'
            st.success("✅ Research completed! Generating report...")
            st.rerun()
        else:
            st.warning("⚠️ Need more research data. Conducting additional searches...")
            # Add more searches logic here
            st.session_state.collected_data = collected_data
            st.session_state.current_step = 'report'
            st.rerun()
    
    # Step 4: Final Report
    elif st.session_state.current_step == 'report':
        st.header("Step 4: Research Report")
        
        if not st.session_state.final_report:
            with st.spinner("Generating final report..."):
                st.session_state.final_report = generate_final_report(
                    st.session_state.collected_data, 
                    st.session_state.goal
                )
        
        st.markdown(st.session_state.final_report)
        
        # Download button
        st.download_button(
            label="📥 Download Report",
            data=st.session_state.final_report,
            file_name=f"research_report_{st.session_state.topic.replace(' ', '_')}.md",
            mime="text/markdown"
        )
        
        if st.button("🔄 Start New Research"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main() 