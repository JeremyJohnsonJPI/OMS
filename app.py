from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World here!'

@app.route('/hello')
def hello():
  return "Hello from flask!"

if __name__ == "__main__":        
  app.run()