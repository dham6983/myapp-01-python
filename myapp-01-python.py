from flask import Flask

app = Flask(__name__)

@app.run('/')
def print_greetings():
  return 'Hello World'
