import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# 1. SETUP
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Page Styling
st.set_page_config(page_title="MyTrip AI Agent", page_icon="🇮🇳", layout="wide")

st.title("🇮🇳 MYTRIP - DOMESTIC AGENT")
st.markdown("---")

# 2. UI LAYOUT: SIDEBAR FOR INPUTS
with st.sidebar:
    st.header("📍 Trip Configuration")
    source = st.text_input("Departing From", placeholder="e.g., Mumbai")
    dest = st.text_input("Destination City", placeholder="e.g., Kochi")
    
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", format="DD/MM/YYYY")
    with col2:
        end_date = st.date_input("End Date", format="DD/MM/YYYY")
        
    budget = st.number_input("Total Budget (INR)", min_value=1000, value=50000)
    people = st.number_input("Number of People", min_value=1, value=3)

    # Replicating your "Dropdown" logic
    mode = st.selectbox("Transportation Mode:", ["Flight", "Train", "Road (Self/Cab)"])
    
    # Conditional Trip Type (Same as your code)
    if mode != "Road (Self/Cab)":
        trip_type = st.radio("Trip Type:", ["Round Trip", "One Way"])
    else:
        trip_type = "One-Way"
        
    stay_pref = st.selectbox("Stay Preference:", ["Hotels", "Homestays", "Bungalows/Hostels", "Farmhouse"])

    generate_btn = st.button("Generate My Plan ✅", use_container_width=True)

# 3. MAIN AREA - LOGIC EXECUTION
if generate_btn:
    if not source or not dest:
        st.error("Please provide both Origin and Destination cities.")
    else:
        with st.status(f"📡 Analyzing {dest} constraints for {start_date}...", expanded=True) as status:
            
            # PHASE 1: FACT EXTRACTION (Compound Mini)
            st.write("Fetching 2026 domestic facts...")
            research_prompt = f"""
            Find 2026 domestic facts for {people} people: {source} to {dest}.
            1. PRICE CHECK: Current 2026 average cost for {mode} ({trip_type}).
            2. EVENT SCAN: Any Indian festivals, matches, or local holidays in {dest} during {start_date}-{end_date}.
            3. WEATHER: Specific monsoon/heat alert for {dest} in that month.
            """
            
            res_resp = client.chat.completions.create(
                model="groq/compound-mini",
                messages=[{"role": "user", "content": research_prompt}]
            )
            facts = res_resp.choices[0].message.content

            # PHASE 2: ARCHITECTURE (Llama 70B)
            st.write("Structuring your personalized itinerary...")
            planner_prompt = f"""
            FACTS: {facts}
            USER: {people} people, Budget ₹{budget}, Dates: {start_date}-{end_date}, Mode: {mode}, Stay: {stay_pref}.
            
            FORMAT:
            ### ⚠️ EVENT & WEATHER ALERT
            Highlight important local events or weather risks.
            
            ### ✈️ TRANSPORTATION (Selection)
            Best {mode} options for {people} people under budget.
            
            ### 🏨 STAY RECOMMENDATIONS
            3 options for {stay_pref} in a central neighborhood.
            
            ### 📍 REALISTIC ITINERARY
            - Every day starts and ends at the stay.
            - Include 1 'Feel Good' activity, 1 shopping spot, and 1 local restaurant per day.
            
            ### 💰 BUDGET SUMMARY (Estimation)
            Table of costs vs. Total Budget.
            """

            final_resp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a realistic domestic travel agent. No global fluff. Focus on INR, Indian neighborhoods, and realistic transit times."},
                    {"role": "user", "content": planner_prompt}
                ]
            )
            
            status.update(label="Planning Complete!", state="complete", expanded=False)

        # FINAL OUTPUT DISPLAY
        st.subheader("✅ YOUR CUSTOM DOMESTIC PLAN IS READY")
        st.markdown("---")
        st.markdown(final_resp.choices[0].message.content)

else:
    # Welcome message when the app loads
    st.info("👋 Welcome! Fill in your details on the left and click 'Generate' to create your stylish travel plan.")