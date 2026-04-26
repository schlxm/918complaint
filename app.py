import streamlit as st
import random

# --- TULSA CONFIG ---
st.set_page_config(page_title="918 Sentry 2.0", page_icon="🏗️")

# MOCK API DATA (Sunday, April 26, 2026)
# Once you get an API key, we replace these hardcoded values with a requests.get()
current_temp = 65 
humidity = 89
condition = "Heavy Thunderstorm Incoming"
wind_speed = 6 

st.title("🏗️ 918 Weather Sentry: Pro Edition")
st.write(f"**Current Status:** {current_temp}°F | {condition}")

# --- THE EXPANDED COMPLAINT VAULT ---
tulsa_complaints = [
    "The 169 is currently a parking lot. It would be faster to walk, but it's humid enough to grow gills.",
    "Forecast says 'Sunny' tomorrow, but Travis Meyer hasn't rolled up his sleeves yet, so I don't believe it.",
    "There's a new pothole on 71st street that just registered for its own ZIP code.",
    "Humidity is at 89%. My hair now has the structural integrity of a cotton candy machine.",
    "Construction on 31st & Peoria has officially entered its 4th decade. The orange cones are now historical landmarks.",
    "The wind is blowing 6mph out of the SE, which means the refinery smell is currently a 'local delicacy'.",
    "It's Sunday morning. QuikTrip is out of the good breakfast pizza. Life is a void.",
    "A single raindrop hit the IDL, so naturally, everyone has forgotten how to drive 65mph.",
    "The Gathering Place is probably packed. Avoid at all costs unless you enjoy dodging strollers.",
    "I saw a guy at 91st & Yale driving a lifted truck like it’s a jet ski. Stay safe out there.",
    "It's 65 degrees now, but Monday says 87. My thermostat is going to have a mid-life crisis by noon.",
    "The Golden Driller is currently staring at the clouds and wondering why he doesn't have an umbrella."
]

# --- THE SENTRY OUTPUT ---
with st.chat_message("user", avatar="🤠"):
    st.write(f"**Sentry Alert:** {random.choice(tulsa_complaints)}")

# --- THE "STAY HOME" METER ---
st.divider()
st.subheader("Should I stay on the couch?")

# Logic based on today's heavy thunderstorm forecast
risk_score = 0
if humidity > 80: risk_score += 30
if "thunderstorm" in condition.lower(): risk_score += 50
if current_temp < 70: risk_score += 20

st.progress(risk_score / 100)
if risk_score > 80:
    st.error("COUCH STATUS: MANDATORY. Order some local BBQ and wait for the green sky to pass.")
else:
    st.success("COUCH STATUS: OPTIONAL. But why would you leave?")

# --- TULSA WEEKEND GENERATOR ---
if st.button("Generate a 918 Weekend Plan"):
    plans = [
        "Go to the Cherry Street Farmers Market, buy one loaf of bread for $12, and feel cultured.",
        "Drive to the Blue Whale in Catoosa, take one photo, and wonder why you drove that far.",
        "Attempt to find the 'Center of the Universe' and get disappointed by the acoustics again.",
        "Go to a 918-themed brewery and pretend you can taste the 'notes of Arkansas River water'."
    ]
    st.info(random.choice(plans))

st.caption(f"Last updated: Sunday, April 26 | Data provided by 918 Vibes™")
