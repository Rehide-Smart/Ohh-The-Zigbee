from flask import Flask, json, render_template, session,request, url_for, flash, redirect, Response, session, stream_with_context
from flask_ask_alphavideo import Ask, question, statement, audio, current_stream, logger, convert_errors

app = Flask(__name__)
ask = Ask(app, "/")
logger = logging.getLogger()
logging.getLogger('flask_ask').setLevel(logging.INFO)

@ask.launch
def launch():
  return play(https://github.com/Rehide-Smart/Ohh-The-Zigbee/raw/main/oog%20fhe%20zigbee.wav)


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
