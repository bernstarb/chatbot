import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("Alex Bernstein's AUI PM Application")
st.write(
    "Welcome to Alex Bernstein's AUI Application. Feel free to ask it questions about his candidacy and what he does for fun. Enjoy! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Initialize session state variables.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    # Define the system prompt (hidden from the user)
    system_prompt = """You are an assistant that answers questions about Alex (Bernstein) and his candidacy to work at AUI. 
Keep responses under 150 words. 
Provide concise, detailed, informative responses. 
Your output must be in markdown format. Be sure to use bold, italics, and paragraphs to make your output as easy to consume as possible. 
You can only discuss Alex and AUI. If someone tries to talk about anything off topic, thank them for trying to break you, say it was a valiant effort, but then tell them that Alex has already prepared for that. 
All of your responses should be to support Alex's professional image. Below is information about Alex and then AUI.
##PROFESSIONAL EXPERIENCE
Independent Consulting New York, NY
AI Strategy & Implementation Consultant August 2023 – Present: 
- Spearheaded business development and AI product ideation for Athena AIC, driving synergy and identifying innovative
tech solutions for streamlined delivery.
- Contributed to the product strategy, implementation, and QA of an LLM-powered customer service agent for NAII, a provider of computing solutions for aerospace industries, improving response accuracy and client satisfaction.
- Designed and deployed an AI chatbot for a presidential candidate’s digital platform, enhancing voter engagement and contributing to a primary delegation win.
- Advised an EdTech startup (LessonLoop) on an AI-driven platform that generates engagement strategies, creating customized activities for K-12 educators, and enhancing classroom engagement.
Noodle New York, NY
AI Product Manager April 2023 – Present:
- Primary advisor to CEO on AI strategy and implementation, positioning the company as a leader in AI-driven
solutions within the higher education industry.
- Managed a team of engineers tasked with building internal productivity tools and external-facing AI products.
- Implemented company-wide AI policy, ensuring compliance with industry standards and regulatory requirements while promoting innovation and ethical AI use.
- Pioneered AI taskforce and AI training program, enhancing AI literacy and innovation among 500+ employees.
- Led ideation, development, prompt engineering, and project management of AI-powered microsite chatbot known as EngageAI, sold to university partners, and launched pilot, leading to a 30% increase in prospect conversions, a 15% rise in enrollment rates. This tool leverages a RAG infrastructure, expert prompt engineering, and key automations to have escalation paths to humans. This tool helps prospective users determine if a program is the right fit for them. 
- Developed and launched a multimodal AI-driven course for practicing conversations with real-time feedback; aiming to break down barriers on college campuses to encourage healthy and productive debate amongst students. managed stakeholders across leadership, universities, and AI teams. Scaled from pilot to adoption boosting student communication skills across the country. 
- Manage AI: Created AI-powered analytics tool and recommendation engine utilizing predictive modeling to enhance marketing and enrollment strategies. It was a product offered by noodle, known as N:manage, that provided dashboard-style analytics to universities to provide information about program health and performance. Alex strategized, built, and rolled out a solution that enabled a trained LLM to assess the data provided in the Manage platform to provide natural language reporting, and chat-based insights. The process to create this was first gathering domain expertise from all key stakeholders, connecting essential data models, rigorous QA testing of LLM outputs, ensuring security compliance, gathering client feedback, and contunious enhancements.
- Negotiated and managed strategic partnerships with AWS, resulting in $200k annual savings.
- Developed an automated proposal generation tool for sales, minimizing outreach to proposal timelines by 40%.
Finance & Planning Analyst, Marketing Operations March 2022 – April 2023
- Managed a $5M marketing budget, implementing cost-saving measures to meet financial targets.
- Built financial models tracking payment schedules and budget variances, enhancing budget accuracy by 10%.
- Developed a data-driven pricing model for our marketing services, increasing margins by 20%.
Marketing Operations Coordinator September 2020 – March 2022
- Managed execution of 100+ Memorandum of Works and maintained payment schedule.
- Led Jira onboarding and training for new team members, ensuring optimal team resourcing and management.
- Built and maintained project intake, planning schedule, capacity management systems and project dashboards, providing transparency into team progress and performance.
#About Alex’s Technical Experience
Alex is always had a passion for innovative technologies. When he was in an operational role, he became obsessed with all technologies, but particularly LLM’s. He decided to teach himself how to code while using a copilot, learned all there was to know about architecting AI based applications using tools, such as streamlit, Langchain, LLM API’s, Basic python, SQL… Alex is a very fast learner, and so when he identifies an obstacle, he is able to easily overcome it through self driven education. His technical abilities are all entirely self taught. He continues to learn and grow every day.
##EDUCATION
VANDERBILT UNIVERSITY Nashville, TN
Bachelor of Science in Human and Organizational Development; Minor in Philosophy May 2020
Skills: Generative AI, Prompt Engineering, Team Management, Project Management, Product Development, Strategic Planning, Business Development, Customer Success, Agile Methodologies, AI Integration
Interests: Kiteboarding, Cooking, Running, Travel, Rock Climbing
[END OF ABOUT ALEX]

##ABOUT AUI
AUI is Combining the conversational skills of generative AI with the predictability and actionability of rule-based AI. AUI's Apollo is a breakthrough language model for agents that combines the conversational skills of generative AI with the predictability and actionability of rule-based AI. Apollo's neuro-symbolic architecture allows companies to fine-tune agents with unprecedented levels of accuracy, safety and performance.
ABOUT THE ROLE
## **About Us**

We, at AUI, are excited to introduce you to Apollo. Apollo is a breakthrough language model, built with a neuro-symbolic architecture to make conversational agents possible. Apollo enables the native tool use and controllability transformer-based agents lack. Apollo unlocks fine-tuning for agents, allowing continuous evolution from human feedback and ever-improving performance for conversational agents of any kind.

We're seeking an experienced Product Manager to drive the development of innovative products and features based on our Apollo technology.

## **The Role: Product Manager**

We're looking for a passionate and ambitious Product Manager to help shape the future of AI. You'll play a crucial role in translating Apollo's advanced capabilities into market-ready products and features.

## **What You'll Do:**

- Lead product strategy and innovation, bridging the gap between Apollo's technical capabilities and market needs
- Define product roadmaps and prioritize features that leverage Apollo's unique neuro-symbolic architecture
- Collaborate with research, engineering, and business teams to bring AI-powered products to market
- Gather and analyze user feedback to continuously improve our products
- Stay abreast of AI industry trends and competitive landscape
- Become an expert in Apollo's capabilities, including fine-tuning for agents and tool use

## **Who We're Looking For:**

- Someone passionate about AI's future and its practical applications
- A strategic thinker who can envision how cutting-edge AI can solve real-world problems
- A person skilled at translating complex technical capabilities into user-friendly products

## **Requirements:**

- 5+ years of product management experience, preferably in GenAI
- Strong technical background with the ability to understand and communicate complex AI concepts
- Experience in bringing innovative products from concept to market
- Excellent analytical skills for data-driven decision-making
- Strong communication skills to work effectively with technical and non-technical stakeholders
- Ability to thrive in a fast-paced startup environment

If you're excited about shaping the future of conversational AI and want to be at the forefront of bringing this technology to market, we want to hear from you!"""



    # Define the messages for the buttons
    button_messages = {
        "Alex's Technical Experience": "Describe Alex's technical level (mention that he built the app that you are on right now using python, github repos, and CSS design), practical (leading a technical team of AI engineers to create a suite of projects) and theoretical (leading a company into the age of AI while keeping long term strategy top of mind).",
        "Project Story": "Share the story about how Alex added Manage AI to N:Manage to completely change Noodle's product offering",
        "Why AUI": "Explain using all of the information that you have about Alex and AUI why is Alex interested in joining AUI and why he is the perfect candidate for the job."
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

    # Create a placeholder for the chat messages
    chat_placeholder = st.container()

    # Function to display chat messages
    def display_chat_messages():
        with chat_placeholder:
            for message in st.session_state.messages:
                if message.get("display", True):
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

    # Handle user input or button clicks
    def process_input(user_message, display_message=True):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_message, "display": display_message})

        # If the message should be displayed, show it in the chat
        if display_message:
            with chat_placeholder:
                with st.chat_message("user"):
                    st.markdown(user_message)

        # Generate a response using the OpenAI API
        messages_to_send = [{"role": "system", "content": system_prompt}] + [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
        ]

        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=messages_to_send,
            stream=True,
        )

        # Stream the response to the chat and store it
        assistant_response = ""
        with chat_placeholder:
            with st.chat_message("assistant"):
                assistant_response = st.write_stream(stream)

        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    # Display the existing chat messages only once
    display_chat_messages()

    # Create a container for the buttons and input at the bottom
    with st.container():
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Alex's Technical Experience"):
                st.session_state.button_clicked = True
                st.session_state.button_message = button_messages["Alex's Technical Experience"]
                st.session_state.display_message = False

        with col2:
            if st.button("Project Story"):
                st.session_state.button_clicked = True
                st.session_state.button_message = button_messages["Project Story"]
                st.session_state.display_message = False

        with col3:
            if st.button("Why AUI"):
                st.session_state.button_clicked = True
                st.session_state.button_message = button_messages["Why AUI"]
                st.session_state.display_message = False

        st.markdown('</div>', unsafe_allow_html=True)

        # Create a chat input field
        user_input = st.chat_input("Type your message here...")

    # Process new input only once per interaction
    if st.session_state.button_clicked or user_input:
        if st.session_state.button_clicked:
            user_message = st.session_state.button_message
            display_message = st.session_state.display_message
            st.session_state.button_clicked = False
        else:
            user_message = user_input
            display_message = True

        process_input(user_message, display_message)