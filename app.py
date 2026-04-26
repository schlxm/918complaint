import streamlit as st
import requests
import os
import random

# --- 1. SETUP ---
# Grabs the key you saved in GitHub Settings
API_KEY = os.environ.get('OWM_API_KEY')
CITY = "Tulsa"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=imperial"

st.set_page_config(page_title="918 Weather Sentry: LIVE", page_icon="🚜")
st.title("🚜 918 Weather Sentry: LIVE")

# --- 2. GETTING DATA ---
def get_weather():
    if not API_KEY:
        st.error("Key not found! Did you restart the Codespace?")
        return None
    try:
        response = requests.get(URL)
        return response.json()
    except:
        return None

weather_data = get_weather()

# --- 3. SHOWING RESULTS ---
if weather_data and weather_data.get('main'):
    temp = weather_data['main']['temp']
    hum = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    condition = weather_data['weather'][0]['description'].title()

    st.metric("Tulsa Temperature", f"{temp}°F")
    st.write(f"**Current Sky:** {condition} | **Humidity:** {hum}% | **Wind:** {wind_speed} MPH")

    # --- 4. THE EXPANDED COMPLAINT VAULT ---
    tulsa_complaints = [
        "The 169 is currently a parking lot. It would be faster to walk, but it's humid enough to grow gills.",
        "Forecast says 'Sunny' tomorrow, but Travis Meyer hasn't rolled up his sleeves yet, so I don't believe it.",
        "There's a new pothole on 71st street that just registered for its own ZIP code.",
        "Humidity is high. My hair now has the structural integrity of a cotton candy machine.",
        "Construction on 31st & Peoria has officially entered its 4th decade. The orange cones are now historical landmarks.",
        "The wind is blowing, which means the refinery smell is currently a 'local delicacy'.",
        "It's Sunday morning. QuikTrip is out of the good breakfast pizza. Life is a void.",
        "A single raindrop hit the IDL, so naturally, everyone has forgotten how to drive 65mph.",
        "The Gathering Place is probably packed. Avoid at all costs unless you enjoy dodging strollers.",
        "I saw a guy at 91st & Yale driving a lifted truck like it’s a jet ski. Stay safe out there.",
        "My thermostat is going to have a mid-life crisis by noon.",
        "The Golden Driller is currently staring at the clouds and wondering why he doesn't have an umbrella."
    ]
    
    with st.chat_message("user", avatar="🤠"):
        st.write(f"**Tulsa Sentry says:** {random.choice(tulsa_complaints)}")

    # --- 5. THE "STAY HOME" METER ---
    st.divider()
    st.subheader("Should I stay on the couch?")

    risk_score = 0
    if hum > 80: risk_score += 30
    if "rain" in condition.lower() or "thunderstorm" in condition.lower(): risk_score += 50
    if temp < 70 or temp > 95: risk_score += 20

    # Cap at 100 for the progress bar
    progress_val = min(risk_score, 100)
    st.progress(progress_val / 100)
    
    if risk_score > 80:
        st.error("COUCH STATUS: MANDATORY. Order some local BBQ and wait for the green sky to pass.")
    else:
        st.success("COUCH STATUS: OPTIONAL. But why would you leave?")

else:
    st.info("Still waiting on the data. It's probably stuck in traffic on Yale.")

# --- 6. TULSA WEEKEND GENERATOR ---
st.divider()
if st.button("Generate a 918 Weekend Plan"):
    plans = [
        "Go to the Cherry Street Farmers Market, buy one loaf of bread for $12, and feel cultured.",
        "Drive to the Blue Whale in Catoosa, take one photo, and wonder why you drove that far.",
        "Attempt to find the 'Center of the Universe' and get disappointed by the acoustics again.",
        "Go to a 918-themed brewery and pretend you can taste the 'notes of Arkansas River water'."
    ]
    st.info(random.choice(plans))

st.divider()
if st.button("Force Sentry Refresh"):
    st.rerun()
