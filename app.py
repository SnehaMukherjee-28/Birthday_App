import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="For My Ghutan", page_icon="❤️")

# Custom CSS for look and feel
st.markdown("""
    <style>
    .main { background-color: #fff0f3; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b6b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Happy Birthday Ghutnu/Pom/Papu/Pappu/Anupam/Dudu dealer/Badshah Dajjal! ❤️")
st.subheader("তোর জন্য একটা বিশেষ উপহার...")

# Main Menu (Tinte Option)
option = st.radio("Choose an option to start:", ["1. আমাদের খিচুড়ি", "2.রোজনামচায় ঘুম-তাড়ানি", "3. চেনা মুখুজ্যে বামনের পৈতে টেস্ট"])

st.divider()

# Option 1: Memory Book (Slider style using Tabs)
if option == "1. আমাদের খিচুড়ি":
    st.header("📸 আমাদের ঝ্যাঁকন্যাকা সাতকাহন")
    st.write("আমাদের বিশেষ মুহূর্তে টেপ আরওওওওওওওওওওওও জোড়ে 😜, r ওপাশটাতে সরাও তো একটু!:")

    # 6-ta tab banano hochhe
    tabs = st.tabs(["M1", "M2", "M3", "M4", "M5", "M6","M7","M8"])

    memories = [
        {"file": "photo1.jpg", "caption": "কপাল পোড়ার প্রথম ধাপ,দিনটা কবে  তুমি  বলবে 😉✨..."},
        {"file": "photo2.jpg", "caption": "Aযত কাণ্ড  বেহালাতে!"},
        {"file": "photo3.jpg", "caption": "ছলচাতুরিতে বশীকরণ"},
        {"file": "photo4.jpg", "caption": "ভয় জয় করে এক নিরীহ হরিণ শিশুর বাঘের ডেরায় হাজিরা! 🦌🐅"},
        {"file": "photo5.jpg", "caption": "সেই কুইন অফ হিলসের কোলে হাজারো রোমান্স আর মিষ্টি বকাঝকার সাতকাহন শেষে, এই অক্টোবরে কি তবে ভাইজাগ নয়, অন্য কোনো রহস্যময় ডেরায় জমবে  জীবনের সেরা ঝকঝকে মহরত?✨"},
        {"file": "photo6.jpg", "caption": "Ghutnu রানী, বড়ই সেয়ানি! 👑✨🥰"},
        {"file": "photo7.jpg", "caption": "আমরা দুজনে একসাথে থাকা মানেই মোহুনবাগানের জয় নিশ্চিত, তাই লক্ষ্মীটি হয়ে থাকো—আমার সাথে একদম No ঝগড়া!💚🏹❤️"},
        {"file": "photo8.jpg", "cঅবশেষে বলি, আমার সাথে চল একটু পথ যদি চাস... ভালো থাকিস খুব গি! ❤️✨"}
    ]

    # Prottekta tab-er bhetore ekta kore image r caption
    for i, tab in enumerate(tabs):
        with tab:
            try:
                st.image(memories[i]["file"], use_container_width=True)
                st.subheader(memories[i]["caption"])
            except:
                st.warning(f"{memories[i]['file']} upload kora hoyni ekhono.")


# Option 2: Daily Love Notes
elif option == "2. রোজনামচায় ঘুম-তাড়ানি":
    st.header("💌 একদিন প্রতিদিন")
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
