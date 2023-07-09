import  streamlit as st 
from streamlit_timeline import timeline
from datetime import datetime
from streamlit_pills import pills
from streamlit_option_menu import option_menu



st.set_page_config(page_title="Pate Health AI",layout="wide", initial_sidebar_state="collapsed")





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

    css = """
    <style>
    .tl-slide .tl-slide-content-container{
        vertical-align: bottom !important;
    }
    
    </style>
    """
    st.markdown(css , unsafe_allow_html=True)
    timeline(data, height=800)


#hide_hamburger()

st.markdown("<h1 style='text-align: center; color: red;'>Pate Health</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'> Make us better !!!</p>", unsafe_allow_html=True)



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
                st.session_state.med_his = st.text_input('Medical history', key='la1')
                if st.session_state.med_his:
                    st.session_state.list_answer['Medical history'] = st.session_state.med_his
                st.session_state.target  = st.text_area("Your target")    
                
            with dataColumns[1]:
                st.session_state.Foodlike  = st.text_input('Food interested', key='la2')
                
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
            
                st.session_state.timeline  = st.date_input(
                "When\'s timeline?",
                datetime.now())
                selected = pills("You can chooose this plans", ["1 month ", "2 month", "3 month"])
                
                
                if st.session_state.Foodlike:
                    st.session_state.list_answer['Food interested'] = st.session_state.Foodlike
            
                st.markdown(css , unsafe_allow_html=True)
            
            
            
            dataColumns_submit = st.columns(2)
            with dataColumns_submit[0]:
                if st.form_submit_button('Confirm Responses'):    
                    st.session_state.button  = True
                    
        

    if  st.session_state.button  == True:
        st.write(st.session_state.list_answer)

        show_time_line()
        
