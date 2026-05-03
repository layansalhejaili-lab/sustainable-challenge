import streamlit as st

# -----------------------
# إعداد الصفحة
# -----------------------
st.set_page_config(page_title="تحدي التقنية المستدامة", page_icon="🌱", layout="centered")

# -----------------------
# تنسيق CSS
# -----------------------
st.markdown("""
<style>
body {
    direction: rtl;
}
.main {
    background-color: #f5f7f6;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    border: 2px solid #e0e0e0;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}
.title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: #2e7d32;
}
.points {
    text-align: center;
    font-size: 18px;
    margin-bottom: 10px;
}
.question {
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
}
.task {
    font-size: 20px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# البيانات
# -----------------------
tasks = [
    {
        "day": "اليوم 1",
        "task": "🔌 افصل الشواحن غير المستخدمة",
        "question": "هل ترك الشاحن في الكهرباء بدون استخدام يوفر طاقة؟",
        "options": ["نعم", "لا"],
        "correct": "لا",
        "points": 20,
        "explanation": "ترك الشاحن موصولًا قد يستهلك كمية بسيطة من الطاقة حتى بدون استخدام، لذلك الأفضل فصله."
    },
    {
        "day": "اليوم 2",
        "task": "💡 فعّل وضع توفير الطاقة",
        "question": "هل وضع توفير الطاقة يقلل استهلاك البطارية؟",
        "options": ["نعم", "لا"],
        "correct": "نعم",
        "points": 20,
        "explanation": "وضع توفير الطاقة يقلل من استهلاك البطارية عن طريق تقليل بعض العمليات في الخلفية."
    },
    {
        "day": "اليوم 3",
        "task": "📱 احذف التطبيقات غير الضرورية",
        "question": "هل حذف التطبيقات يحسن أداء الجهاز؟",
        "options": ["نعم", "لا"],
        "correct": "نعم",
        "points": 20,
        "explanation": "حذف التطبيقات غير الضرورية يوفّر مساحة وقد يساعد في تحسين أداء الجهاز."
    },
    {
        "day": "اليوم 4",
        "task": "🔐 غيّر كلمة مرور ضعيفة",
        "question": "هل كلمة المرور 123456 آمنة؟",
        "options": ["نعم", "لا"],
        "correct": "لا",
        "points": 20,
        "explanation": "كلمة المرور 123456 ضعيفة جدًا وسهلة التخمين، لذلك يجب استخدام كلمة مرور قوية."
    },
    {
        "day": "اليوم 5",
        "task": "♻️ أعد تدوير جهاز إلكتروني قديم",
        "question": "هل يجب حذف البيانات قبل إعادة التدوير؟",
        "options": ["نعم", "لا"],
        "correct": "نعم",
        "points": 20,
        "explanation": "يجب حذف البيانات الشخصية قبل إعادة تدوير الجهاز لحماية الخصوصية."
    },
]

# -----------------------
# الحالة
# -----------------------
if "day" not in st.session_state:
    st.session_state.day = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "last_correct" not in st.session_state:
    st.session_state.last_correct = False

score = st.session_state.score
day = st.session_state.day

# -----------------------
# الشجرة
# -----------------------
if score >= 80:
    tree = "🌳"
elif score >= 40:
    tree = "🌿"
else:
    tree = "🌱"

# -----------------------
# العنوان
# -----------------------
st.markdown('<div class="title">🌱 تحدي التقنية المستدامة</div>', unsafe_allow_html=True)
st.markdown(f"<div style='text-align:center;font-size:60px'>{tree}</div>", unsafe_allow_html=True)

# -----------------------
# النقاط + التقدم
# -----------------------
st.markdown(f"<div class='points'>⭐ النقاط: {score}</div>", unsafe_allow_html=True)

progress = day / len(tasks)
st.progress(progress)
st.write(f"{int(progress * 100)}% مكتمل")

# -----------------------
# الكرت
# -----------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

if day < len(tasks):
    task = tasks[day]

    st.subheader(task["day"])
    st.markdown(f"<div class='task'>{task['task']}</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='question'>🧠 {task['question']}</div>", unsafe_allow_html=True)

    answer = st.radio("اختر الإجابة:", task["options"], key=f"answer_{day}")

    if not st.session_state.answered:
        if st.button("تحقق من الإجابة"):
            st.session_state.answered = True

            if answer == task["correct"]:
                st.session_state.last_correct = True
                st.session_state.score += task["points"]
            else:
                st.session_state.last_correct = False

            st.rerun()

    else:
        if st.session_state.last_correct:
            st.success("إجابة صحيحة! 🎉")
            st.info(task["explanation"])

            if st.button("التالي"):
                st.session_state.day += 1
                st.session_state.answered = False
                st.session_state.last_correct = False
                st.rerun()
        else:
            st.error("إجابة خاطئة ❌ حاول مرة أخرى")
            st.warning(task["explanation"])

            if st.button("إعادة المحاولة"):
                st.session_state.answered = False
                st.session_state.last_correct = False
                st.rerun()

else:
    st.success("🎉 انتهى التحدي!")
    st.balloons()

    if score == 100:
        st.success("ممتاز! أنت بطل التقنية المستدامة 🌳")
    elif score >= 60:
        st.info("أداء جميل! واصل تحسين عاداتك التقنية المستدامة 🌿")
    else:
        st.warning("بداية جيدة، حاول مرة أخرى لتحسين نتيجتك 🌱")

    st.write(f"درجتك النهائية: {score} من 100")

    if st.button("إعادة التحدي"):
        st.session_state.day = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.last_correct = False
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)