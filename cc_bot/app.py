import streamlit
import requests
from loguru import logger

def _set_title():
    streamlit.title("Credit Card Bot")

def _put_textbox():
    user_input = streamlit.text_input(label="Ask a credit card question", max_chars=3000)
    return user_input

def _set_submit_button():
    with streamlit.form("cc_question_form"):
        submitted = streamlit.form_submit_button(label="Go")
    return submitted


def _call_backend_api(user_input: str, submission: bool):
    if submission:
        logger.info(f"User submitted question is: {user_input} ")
        response = requests.request(method="GET", url="http://localhost:8000/ccbot/user_query")
        logger.info(f"Response from AI is: {response}")
        if response:
            streamlit.subheader("Credit Card Bot Response")
            streamlit.write(response.text)


def main():
    _set_title()
    user_input = _put_textbox()
    submission = _set_submit_button()
    response = _call_backend_api(user_input, submission)


if __name__ == '__main__':
    main()