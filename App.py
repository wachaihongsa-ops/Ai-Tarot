import streamlit as st
import random

st.set_page_config(
    page_title="AI Tarot",
    page_icon="🔮"
)

cards = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World"
]

st.title("🔮 AI Tarot")

topic = st.selectbox(
    "เลือกหัวข้อที่ต้องการดูดวง",
    ["การงาน", "การเงิน", "ความรัก"]
)

if st.button("🎴 Draw Card"):

    card = random.choice(cards)

    st.success(f"ไพ่ที่ได้: {card}")

    st.write("## 🔮 คำทำนาย")

    if card == "The Sun":

        st.markdown("""
### 🌞 The Sun

#### 💼 การงาน
- มีโอกาสได้รับข่าวดี
- งานที่กำลังทำมีแนวโน้มสำเร็จ
- ได้รับการยอมรับจากคนรอบข้าง

#### 💰 การเงิน
- รายได้ดีขึ้น
- มีโอกาสได้รับผลตอบแทนที่ดี

#### ❤️ ความรัก
- ความสัมพันธ์สดใส
- มีความชัดเจนมากขึ้น

#### ✅ คำแนะนำ
ใช้ความมั่นใจและพลังบวกให้เต็มที่
""")

    elif card == "The Moon":

        st.markdown("""
### 🌙 The Moon

#### 💼 การงาน
- มีเรื่องที่ยังไม่ชัดเจน
- ควรตรวจสอบข้อมูลให้ละเอียด

#### 💰 การเงิน
- ระวังค่าใช้จ่ายที่ไม่คาดคิด

#### ❤️ ความรัก
- อย่ารีบด่วนสรุปสถานการณ์

#### ✅ คำแนะนำ
ใช้สติและความรอบคอบ
""")

    elif card == "The Star":

        st.markdown("""
### ⭐ The Star

#### 💼 การงาน
- มีโอกาสใหม่เข้ามา
- ความหวังเริ่มเป็นจริง

#### 💰 การเงิน
- แนวโน้มดีขึ้นเรื่อย ๆ

#### ❤️ ความรัก
- ความสัมพันธ์มีพัฒนาการ

#### ✅ คำแนะนำ
เชื่อมั่นในตัวเอง
""")

    elif card == "The Fool":

        st.markdown("""
### 🃏 The Fool

#### 💼 การงาน
- เหมาะกับการเริ่มต้นใหม่
- กล้าลองสิ่งที่ไม่เคยทำ

#### 💰 การเงิน
- มีโอกาสใหม่เกิดขึ้น

#### ❤️ ความรัก
- เปิดใจรับสิ่งใหม่

#### ✅ คำแนะนำ
ออกจาก Comfort Zone
""")

    else:

        st.markdown(f"""
### 🔮 {card}

#### 💼 การงาน
มีโอกาสเกิดการเปลี่ยนแปลงหรือบทเรียนใหม่

#### 💰 การเงิน
ควรวางแผนการใช้จ่ายอย่างรอบคอบ

#### ❤️ ความรัก
เปิดใจรับมุมมองใหม่ ๆ

#### ✅ คำแนะนำ
ใช้สติและไตร่ตรองก่อนตัดสินใจ
""")
