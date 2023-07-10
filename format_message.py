import streamlit as st
import re
import html

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
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
        <style>
          
            .stApp {{
            background: url("https://cdn.pixabay.com/photo/2017/08/06/01/56/bulb-2587637_1280.jpg"), linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8));
            background-position: center;
            background-blend-mode: multiply;
            
         }}
         
        </style>
         """,
         unsafe_allow_html=True
     )
    
def customize_button():

    custom_button_style = """
                <style>
                .row-widget.stButton {
                width: 133px;
                margin: 20px auto;
                font-size: 20px;
                }
                
                .row-widget.stButton button {
                /* Add your custom styles for the button here */
                }
                
                </style>
                """
    st.markdown(custom_button_style, unsafe_allow_html=True)
    
    


def format_message(text, allow_html=False):
    """
    This function is used to format the messages in the chatbot UI.

    Parameters:
    text (str): The text to be formatted.
    allow_html (bool): Whether to allow HTML tags in the formatted text.

    Returns:
    str: The formatted text.
    """
    text_blocks = re.split(r"```[\s\S]*?```", text)
    code_blocks = re.findall(r"```([\s\S]*?)```", text)

    text_blocks = [html.escape(block) for block in text_blocks]

    formatted_text = ""
    for i in range(len(text_blocks)):
        formatted_text += text_blocks[i].replace("\n", "")
        if i < len(code_blocks):
            if allow_html:
                formatted_text += f'<pre style="white-space: pre-wrap; word-wrap: break-word;"><code>{code_blocks[i]}</code></pre>'
            else:
                formatted_text += f'<pre style="white-space: pre-wrap; word-wrap: break-word;"><code>{html.escape(code_blocks[i])}</code></pre>'

    return formatted_text

def message_func(text, is_user=False, is_df=False):
    """
    This function is used to display the messages in the chatbot UI.

    Parameters:
    text (str): The text to be displayed.
    is_user (bool): Whether the message is from the user or not.
    is_df (bool): Whether the message is a dataframe or not.
    """
    if is_user:
        avatar_url = "https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortFlat&accessoriesType=Prescription01&hairColor=Auburn&facialHairType=BeardLight&facialHairColor=Black&clotheType=Hoodie&clotheColor=PastelBlue&eyeType=Squint&eyebrowType=DefaultNatural&mouthType=Smile&skinColor=Tanned"
        message_alignment = "flex-end"
        message_bg_color = "linear-gradient(135deg, #76b31d 0%, #e8e8e8 110%)"
        avatar_class = "user-avatar"
        st.write(
            f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <div style="background: {message_bg_color}; color: black; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 14px;">
                        {text} \n </div>
                    <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                </div>
                """,
            unsafe_allow_html=True,
        )
    else:
        avatar_url = "https://www.svgrepo.com/download/276096/recycling-recycle.svg"
        message_alignment = "flex-start"
        message_bg_color = "#fafcfc"
        avatar_class = "bot-avatar"

        text = format_message(text, True)

        st.write(
            f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                    <div style="background: {message_bg_color}; color: black; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 14px;">
                        {text} \n </div>
                </div>
                """,
            unsafe_allow_html=True,
        )