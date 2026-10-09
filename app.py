
import streamlit as st
import joblib
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Personality Quest",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- MODEL LOADING ----------------
@st.cache_resource
def load_artifacts():
    artifacts = joblib.load("personality_model.joblib")
    return artifacts["model"], artifacts["scaler"]

try:
    model, scaler = load_artifacts()
except Exception as exc:
    st.error(f"Could not load model artifacts: {exc}")
    st.stop()

# ---------------- FEATURES ----------------
FEATURES = [
    "social_energy",
    "alone_time_preference",
    "talkativeness",
    "deep_reflection",
    "group_comfort",
    "party_liking",
    "listening_skill",
    "empathy",
    "organization",
    "leadership",
    "risk_taking",
    "public_speaking_comfort",
    "curiosity",
    "routine_preference",
    "excitement_seeking",
    "friendliness",
    "planning",
    "spontaneity",
    "adventurousness",
    "reading_habit",
    "sports_interest",
    "online_social_usage",
    "travel_desire",
    "gadget_usage",
    "work_style_collaborative",
    "decision_speed",
]

PERSONALITY_NAMES = {
    0: "Ambivert",
    1: "Extrovert",
    2: "Introvert",
}

SECTIONS = {
    "🌈 Social Energy": [
        "social_energy",
        "alone_time_preference",
        "talkativeness",
        "group_comfort",
        "party_liking",
        "listening_skill",
        "empathy",
        "friendliness",
        "public_speaking_comfort",
    ],
    "🧠 Thinking & Curiosity": [
    "deep_reflection",
    "curiosity",
    "decision_speed",
    ],
    "🎯 Lifestyle & Interests": [
        "risk_taking",
        "excitement_seeking",
        "adventurousness",
        "reading_habit",
        "sports_interest",
        "online_social_usage",
        "travel_desire",
        "gadget_usage",
    ],
    "💡 Work & Personal Habits": [
        "organization",
        "leadership",
        "routine_preference",
        "planning",
        "spontaneity",
        "work_style_collaborative",
    ],
}

QUESTIONS = {
    "social_energy": ("Social energy", "How energized do you feel around other people?"),
    "alone_time_preference": ("Me time", "How much do you enjoy spending time alone?"),
    "talkativeness": ("Talking", "How much do you enjoy talking with others?"),
    "deep_reflection": ("Deep thinking", "How often do you reflect deeply before forming an opinion?"),
    "group_comfort": ("Group comfort", "How comfortable are you in group settings?"),
    "party_liking": ("Social events", "How much do you enjoy parties and gatherings?"),
    "listening_skill": ("Listening", "How strongly do you value listening to others?"),
    "empathy": ("Empathy", "How readily do you understand other people's feelings?"),
    "organization": ("Organization", "How organized do you like to keep things?"),
    "leadership": ("Leadership", "How comfortable are you taking the lead?"),
    "risk_taking": ("Risk taking", "How willing are you to take risks?"),
    "public_speaking_comfort": ("Public speaking", "How comfortable are you speaking in front of a group?"),
    "curiosity": ("Curiosity", "How eager are you to explore new ideas?"),
    "routine_preference": ("Routine", "How much do you prefer a predictable routine?"),
    "excitement_seeking": ("Excitement", "How much do you seek exciting experiences?"),
    "friendliness": ("Friendliness", "How easily do you connect with new people?"),
    "planning": ("Planning", "How much do you plan ahead?"),
    "spontaneity": ("Spontaneity", "How much do you enjoy doing things spontaneously?"),
    "adventurousness": ("Adventure", "How adventurous would you describe yourself?"),
    "reading_habit": ("Reading", "How much do you enjoy reading?"),
    "sports_interest": ("Sports", "How interested are you in sports?"),
    "online_social_usage": ("Online social life", "How much do you use social platforms to connect with others?"),
    "travel_desire": ("Travel", "How strongly do you want to explore new places?"),
    "gadget_usage": ("Gadgets", "How much do you enjoy using technology and gadgets?"),
    "work_style_collaborative": ("Teamwork", "How much do you enjoy working collaboratively?"),
    "decision_speed": ("Decision making", "How quickly do you usually make decisions?"),
}

# Four excluded columns are deliberately not used as inputs.
# This model was trained on the 26 FEATURES above.
# Do not add creativity, emotional_stability, or stress_handling.

