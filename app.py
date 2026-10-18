import os
import datetime
import webbrowser
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def process_command(cmd):
    cmd = cmd.lower().strip()
    
    if 'time' in cmd:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
    elif 'date' in cmd or 'day' in cmd:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."
    elif 'wikipedia' in cmd or 'who is' in cmd or 'what is' in cmd:
        query = cmd.replace('wikipedia', '').replace('who is', '').replace('what is', '').strip()
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
            res = requests.get(url, timeout=5).json()
            if 'extract' in res:
                return res['extract'][:280] + "..."
            return f"I searched Wikipedia for '{query}' but could not find a summary."
        except Exception:
            return f"I couldn't fetch Wikipedia information for '{query}' right now."
    elif 'youtube' in cmd:
        return "Opening YouTube for you..."
    elif 'google' in cmd:
        return "Opening Google Search..."
    elif 'joke' in cmd:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif 'hello' in cmd or 'hi' in cmd:
        return "Hello! I am your AI Voice Assistant. How can I assist you today?"
    elif 'how are you' in cmd:
        return "I'm functioning at 100% capacity and ready to assist you!"
    else:
        return f"I received your command: '{cmd}'. You can ask me for the time, date, Wikipedia summaries, jokes, or website shortcuts!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json() if request.is_json else request.form
    command = data.get('command', '').strip()
    if not command:
        return jsonify({'error': 'No command detected.'}), 400
        
    response_text = process_command(command)
    return jsonify({
        'command': command,
        'response': response_text
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
