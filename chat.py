import json
from collections import Counter

import streamlit as st
from streamlit_chat import message


def fizzbuzz(x):
    try:
        x = eval(x)
    except:
        x = 1
    match x:
        case _ if x % 15 == 0:
            return "fizzbuzz"
        case _ if x % 3 == 0:
            return "fizz"
        case _ if x % 5 == 0:
            return "buzz"
        case _:
            return "other"


default_fizzbuzz = {"fizzbuzz": 0, "fizz": 0, "buzz": 0, "other": 0}

default_logo = (
    "https://raw.githubusercontent.com/"
    "nick-konovalchuk/streamlit-chat-azure/main/lama.png"
)

if "bot" not in st.session_state:
    st.session_state["bot"] = []
    st.session_state["fizzbuzz"] = []

if "user" not in st.session_state:
    st.session_state["user"] = []

message(
    """Hello!
I'm FizzBuzz Llama.
Please, enter something"""
)

for i, (user_message, bot_message) in enumerate(
    zip(st.session_state.user, st.session_state.bot)
):
    message(user_message, is_user=True, key=f"{i}_user", avatar_style="no-avatar")
    message(bot_message, allow_html=True, key=f"{i}", logo=default_logo)

with st.form(key="input"):
    user_input = st.text_area("You: ", "")
    pushed = st.form_submit_button("Enter")

if pushed:
    fizzbuzz_out = fizzbuzz(user_input)

    st.session_state.user.append(user_input)
    st.session_state.fizzbuzz.append(fizzbuzz_out)
    response = json.dumps(
        {**default_fizzbuzz, **Counter(st.session_state.fizzbuzz)},
        indent=4,
        separators=(", ", ":\t "),
    )

    st.session_state.bot.append(f"```json\n{response}\n```")

    st.rerun()