# ---------------- STYLING ----------------
st.markdown("""

<style>
/* Main page: use colors that adapt to Streamlit's theme */
.stApp {
    background: var(--background-color);
    color: var(--text-color);
}


.block-container {
    max-width: 850px;
    padding-top: 3.5rem;
    padding-bottom: 3rem;
}


/* Welcome banner */
.hero {
    padding: 2rem;
    border-radius: 26px;
    background: linear-gradient(
        120deg,
        #eadcff,
        #dff3ff,
        #dcfff0
    );
    color: #30204d !important;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(140, 120, 180, 0.2);
}

.hero h1,
.hero p {
    color: #30204d !important;
}

.hero h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

/* Questionnaire card */
div[data-testid="stForm"] {
    border: 1px solid var(--secondary-background-color);
    border-radius: 20px;
    padding: 1rem;
    background: var(--secondary-background-color);
}

/* Keep form text readable in both themes */
div[data-testid="stForm"] label,
div[data-testid="stForm"] p,
div[data-testid="stForm"] h2,
div[data-testid="stForm"] h3 {
    color: var(--text-color);
}

/* Buttons */
div.stButton > button[kind="primary"],
div[data-testid="stFormSubmitButton"] button {
    border: 0;
    border-radius: 14px;
    min-height: 3rem;
    font-weight: 700;
    background: linear-gradient(100deg, #8b5cf6, #ec72aa);
    color: #ffffff !important;
}

/* Result card: deliberately use a light card in either theme */
.result-card {
    border-radius: 24px;
    padding: 1.6rem;
    text-align: center;
    background: linear-gradient(135deg, #efe5ff, #e2f6ff);
    border: 1px solid rgba(140, 120, 180, 0.2);
    color: #30204d !important;
}

.result-card h1,
.result-card h2,
.result-card h3,
.result-card p {
    color: #30204d !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "started" not in st.session_state:
    st.session_state.started = False

if "result" not in st.session_state:
    st.session_state.result = None

if "answers" not in st.session_state:
    st.session_state.answers = {feature: 5.0 for feature in FEATURES}

# ---------------- WELCOME ----------------
st.markdown("""
<div class="hero">
    <h1>✨ Personality Quest</h1>
    <p>Every personality has its own kind of magic.</p>
    <p>Explore your preferences, answer honestly, and discover
    which personality type your ML model predicts.</p>
</div>
""", unsafe_allow_html=True)

if not st.session_state.started:
    st.markdown("### Ready to discover your personality?")
    st.write(
        "Answer 26 questions about your social preferences, "
        "interests, habits, and working style."
    )

    if st.button("🚀 Start my quest", type="primary", use_container_width=True):
        st.session_state.started = True
        st.rerun()

    st.caption("This is a machine-learning prediction, not a clinical assessment.")
    st.stop()

# ---------------- QUESTIONNAIRE ----------------
st.subheader("Your personality questions")

st.caption(
    "Rate each statement from 0 to 10. "
    "0 means very low and 10 means very high."
)

with st.form("personality_quiz"):
    answers = {}

    for section, features in SECTIONS.items():
        st.markdown(f"### {section}")

        for feature in features:
            label, question = QUESTIONS[feature]
            st.markdown(f"**{label}**")
            st.caption(question)

            answers[feature] = st.slider(
                label=f"Rate: {label}",
                min_value=0.0,
                max_value=10.0,
                value=float(st.session_state.answers[feature]),
                step=1.0,
                key=f"input_{feature}",
                label_visibility="collapsed",
            )

    submitted = st.form_submit_button(
        "✨ Reveal my personality",
        type="primary",
        use_container_width=True
    )

# Progress indicator
answered_count = len(FEATURES)
st.progress(answered_count / len(FEATURES))
st.caption(f"{answered_count} questions included in this quiz")

# ---------------- PREDICTION ----------------
if submitted:
    input_df = pd.DataFrame(
        [[answers[feature] for feature in FEATURES]],
        columns=FEATURES
    )

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]
    personality_id = int(prediction)

    personality = PERSONALITY_NAMES[personality_id]

    st.session_state.answers = answers
    st.session_state.result = {
        "class": personality_id,
        "personality": personality,
    }


PERSONALITY_NAMES = {
    0: "Ambivert",
    1: "Extrovert",
    2: "Introvert",
}

PERSONALITY_INFO = {
    0: {
        "emoji": "⚖️",
        "title": "The Balance Seeker",
        "description": "Ambiverts may enjoy social interactions while also valuing alone time.",
    },
    1: {
        "emoji": "🎉",
        "title": "The Social Energizer",
        "description": "Extroverts tend to enjoy social interaction and group activities.",
    },
    2: {
        "emoji": "🌙",
        "title": "The Quiet Thinker",
        "description": "Introverts tend to appreciate quieter environments and time to reflect.",
    },
}

# ---------------- RESULTS ----------------

if st.session_state.result is not None:
    result = st.session_state.result

    input_df = pd.DataFrame(
        [[st.session_state.answers[f] for f in FEATURES]],
        columns=FEATURES
    )

    scaled_input = scaler.transform(input_df)

    personality_id = result["class"]
    personality = PERSONALITY_NAMES[personality_id]
    info = PERSONALITY_INFO[personality_id]



    st.divider()

    # Animated reveal
    st.balloons()

    st.markdown(
        f"""
        <div class="result-card">
            <div style="font-size: 3rem;">{info["emoji"]}</div>
            <h2>Your Personality Profile</h2>
            <h1>{personality}</h1>
            <h3>{info["title"]}</h3>
            <p>{info["description"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # All three class probabilities
    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(scaled_input)[0]

        st.subheader("📊 Your Personality Breakdown")

        probability_df = pd.DataFrame({
            "Personality": [
                PERSONALITY_NAMES[int(cls)]
                for cls in model.classes_
            ],
            "Probability (%)": probabilities * 100,
        })

        # Show every class and its probability
        for _, row in probability_df.iterrows():

            name = row["Personality"]
            percentage = float(row["Probability (%)"])

            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**{name}**")
                st.progress(
                    max(0.0, min(1.0, percentage / 100))
                )

            with col2:
                st.markdown(f"### {percentage:.2f}%")

        st.caption(
            "These percentages are model-estimated probabilities, "
            "not validated measures of personality certainty."
        )

    # Explain all personality types
    st.subheader("🧠 Understand the Personality Types")

    for class_id in [0, 1, 2]:

        info_item = PERSONALITY_INFO[class_id]
        name = PERSONALITY_NAMES[class_id]

        with st.expander(
            f'{info_item["emoji"]} {name} — {info_item["title"]}'
        ):
            st.write(info_item["description"])

    # Retake
    if st.button(
        "🔄 Retake the Quiz",
        use_container_width=True
    ):
        st.session_state.result = None
        st.session_state.started = False
        st.rerun()