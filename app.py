from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route('/')
def home():
    GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/live/')
def live():
    gen = GameOfLife()
    if gen.counter > 0:
        gen.form_new_generation()
    gen.counter += 1
    return render_template('live.html', gen=gen)

