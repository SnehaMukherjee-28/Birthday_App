import streamlit as st
import time

# --- CONFIGURATION (Mobile Friendly) ---
st.set_page_config(page_title="For My Ghutnu", page_icon="❤️", layout="centered")

# Birthday Logic (21st April = 111th Day)
BIRTHDAY_DAY_OF_YEAR = 111
day_of_year = time.localtime().tm_yday

# --- CUSTOM CSS (Final Fix: No Garbage Text & No Squished Images) ---
# --- CLEAN & COMPACT CSS ---
st.markdown("""
    <style>
    /* 1. Header r extra padding muche fela */
    header, footer { visibility: hidden !important; height: 0px !important; }
    
    .main .block-container {
        padding-top: 1rem !important;    /* Mathay khub chotto gap */
        padding-bottom: 2rem !important;
        max-width: 100% !important;
    }

    /* 2. Scrolling & Refresh Fix (Most Important) */
    html, body, [data-testid="stAppViewContainer"] {
        overscroll-behavior-y: contain !important; /* Pull-to-refresh bondho korbe */
        background-color: #fff0f3 !important;
    }

    /* 3. Gap komanon element-er majhkane */
    [data-testid="stVerticalBlock"] > div {
        gap: 0.5rem !important;
        margin: 0 !important;
    }

    /* 4. Selectbox/Menu (No Blank/Black Issue) */
    div[data-baseweb="select"] > div {
        background-color: #fff9db !important;
        color: #5e001f !important;
        border: 2px solid #ff4b6b !important;
        height: 3rem !important;
    }

    /* 5. Chobi-r aspect ratio fix */
    [data-testid="stImage"] img {
        max-height: 250px !important; 
        object-fit: contain !important;
        border-radius: 12px;
        border: 2px solid #ff4b6b !important;
    }

    /* 6. Text color fix */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #5e001f !important;
        line-height: 1.2 !important;
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

# --- 2. MAIN HEADER (Visible to User) ---
st.markdown('<div class="mobile-header">❤️ For My Ghutan ❤️</div>', unsafe_allow_html=True)
st.subheader("তোর জন্য একটা বিশেষ উপহার...")
st.write("---")

# --- 3. NAVIGATION MENU (selectbox based for mobile-friendly scrolling) ---
# Radio inside sidebar often stuck on mobile. Selectbox in main is better.
option = st.selectbox("Choose an option to start:", 
                      ["1. আমাদের খিচুড়ি", "2. রোজনামচায় ঘুম-তাড়ানি", "3. চেনা মুখুজ্যে বামনের পৈতে টেস্ট"])

st.divider()

# # --- OPTION 1: MEMORY BOOK (Manual Slide) ---
if option == "1. আমাদের খিচুড়ি":
    st.markdown("### 📸 আমাদের ঝ্যাঁকন্যাকা সাতকাহন")
    
    memories = [
        {"file": "photo1.jpg", "caption": "কপাল পোড়ার প্রথম ধাপ, দিনটা কবে তুমি বলবে 😉✨..."},
        {"file": "photo2.jpg", "caption": "যত কাণ্ড বেহালাতে!"},
        {"file": "photo3.jpg", "caption": "ছলচাতুরিতে বশীকরণ"},
        {"file": "photo4.jpg", "caption": "ভয় জয় করে এক নিরীহ হরিণ শিশুর বাঘের ডেরায় হাজিরা!🦌🐅"},
        {"file": "photo5.jpg", "caption": "সেই কুইন অফ হিলসের কোলে হাজারো রোমান্স আর মিষ্টি বকাঝকার সাতকাহন শেষে, এই অক্টোবরে কি তবে ভাইজাগ!! অন্য কোনো রহস্যময় ডেরায়!! জমবে আমাদের জীবনের সেরা ঝকঝকে মহরত? 🏔️❤️"},
        {"file": "photo6.jpg", "caption": "Ghutnu রানী, বড়ই সেয়ানি! 👑✨🥰"},
        {"file": "photo7.jpg", "caption": "আমরা দুজনে একসাথে থাকা মানেই মোহুনবাগানের জয় নিশ্চিত, তাই লক্ষ্মীটি হয়ে থাকো—আমার সাথে একদম কোনো ঝগড়া নয়! 💚🏹❤️"},
        {"file": "photo8.jpg", "caption": "তোমার ওই 'লাভ ইউ' ওয়ালি বেস্ট ফ্রেন্ড আর সবার ছবি দিয়ে একটা  কোলাজ !!, ওনাকে তোমার মনের মণিকোঠায় খুব যত্ন করে রেখে দিও... আর বাকিদের জন্য রইল আমার অনেকটা ভালোবাসা!"},
        {"file": "photo9.jpg", "caption": "অবশেষে বলি, আমার সাথে চল একটু পথ যদি চাস... ভালো থাকিস খুব magi!❤️✨"}
    ]

    # Session State to keep track of photo index
    if 'photo_index' not in st.session_state:
        st.session_state.photo_index = 0

    # Show Current Image
    current_img = memories[st.session_state.photo_index]
    st.image(current_img["file"], use_container_width=True)
    st.caption(current_img["caption"])

    # Slide Buttons (Side by Side)
    # Slide Buttons Side by Side (Horizontal space saving)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.photo_index = (st.session_state.photo_index - 1) % len(memories)
            st.rerun()
    with col2:
        if st.button("Next ➡️"):
            st.session_state.photo_index = (st.session_state.photo_index + 1) % len(memories)
            st.rerun()
    
    st.write(f"Moment {st.session_state.photo_index + 1} of {len(memories)}")


# --- 5. OPTION 2: DAILY LOVE NOTES ---
elif option == "2. রোজনামচায় ঘুম-তাড়ানি":
    st.header("💌 একদিন প্রতিদিন")
    notes = [
        "গুগল বলছিল বড্ড বেশি ভালো ভালো কথা লিখতে, কিন্তু আমার কলমে তো অত ভালো মানুষী আসে না!  জন্মদিনটা দারুণ ভাবে কাটা। পঁয়ত্রিশ মানে কিন্তু বুড়ো হয়ে গেছ! এবার সল্টলেক স্টেডিয়ামে বিয়ে করে মেসোর স্বপ্নটা পূরণ করে ফেলো। নাহলে অদূর ভবিষ্যতে সব দাঁত পড়ে যাবে, তখন কিন্তু আর কচি পাঁঠার মাংস চিবোতে পারবে না, আর কোনো মেয়ের... ও না, থাক!জনমদিন মুবারক জনাব!খুব ভালো থেকো। যতদিন আছি, এভাবেই রোজ তোমাকে জ্বালিয়ে যাব। আর সাবধান! ফোন থেকে এই অ্যাপটা কিন্তু ওড়াবে না একদম!Open it Daily for a surprise foronly 1 week",
        "Ei to mone kore esechis!!! already missing me naki!!",
        "roj sokale brush korbi",
        "kibhabe jalabo vabchi..notun notun technique",
        "vabchilam,365 days i jalabo. seta ar korbona..roj app khulte miss korchis tui..jai Hk... Vote dite sabdhane jabi",
        "Joy Mohunbagan!! O na.khela picholo to..Vote er din jindaaaaabaad",
        "Amar kothati furolo..note gach ti murolo..Love you Ghutnu..",
        "Ar pabina amay kal theke..r khulteo hobena app ta..enjoy your life magi..Tata"
    ]
    current_note = notes[day_of_year % len(notes)]
    st.info(current_note)
    st.write("---")
    # Small fix: Ghutun -> Ghutnu (consistency)
    st.caption("প্রতিদিন ঠিক দুপুর ১২টায় মেসেজ আসবে, তাই রোজ অ্যাপ খুলবি। ভুলে গেলে কিন্তু গাট্টা খাবি! আমার এই খাটনি যেন বিফলে না পাঠাস Ghutnu... 👊💥")

# --- 6. OPTION 3: PERSONALIZED QUIZ ---
elif option == "3. চেনা মুখুজ্যে বামনের পৈতে টেস্ট":
    st.header("🧠 The Quiz")
    score = 0
    
    # Q1
    q1 = st.radio("আমাদের প্রথম বড় বয়সে মোলাকাতের দিন তোর প্রথম প্রশ্নটা কী ছিল?", 
                  ["এই বোরিং জিনিসটা কতক্ষণ চলবে?", "তোর কতগুলো বয়ফ্রেন্ড?"], index=None)
    if q1 == "এই বোরিং জিনিসটা কতক্ষণ চলবে?":
        st.success("😘 উলি-বাবা-লে পুচু পুচু... তুই মনে রেখেছিস!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 🥺✨")
        score += 1
    elif q1 is not None:
        st.error("😡বাহ্!!! এটা ভুল করলি!!! গরু!! ছাগল!!! এইজন্যই বলি তুমি আমায় একটুও ভালোবাসো না। শুধুই বেস্ট ফ্রেন্ড... লাভ ইউ ওয়ালি তোমার চোখের মণি! 😤🙄")
    st.write("---")

    # Q2
    q2 = st.radio("2. ঐ দিনটার তারিখ কত বল দেখি? আর আমি কী রঙের জামা পরেছিলাম!! এটা যদি ভুল করিস, তবে কিন্তু লাঁশ ফেলে দেব... একদম সাবধান!", 
                  ["২৬শে আগস্ট, সাদা", "২৭শে আগস্ট, সাদা", "২৬শে আগস্ট, লাল","২৭শে আগস্ট, লাল"], index=None)
    if q2 == "২৬শে আগস্ট, লাল":
        st.success("😘 যাক, এ যাত্রা বেঁচে গেলি তুই...")
        score += 1
    elif q2 is not None:
        st.error("😡 বাহ্ খুব ভালো!I hate you!🙄✨")
    st.write("---")

    # Q3
    q3 = st.radio("3. আমার পছন্দের কাজ কী বল তো?", 
                  ["তোকে জ্বালানো", "তোর সাথে ঘুরতে বেরোনো", "তোর সাথে সিনেমা দেখা","আর তোর সাথে খেতে যাওয়া"], index=None)
    if q3 == "তোকে জ্বালানো":
        st.success("😘 Correct! বুঝে গেছিস দেখছি আমার আসল মতলবটা কী!")
        score += 1
    elif q3 is not None:
        st.error("😡 সরি সোনা... তবে আমার কাছে তোকে জ্বালানোর চেয়ে বড় ইম্পর্ট্যান্ট কাজ আর কিচ্ছুটি নেই!😜🔥✨")
    st.write("---")

    # Q4
    q4 = st.radio("4. আমার GPay পেমেন্ট পিন কী বল তো?😉🔐", 
                  ["212369","210499","639179"], index=None)
    if q4 == "639179":
        st.success("😘এটা কী করে জানলি!!!!!!!! উফফ্‌ Pompuuuuuuuuuuuuu Pompuuuuuuuuuuuuuuuuuuuu।🤯✨")
        score += 1
    elif q4 is not None:
        st.error("😡 উহুহুহুহুউউউউউ... সব কিছুতেই তুই থাকবি নাকি Baal!! যা, তোর ওই ওয়েভলেংথ ম্যাচকারিণীর কাছে... হুহ্‌!🙄💅✨")
    st.write("---")

    # Q5
    q5 = st.radio("5. আমাদের দুজনের একসাথে দেখা প্রথম মোহুনবাগানের ম্যাচ কোনটা?? এটা কিন্তু তোর পারা উচিত!", 
                  ["MBSG vs Kerala", "CMBSG vs FC Goa", "MBSG vs Bangalore"], index=None)
    if q5 == "MBSG vs Bangalore":
        st.success("😘 জানতাম তুই পারবি এটা.. জয় মোহুনবাগান!💚🏹❤️")
        score += 1
    elif q5 is not None:
        st.error("😡 এ কী!!! এটা ভুললি কী করে!!! আপনার বেস্ট ফ্রেন্ড ছিলেন যে-ই-ই-ই-ই-ই-ই-ই-ই...!😱🤯✨")
    st.write("---")

    # Q6
    q6 = st.radio("6. ফাইনাল প্রশ্ন... আর জ্বালাবো না... একা একাই থাকবি তাহলে, নাকি আমার সাথে থাকবি!! কী ঠিক করলি অবশেষে!!", 
                  ["একা একা থাকবো...", "তোর সাথেই থাকবো।"], index=None)
    if q6 == "তোর সাথেই থাকবো।":
        st.success("😘 তাহলে থেকে যা না হয় আমার সাথেই!ভালো করে পোড়া রান্না করে, সারাক্ষণ জ্বালিয়ে আর খুব যত্নে আগলে রেখে, মাসি,মেসোকে এক্কেবারে পাকড়াও করে নিজের কাছেই রেখে দেব!🍳📚🔒✨😉💅✨")
        score += 1
    elif q6 is not None:
        st.error("😡 যা খুশি কর, পানা পুকুরে মাছের কামড় kha!")

    st.divider()
    if st.button("Submit My Final Score"):
        if score == 6:
            st.balloons()
            st.success(f"Perfect 6/6! A birthday Score!!❤️")
        else:
            # Score warning fix
            st.warning(f"Tomar score {score}/6. Huhh!! jaihok..jonmodin bole chere dilum..😂")

ei code tar modye kothay dhokabo ei code ta?
# --- OPTION 1 LOGIC ---
if option == "1. আমাদের খিচুড়ি":
    # Index check kora
    if 'photo_idx' not in st.session_state:
        st.session_state.photo_idx = 0
        
    current_memory = memories[st.session_state.photo_idx]
    
    # Chobi r caption pashapashi rakha
    st.image(current_memory["file"], use_container_width=True)
    st.markdown(f"<p style='text-align:center; font-style:italic;'>{current_memory['caption']}</p>", unsafe_allow_html=True)

    # Buttons in columns
    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅️ Previous"):
            st.session_state.photo_idx = (st.session_state.photo_idx - 1) % len(memories)
            st.rerun()
    with c2:
        if st.button("Next ➡️"):
            st.session_state.photo_idx = (st.session_state.photo_idx + 1) % len(memories)
            st.rerun()
