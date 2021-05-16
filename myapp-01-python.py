from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_greetings():
  return 'Hello World'

@app.route('/bye')
def print_greetings():
  return 'Good Bye'


if __name__ == '__main__':
  app.run(debug = True)
