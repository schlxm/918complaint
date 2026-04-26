import streamlit as st
import random

st.set_page_config(page_title="918 Weather Sentry", page_icon="🚜")

st.title("🚜 The 918 Weather Sentry")
st.caption("Because in Tulsa, if you don't like the weather, just wait 5 minutes and it'll be worse.")

# --- SIMULATED DATA ---
# Feel free to tweak these while sitting on the couch to see different results
temp = 88 
humidity = 75
wind_speed = 25 # MPH
is_construction_season = True # This is always True in Tulsa

st.subheader(f"Current Stats: {temp}°F | {humidity}% Humidity | {wind_speed} MPH Wind")

# --- THE TULSA LOGIC ---
def get_tulsa_complaint(t, h, w, c):
    if w > 30:
        return "The wind is currently trying to relocate your patio furniture to Broken Arrow. Stay inside."
    elif h > 70 and t > 85:
        return "It's so muggy the Golden Driller is starting to sweat. You will need a snorkel to walk to your car."
    elif t > 95:
        return "It's 'Surface of the Sun' season. Riverside Drive is currently melting. Avoid all contact with asphalt."
    elif 50 < t < 70 and w < 10:
        return "The weather is actually perfect, which means a massive cold front or a tornado is definitely 20 minutes away."
    elif c:
        return "The weather is fine, but the 169 is a parking lot and there's a new pothole on Yale that could swallow a Miata. Stay home."
    else:
        return "Check the sky. If it's green, head to the center-most room."

with st.chat_message("user", avatar="🤠"):
    st.write(f"**Tulsa Sentry says:** {get_tulsa_complaint(temp, humidity, wind_speed, is_construction_season)}")

# --- THE "TULSA VIBE" GENERATOR ---
st.divider()
if st.button("Generate a Local Weekend Plan"):
    plans = [
        "Go to the Gathering Place, realize it's too crowded, and end up at a QuikTrip for a Big Q.",
        "Drive to Jenks, look at the fish, and complain about the traffic on the bridge.",
        "Go to Brookside, look for parking for 45 minutes, then go home and order delivery.",
        "Visit the Center of the Universe, scream into the void, and hope the void doesn't scream back about your taxes.",
        "Go to Cain's Ballroom, stand in the back, and nod your head slightly while protecting your personal space."
    ]
    st.success(random.choice(plans))

st.divider()
st.caption("Data source: Trust me, I looked out the window. | Always check for Ozone Alerts.")
