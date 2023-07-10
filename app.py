import json
import streamlit as st
from streamlit_timeline import timeline
from datetime import datetime
from streamlit_pills import pills
from streamlit_option_menu import option_menu
from streamlit_chat import message
from streamlit.components.v1 import html
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from streamlit_extras.colored_header import colored_header

from botcore.setup import trace_palm2


from botcore.bot.food_doctor import BotFoodDoctor
from botcore.utils import load_example_input

st.set_page_config(page_title="Pate Health AI", layout="wide",
                   initial_sidebar_state="collapsed")
from format_message import *

if "med_his" not in st.session_state:
    st.session_state.med_his = ""

if "Foodlike" not in st.session_state:
    st.session_state.Foodlike = ""

if "list_answer" not in st.session_state:
    st.session_state.list_answer = {}


if "target" not in st.session_state:
    st.session_state.target = ""


if "timeline" not in st.session_state:
    st.session_state.timeline = 0


if "button" not in st.session_state:
    st.session_state.button = False


def hide_hamburger():

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                
                .css-18ni7ap {
                position: static !important; 
                top: auto !important; 
                left: auto !important; 
                right: auto !important; 
                height: auto !important;
            }

                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def show_time_line():

    with open('example.json', "r") as f:
        data = f.read()
    parsed_data = json.loads(data)


    # test case 
    image = ""
    video = ""
    
    
    headline = ""
    text = "CHAPTER II: The subject matter of linguistics comprises all manifestations of human speech, whether that of savages or civilized nations, or of archaic, classical or decadent periods. In each period the linguist must consider not only correct speech and flowery language, but all other forms of expression as well. And that is not all: since he is often unable to observe speech directly, he must consider written texts, for only through them can he reach idioms that are remote in time or space.</p><br/"

    # date time 
    day = ""
    month = ""
    year = ""
    
    
    
    
    format_dicts = {
        "media": {
          "url": f"{image}",
          "caption": ""
        },
        "start_date": {
          "year": "2020",
           "month": "7",
           "day": "20"
        },
        "text": {
          "headline": f"{headline}",
          "text": f"<br/><p>{text}"
        }
      }
    
    

    new_list = [format_dicts]
    parsed_data['events'] = new_list

    json_string = json.dumps(parsed_data)
    timeline(json_string, height=800)


# hide_hamburger()

st.markdown("<h1 style='text-align: center; color: red;'>Pate Health</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'> transform the way you approach your health and nutrition journey</p>",
            unsafe_allow_html=True)


selected_options = option_menu(None, ["📝Analytics",  "💬chat Bot"],
                               icons=['📝', '🔎'],
                               menu_icon="cast", default_index=0, orientation="horizontal",
                               styles={
    "container": {"padding": "0!important", "background-color": "transparent"},
    "icon": {"color": "#52d00", "font-size": "25px"},
    "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#52d00"},
    "nav-link-selected": {"background-color": "#f07382"},

}
)


if selected_options == "📝Analytics":
    with st.expander("See how it work?"):
        with st.form(key='my_form'):
            dataColumns = st.columns(2)

            with dataColumns[0]:
                st.session_state.med_his = st.text_input(
                    'Medical history', key='la1')
                if st.session_state.med_his:
                    st.session_state.list_answer['Medical history'] = st.session_state.med_his
                st.session_state.target = st.text_area("Your target")

            with dataColumns[1]:
                st.session_state.Foodlike = st.text_input(
                    'Food interested', key='la2')

                css = '''
                <style>
                
                    .stTextArea textarea {
                        height: 200px;
                    }
                    .label {
                    display: none;
                    }
                    
                </style>
                '''

                st.session_state.timeline = st.date_input(
                    "When\'s timeline?",
                    datetime.now())
                selected = pills("You can chooose this plans", [
                                 "1 month ", "2 month", "3 month"])

                if st.session_state.Foodlike:
                    st.session_state.list_answer['Food interested'] = st.session_state.Foodlike

                st.markdown(css, unsafe_allow_html=True)

            dataColumns_submit = st.columns(2)
            with dataColumns_submit[0]:
                if st.form_submit_button('Confirm Responses'):
                    st.session_state.button = True
    model = trace_palm2()
    input_note = load_example_input()
    doctor = BotFoodDoctor(model)
    doctor.load_note(input_note)

    data = doctor.checkup()
    st.write(data)

    if st.session_state.button == True:
        st.write(st.session_state.list_answer)

        show_time_line()






# Constants


INITIAL_MESSAGE = [
    {"role": "user", "content": "Hi!"},
    {
        "role": "assistant",
        "content": "Hi there! I'm your Recycling Assistant, designed to help manage and understand your recycling needs. I can provide insights into your waste, help update your recycling preferences, connect you with matching recycling agents, and customize settings to suit your requirements. Let's start recycling smarter together!",
    },
]


def append_chat_history(question, answer):
    st.session_state["history"].append((question, answer))

def append_message(content, role="assistant", display=False):
    message = {"role": role, "content": content}
    message_func(content, False, display)
    st.session_state.messages.append(message)
    if role != "data":
        append_chat_history(st.session_state.messages[-2]["content"], content)

def model_palm2(input):
    trace_palm2(max_tokens=1024)

    vertexai.init(project="sinuous-tuner-392203", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40
    }
    chat = chat_model.start_chat(
        context="""You are a healthcare food bot. Please provide advice and tips to the user regarding their health and nutrition. You can start by asking for specific concerns or any preferences they have. You can also inquire about their dietary restrictions, medical conditions, or weight management goals. 
        Remember to provide personalized recommendations based on the user's input.""",
    )
    response = chat.send_message(str(input), **parameters)
    return response.text





if selected_options == "💬chat Bot":   
    
    # trace_palm2(max_tokens=1024)
    
    # Generate empty lists for generated and past.
    ## generated stores AI generated responses
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["I'm Pate bot, How may I help you?"]
    ## past stores User's questions
    if 'past' not in st.session_state:
        st.session_state['past'] = ['Hi!']

    # Layout of input/response containers
    input_container = st.container()
    colored_header(label='', description='', color_name='blue-30')
    response_container = st.container()

    # User input
    ## Function for taking user provided prompt as input
    def get_text():
        input_text = st.text_input("You: ", "", key="input")
        return input_text
    ## Applying the user input box
    with input_container:
        user_input = get_text()

    # Response output
    ## Function for taking user prompt as input followed by producing AI generated responses

    ## Conditional display of AI generated responses as a function of user provided prompts
    with response_container:
        if user_input:
            response = model_palm2(user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(response)
            
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i), seed=12)