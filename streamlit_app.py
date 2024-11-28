import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("Alex Bernstein's AUI PM Application")
st.write(
    "This is Alex Bernstein's Application to AUI. Feel free to ask it questions about his candidacy and enjoy! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Define the system prompt (hidden from the user)
    system_prompt = "You are a helpful assistant that answers questions about Alex Bernstein's application to AUI. Provide detailed and informative responses."

    # Define the messages for the buttons
    button_messages = {
        "Alex's technical experience": "Please tell me about Alex's technical experience.",
        "Project Story": "Could you share the story about Alex's significant project?",
        "Why AUI": "Why is Alex interested in joining AUI?"
    }

    # Add CSS to style the entire app and buttons
    st.markdown(
        """
        <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Open Sans', sans-serif;
        }

        /* Center the buttons container */
        .button-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }

        /* Style the buttons */
        div.stButton > button {
            background-color: #4a90e2;
            color: white;
            width: 100%;
            height: 50px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        /* Add hover effect to buttons */
        div.stButton > button:hover {
            background-color: #3a78c2;
        }

        /* Adjust the columns for equal spacing */
        .css-1adrfps {
            flex: 1;
            padding: 0 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a container for the buttons
    with st.container():
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        button_clicked = False  # Flag to indicate if a button was clicked
        button_message = ""     # Initialize the button message

        with col1:
            if st.button("Alex's technical experience"):
                button_message = button_messages["Alex's technical experience"]
                button_clicked = True

        with col2:
            if st.button("Project Story"):
                button_message = button_messages["Project Story"]
                button_clicked = True

        with col3:
            if st.button("Why AUI"):
                button_message = button_messages["Why AUI"]
                button_clicked = True
        st.markdown('</div>', unsafe_allow_html=True)

    # Handle button clicks
    if button_clicked:
        # Append the message as a user message
        st.session_state.messages.append({"role": "user", "content": button_message})
        with st.chat_message("user"):
            st.markdown(button_message)

        # Generate a response using the OpenAI API
        messages_to_send = [{"role": "system", "content": system_prompt}] + [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]

        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=messages_to_send,
            stream=True,
        )

        # Stream the response to the chat
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Create a chat input field to allow the user to enter a message.
    if prompt := st.chat_input("Type your message here..."):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        messages_to_send = [{"role": "system", "content": system_prompt}] + [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]

        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=messages_to_send,
            stream=True,
        )

        # Stream the response to the chat and store it.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})