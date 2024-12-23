import streamlit as st
import random

# Define word lists for each grade
word_lists = {
    "Grade1": [
        "adventure", "hill", "shirt", "black", "house", "stem",
        "brown", "king", "butterfly", "lad", "carpet", "leaves",
        "three", "cereal", "love", "wear", "elephant", "week",
        "flower", "pants", "white", "game", "paper", "yard",
        "grapes", "purple", "yellow", "green", "rain", "yelp",
        "happy", "rainbow", "agile"
    ],
    "Grade2": [
        "africa", "curiosity", "mirror", "after", "dresser", "palestine",
        "amharic", "eight", "playground", "english", "precious",
        "bangladesh", "ethiopia", "radiant", "bathroom", "europe", "rectangle",
        "bird", "familiar", "school", "blanket", "find", "spanish",
        "bookcase", "flower", "square", "books", "gratitude", "symphony",
        "canada", "hindi", "temperature", "carpet", "laugh", "urdu",
        "ceiling", "mean", "write", "click"
    ],
    "Grade3": [
        "apartment", "illuminate", "numbers", "backpack", "invent", "nutmeg",
        "bicycle", "jellyfish", "octopus", "boxcar", "kitchen", "peculiar",
        "butterfly", "language", "perseverance", "camera", "latch", "plaster",
        "chalkboard", "lessons", "poached", "complex", "letters", "pumpkin",
        "daring", "library", "rabbit", "delicate", "loaf", "school",
        "division", "meaning", "telescope", "dreamers", "microscope", "umbrella",
        "encyclopedia", "monkey", "violin", "favorite", "multiplication", "waterfall",
        "guitar", "mysterious", "xylophone"
    ],
    "Grade4": [
        "ambiguous", "giraffe", "percentage", "antarctic", "glamorous", "phenomenal",
        "calendar", "graduate", "presentation", "centipede", "guess", "question",
        "conscientious", "handwriting", "recent", "counsel", "hardship", "refrigerator",
        "coupon", "helicopter", "rough", "crackle", "highlight", "sincere",
        "custard", "igloo", "spreadsheet", "darkness", "ingenious", "stampede",
        "demonstrate", "jaguar", "suitable", "devastate", "kangaroo", "swordsmen",
        "dinosaur", "medication", "vikings", "dither", "nightmare", "windshield",
        "essential", "norsemen", "wishful", "exchange", "opportunity", "wristwatch",
        "exquisite", "ostrich"
    ],
    "Grade5": [
        "abdicate", "eccentricity", "perpendicular", "accommodate", "evaporate",
        "predominant", "advanced", "evermore", "quagmire", "ambiguous", "extensive",
        "qualitative", "amusing", "formidable", "solution", "barrage", "gigantic",
        "solvent", "belligerent", "gregarious", "berserk", "hypnotize", "squeeze",
        "bizarre", "incognito", "translucent", "bureaucracy", "intersect", "tuneful",
        "cabbage", "intuition", "ubiquitous", "complementary", "knelt", "unwavering",
        "confiscate", "leopard", "vanish", "construction", "meticulous", "versatile",
        "continuous", "nauseate", "violet", "creatures", "nostalgic", "voice",
        "dehydrated", "optimistic", "whimsical", "derogatory", "oscillate"
    ],
    "Grade6": [
        "administration", "ephemeral", "mischievous", "advanced", "esoteric", "negotiation",
        "alabaster", "exterior", "partisan", "altitude", "facetious", "phenomenon",
        "amiable", "faucet", "primers", "amusing", "garrulous", "procession",
        "anthem", "hexagonal", "pronounce", "banishment", "hypothesis", "recognition",
        "barricade", "improvise", "reimburse", "boisterous", "inscrutable", "relics",
        "commemorate", "intrepid", "resemble", "compliant", "jubilation", "salvation",
        "conclusion", "kaleidoscope", "scrimmage", "conference", "kneel", "simulation",
        "conserve", "leadership", "spectators", "discomfort", "lecture", "strident",
        "disengage", "leeway", "subdivision", "disseminate", "luminance", "vagabond"
    ],
    "Grade7": [
        "accompany", "enlisted", "perspicacity", "affirmation", "euphoria", "pharaoh",
        "alabaster", "fluctuate", "quaim", "altitude", "germinate", "quantum",
        "brigadier", "inexorable", "recognition", "bulletin", "infraction", "resourceful",
        "cherished", "jettison", "sausage", "collaboration", "lascivious", "scenery",
        "colonel", "lieutenant", "scrimmage", "commendable", "mellfluous", "siesta",
        "commissioned", "sophomore", "composure", "miniature", "stagnant", "conquering",
        "miracle", "superfluous", "consecutive", "narration"
    ],
    "Grade8": [
        "adage", "detrimental", "onomatopoeia", "affirmation", "dexterity", "perfidious",
        "airman", "discordant", "piedmont", "amethyst", "discredit", "plaudits",
        "amphitheater", "discrepancy", "preclude", "annexation", "disparate", "pronunciation",
        "appendectomy", "pulmonary", "azalea", "ephemeral", "auaint", "boisterously",
        "excerpt", "auixotic", "cacophony", "extravaganza", "redundancy", "chandeliers",
        "handkerchief", "remorse", "cherished", "indelible", "servile", "churlish",
        "indigenous", "sobriety", "cinnabar", "jubilee", "sphinx"
    ]
}

# Initialize state to track used words and contestants
if "used_words" not in st.session_state:
    st.session_state["used_words"] = {grade: [] for grade in word_lists.keys()}
if "contestants" not in st.session_state:
    st.session_state["contestants"] = {grade: [] for grade in word_lists.keys()}

# Streamlit app title
st.title("Spelling Bee Word Picker")

# Select grade
selected_grade = st.selectbox("Select Grade:", options=list(word_lists.keys()))

# Input number of contestants
num_contestants = st.number_input("Enter number of contestants for this grade:", min_value=1, step=1)

# Assign words to contestants
if st.button("Assign Words to Contestants"):
    available_words = [
        word for word in word_lists[selected_grade] 
        if word not in st.session_state["used_words"][selected_grade]
    ]

    if len(available_words) >= num_contestants:
        assigned_words = random.sample(available_words, num_contestants)
        st.session_state["used_words"][selected_grade].extend(assigned_words)
        st.session_state["contestants"][selected_grade] = assigned_words

        st.success("Words assigned to contestants:")
        for i, word in enumerate(assigned_words, start=1):
            st.write(f"Contestant {i}: {word}")
    else:
        st.warning("Not enough words available to assign to all contestants.")

# Reset words and contestants
if st.button("Reset Words and Contestants"):
    st.session_state["used_words"] = {grade: [] for grade in word_lists.keys()}
    st.session_state["contestants"] = {grade: [] for grade in word_lists.keys()}
    st.info("All words and contestants have been reset.")


# Reset words button
if st.button("Reset Words"):
    st.session_state["used_words"] = {grade: [] for grade in word_lists.keys()}
    st.info("All word lists have been reset.")
