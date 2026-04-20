import streamlit as st
import time


# App Configuration
st.set_page_config(page_title="For My Ghutnu", page_icon="❤️", layout="centered")
# Birthday Logic (21st April = 111th Day)
BIRTHDAY_DAY_OF_YEAR = 111
day_of_year = time.localtime().tm_yday

# --- CUSTOM CSS (Smooth Scroll & Design) ---
st.markdown("""
    <style>
    /* Background and Padding */
    .stApp { background-color: #fff0f3; }
    
    /* Scroll fix */
    .main .block-container { padding-top: 2rem; padding-bottom: 5rem; }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #ff4b6b;
        color: white;
        border: none;
        height: 3.5em;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    
    /* Birthday Box Styling */
    .bday-box {
        background: linear-gradient(45deg, #ff4b6b, #ff8e8e);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 5px 15px rgba(255, 75, 107, 0.4);
    }

    /* Custom Header for Mobile */
    .mobile-header {
        font-size: 24px;
        font-weight: bold;
        color: #ff4b6b;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. BIRTHDAY SURPRISE ---
if day_of_year == BIRTHDAY_DAY_OF_YEAR:
    st.balloons()
    st.markdown(f"""
    <div class="bday-box">
        <h1>🎂 Happy Birthday, My Love! 🎂</h1>
        <p style="font-size: 18px;">
            Ekhane tomar boro message-ta likhe dao. <br>
            Tumi amar jibon-er shobcheye special manush! ❤️
        </p>
    </div>
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
    tabs = st.tabs(["M1", "M2", "M3", "M4", "M5", "M6","M7","M8","M9"])

    memories = [
        {"file": "photo1.jpg", "caption": "কপাল পোড়ার প্রথম ধাপ,দিনটা কবে  তুমি  বলবে 😉✨..."},
        {"file": "photo2.jpg", "caption": "যত কাণ্ড  বেহালাতে!"},
        {"file": "photo3.jpg", "caption": "ছলচাতুরিতে বশীকরণ"},
        {"file": "photo4.jpg", "caption": "ভয় জয় করে এক নিরীহ হরিণ শিশুর বাঘের ডেরায় হাজিরা! 🦌🐅"},
        {"file": "photo5.jpg", "caption": "সেই কুইন অফ হিলসের কোলে হাজারো রোমান্স আর মিষ্টি বকাঝকার সাতকাহন শেষে, এই অক্টোবরে কি তবে ভাইজাগ নয়, অন্য কোনো রহস্যময় ডেরায় জমবে  জীবনের সেরা ঝকঝকে মহরত?✨"},
        {"file": "photo6.jpg", "caption": "Ghutnu রানী, বড়ই সেয়ানি! 👑✨🥰"},
        {"file": "photo7.jpg", "caption": "আমরা দুজনে একসাথে থাকা মানেই মোহুনবাগানের জয় নিশ্চিত, তাই লক্ষ্মীটি হয়ে থাকো—আমার সাথে একদম No ঝগড়া!💚🏹❤️"},
        {"file": "photo8.jpg", "caption": "লাভ ইউ ওয়ালি বেস্ট ফ্রেন্ড আর সবার ছবি দিয়ে একটা কোলাজ ...ওনাকে তোমার মনের মণিকোঠায় খুব যত্ন করে রেখে দিও... আর বাকিদের জন্য রইল আমার অনেকটা ভালোবাসা! ❤️✨"},
        {"file": "photo9.jpg","caption":  "অবশেষে বলি, আমার সাথে চল একটু পথ যদি চাস... ভালো থাকিস খুব মাগি! ❤️✨"}
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
        "গুগল বলছিল বড্ড বেশি ভালো ভালো কথা লিখতে, কিন্তু আমার কলমে তো অত ভালো মানুষী আসে না!  জন্মদিনটা দারুণ ভাবে কাটা। পঁয়ত্রিশ মানে কিন্তু বুড়ো হয়ে গেছ! এবার সল্টলেক স্টেডিয়ামে বিয়ে করে মেসোর স্বপ্নটা পূরণ করে ফেলো। নাহলে অদূর ভবিষ্যতে সব দাঁত পড়ে যাবে, তখন কিন্তু আর কচি পাঁঠার মাংস চিবোতে পারবে না, আর কোনো মেয়ের... ও না, থাক!জনমদিন মুবারক জনাব!খুব ভালো থেকো। যতদিন আছি, এভাবেই রোজ তোমাকে জ্বালিয়ে যাব। আর সাবধান! ফোন থেকে এই অ্যাপটা কিন্তু ওড়াবে না একদম!Open it Daily for a surprise foronly 1 week",
        "Ei to mone kore esechis!!! already missing me naki!!",
        "roj sokale brush korbi",
        "kibhabe jalabo vabchi..notun notun technique",
        "vabchilam,365 days i jalabo. seta ar korbona..roj app khulte miss korchis tui..jai Hk... Vote dite sabdhane jabi",
        "Joy Mohunbagan!! O na.khela picholo to..Vote er din jindaaaaabaad",
        "Amar kothati furolo..note gach ti murolo..Love you Ghutnu.."
        "Ar pabina amay kal theke..r khulteo hobena app ta..enjoy your life magi..Tata"
        
    ]
    current_note = notes[day_of_year % len(notes)]
    st.info(current_note)
    st.write("---")
    st.caption("প্রতিদিন ঠিক দুপুর ১২টায় মেসেজ আসবে, তাই রোজ অ্যাপ খুলবি। ভুলে গেলে কিন্তু গাট্টা খাবি! আমার এই খাটনি যেন বিফলে না পাঠাস Ghutun... 👊💥")

# Option 3: Personalized Quiz
elif option == "3. চেনা মুখুজ্যে বামনের পৈতে টেস্ট":
    st.header("🧠 The Quiz")
    score = 0
    
    q1 = st.radio("আমাদের প্রথম বড় বয়সে মোলাকাতের দিন তোর প্রথম প্রশ্নটা কী ছিল?", ["এই বোরিং জিনিসটা কতক্ষণ চলবে?", "তোর কতগুলো বয়ফ্রেন্ড?"])
    if q1 == "এই বোরিং জিনিসটা কতক্ষণ চলবে?": # Answer change kore nio
        st.write("😘 উলি-বাবা-লে পুচু পুচু... তুই মনে রেখেছিস!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 🥺✨")
        score += 1
    elif q1 is not None:
        st.write("😡বাহ্!!! এটা ভুল করলি!!! গরু!! ছাগল!!! এইজন্যই বলি তুমি আমায় একটুও ভালোবাসো না। শুধুই বেস্ট ফ্রেন্ড... লাভ ইউ ওয়ালি তোমার চোখের মণি! 😤🙄")

    # Question 2
    q2 = st.radio("2. ঐ দিনটার তারিখ কত বল দেখি? আর আমি কী রঙের জামা পরেছিলাম!! এটা যদি ভুল করিস, তবে কিন্তু লাঁশ ফেলে দেব... একদম সাবধান!", ["২৬শে আগস্ট, সাদা", "২৭শে আগস্ট, সাদা", "২৬শে আগস্ট, লাল","২৭শে আগস্ট, লাল"], index=None)
    if q2 == "২৬শে আগস্ট, লাল":
        st.write("😘 যাক, এ যাত্রা বেঁচে গেলি তুই...")
        score += 1
    elif q2 is not None:
        st.write("😡 বাহ্ খুব ভালো!I hate you!🙄✨")

    # Question 3
    q3 = st.radio("3.আমার পছন্দের কাজ কী বল তো?", ["তোকে জ্বালানো", "তোর সাথে ঘুরতে বেরোনো", "তোর সাথে সিনেমা দেখা","আর তোর সাথে খেতে যাওয়া"], index=None)
    if q3 == "তোকে জ্বালানো": # Swap if you like beaches!
        st.write("😘 Correct! বুঝে গেছিস দেখছি আমার আসল মতলবটা কী!")
        score += 1
    elif q3 is not None:
        st.write("সরি সোনা... তবে আমার কাছে তোকে জ্বালানোর চেয়ে বড় ইম্পর্ট্যান্ট কাজ আর কিচ্ছুটি নেই!😜🔥✨")

    # Question 4
    q4 = st.radio("4. আমার GPay পেমেন্ট পিন কী বল তো?😉🔐", ["212369","210499","639179"], index=None)
    if q4 == "639179":
        st.write("😘এটা কী করে জানলি!!!!!!!! উফফ্‌ Pompuuuuuuuuuuuuu Pompuuuuuuuuuuuuuuuuuuuu।🤯✨")
        score += 1
    elif q4 is not None:
        st.write("😡 উহুহুহুহুউউউউউ... সব কিছুতেই তুই থাকবি নাকি Baal!! যা, তোর ওই ওয়েভলেংথ ম্যাচকারিণীর কাছে... হুহ্‌!🙄💅✨")

    # Question 5
    q5 = st.radio("5. আমাদের দুজনের একসাথে দেখা প্রথম মোহুনবাগানের ম্যাচ কোনটা?? এটা কিন্তু তোর পারা উচিত!", ["MBSG vs Kerala", "CMBSG vs FC Goa", "MBSG vs Bangalore"], index=None)
    if q5 == "MBSG vs Bangalore":
        st.write("😘 জানতাম তুই পারবি এটা.. জয় মোহুনবাগান!💚🏹❤️")
        score += 1
    elif q5 is not None:
        st.write(" এ কী!!! এটা ভুললি কী করে!!! আপনার বেস্ট ফ্রেন্ড ছিলেন যে-ই-ই-ই-ই-ই-ই-ই-ই...!😱🤯✨")

    # Question 6
    q6 = st.radio("6. ফাইনাল প্রশ্ন... আর জ্বালাবো না... একা একাই থাকবি তাহলে, নাকি আমার সাথে থাকবি!! কী ঠিক করলি অবশেষে!!", ["একা একা থাকবো...", "তোর সাথেই থাকবো।"], index=None)
    if q6 == "তোর সাথেই থাকবো।":
        st.write("😘 তাহলে থেকে যা না হয় আমার সাথেই!ভালো করে পোড়া রান্না করে, সারাক্ষণ জ্বালিয়ে আর খুব যত্নে আগলে রেখে, মাসি,মেসোকে এক্কেবারে পাকড়াও করে নিজের কাছেই রেখে দেব!🍳📚🔒✨😉💅✨")
        score += 1
    elif q6 is not None:
        st.write("😡 যা খুশি কর, পানা পুকুরে মাছের কামড় kha!")

    st.divider()
    if st.button("Submit My Final Score"):
        if score == 6:
            st.success(f"Perfect 6/6! A birthday Score!!❤️")
            st.balloons()
        else:
            st.warning(f"Tomar score {score}/6.Huhh!! jaihok..jonmodin bole chere dilum..😂")
