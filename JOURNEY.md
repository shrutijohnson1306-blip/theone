# 🛠️ The Build Journey: MyTrip AI Agent

### 📍 The Vision
The goal was simple but ambitious: Build a domestic travel agent for India that doesn't rely on a dozen different APIs. I wanted to see if I could use **pure reasoning** to handle budgets, seasonal weather, and local geography. No Google Maps, no Skyscanner—just the brain of the model.

### 🏗️ The Build Process
1.  **Architecture:** I designed a "Compound AI" system. Instead of one model doing everything, I used a **Researcher** to gather facts and an **Architect** to build the plan.
2.  **Constraint Logic:** The hardest part was the "Mental Math." Getting the AI to understand that ₹50,000 for 3 people during Christmas in Goa is a tight squeeze required deep prompt engineering to prioritize "Survival" (Flights/Stays) over "Luxury" (Shopping).
3.  **UI/UX:** I used Streamlit to keep it clean and fast, ensuring the user gets a "Ready-to-Go" itinerary in under 2 seconds.

### 🌋 The "Git" Battle
The biggest hurdle wasn't the code—it was the deployment! 
- I accidentally committed my `.env` file with my private Groq API key.
- GitHub's **Push Protection** (thankfully!) blocked it, but it created a "poisoned" history.
- I had to learn how to wipe a local Git history, set up a proper `.gitignore`, and force-push a clean timeline. 
- **The Lesson:** Always protect your secrets *before* the first commit!

### 🤖 The Brains Behind the App
* **Groq Compound Mini:** My "Grounding" model. It’s incredibly fast at retrieving semantic facts like flight price trends and 2026 holiday dates without getting distracted.
* **Llama 3.3 70B:** The "Decision Maker." This model's high-parameter count is why the agent can handle complex budgeting and geographic routing without making mistakes.

### 🎓 Key Learnings
- **Internal World Models:** High-end LLMs already "know" enough about the world to act as their own database for general planning.
- **Latency Matters:** By using Groq's LPU, I achieved speeds that make traditional API-based apps feel ancient.
- **Fail Fast:** The Git error taught me more about repository management than any tutorial ever could.

### 🔮 Future Goals
- **Self-Correction Loop:** Having the model "double-check" its own math before showing the output.
- **Personalized Styles:** Adding "Backpacker," "Luxury," or "Family" modes that change the logic of the recommendations.
- **Export to PDF:** A one-click button to turn the itinerary into a travel document.
