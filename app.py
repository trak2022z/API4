from flask import Flask
app = Flask(__name__)

notatki = []



@app.route('/')
def index():
    
  return 'Heloooooo'  

if __name__ == "__main__":
        app.run()

