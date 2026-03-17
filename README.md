# ✈️ MyTrip: The 0-API AI Travel Agent

So, I wanted to see if I could build a full-scale travel agent without using any external APIs (no Google Maps, no Skyscanner, nothing). Just the raw reasoning power of Groq’s models. Turns out, you can. 

This is a **Mini-MMT (MakeMyTrip)** built entirely on logic. It doesn't just "chat"; it plans, budgets, and thinks through the logistics of Indian travel.

## 🧠 Why Groq & The Two-Model Strategy?
I used a "Compound AI" approach by splitting the brain into two parts:

1. **Phase 1: The Researcher (Groq Compound Mini)**
   - **The Job:** Fact extraction.
   - **The Insight:** This model is super fast and focused. It pulls the "ground truth"—weather patterns (like the 2026 monsoon), holiday dates, and realistic price ranges for flights and stays in India.

2. **Phase 2: The Architect (Llama 3.3 70B)**
   - **The Job:** Logic & Constraint Satisfaction.
   - **The Insight:** This is the heavy lifter. It takes the facts from Phase 1 and does the "mental math." It makes sure the plan is actually possible within a ₹50,000 budget and builds a circular itinerary so you aren't wasting time in traffic.

## 🚀 How it works (and why it's useful)
- **Zero Latency:** No waiting for third-party APIs to respond. It's near-instant.
- **Internal World Model:** The agent "knows" Indian geography. It understands that "Christmas in Goa" means "Everything gets expensive."
- **Future Ready:** This can easily be scaled to include a "Booking Agent" phase or live flight tracking later on.

## 🛠️ Setup (Important!)
**Note:** I have deleted my `.env` file for security (obviously!). To run this:
1. Create a `.env` file in the root folder.
2. Add your own Groq API Key: `GROQ_API_KEY=your_key_here`
3. Install requirements: `pip install -r requirements.txt`
4. Run it: `streamlit run app.py`
