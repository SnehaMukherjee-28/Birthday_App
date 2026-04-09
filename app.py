import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="For My Love", page_icon="❤️")

# Custom CSS for look and feel
st.markdown("""
    <style>
    .main { background-color: #fff0f3; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b6b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Happy Birthday! ❤️")
st.subheader("Tomar jonno choto ekta gift...")

# Main Menu (Tinte Option)
option = st.radio("Choose an option to start:", ["1. Our Memory Book", "2. Daily Love Notes", "3. The 'How Well Do You Know Me' Quiz"])

st.divider()

# Option 1: Memory Book
if option == "1. Our Memory Book":
    st.header("📸 Our Memories")
    st.write("Click koro amader kichu special moments dekhte:")
    if st.button("Open Memory 1"):
        st.image("https://via.placeholder.com/400x300.png?text=Tomader+Chobi+1", caption="Sei prothom dekha...")
    if st.button("Open Memory 2"):
        st.write("Ekhane tumi tomader purono kothopokothon likhte paro!")

# Option 2: Daily Love Notes
elif option == "2. Daily Love Notes":
    st.header("💌 Daily Notes")
    notes = [
        "You are the best thing that ever happened to me!",
        "Tomar hashi-ta amar shobcheye favorite.",
        "I'm so proud of everything you do.",
        "Ajker din-ta khub bhalo katuk tomar!"
    ]
    # Ajker diner ekta random note dekhabe
    day_of_year = time.localtime().tm_yday
    current_note = notes[day_of_year % len(notes)]
    st.info(current_note)

# Option 3: Personalized Quiz
elif option == "3. The 'How Well Do You Know Me' Quiz":
    st.header("🧠 The Quiz")
    score = 0
    
    q1 = st.radio("Amader prothom kothay dekha hoyeche?", ["Park Street", "College Canteen", "Prinsep Ghat"])
    if q1 == "Prinsep Ghat": # Answer change kore nio
        score += 1
        
    q2 = st.radio("Amar favorite khabar ki?", ["Biryani", "Phuchka", "Chanar Dalna"])
    if q2 == "Chanar Dalna": # Answer change kore nio
        score += 1
        
    if st.button("Submit Quiz"):
        st.success(f"Tomar score: {score}/2")
        if score == 2:
            st.balloons()
            st.write("Tumi sotti amake khub bhalo jano! ❤️")
