from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_greetings():
  return 'Hello World'

@app.route('/hello/<name>')
def print_custom_greetongs(name):
  return f'Hello {name} , How are you feeling today?'

if __name__ == '__main__':
  app.run(debug = True)
