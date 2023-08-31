from flask import Flask,render_template
from game_of_life import GameOfLife 
app = Flask(__name__)

@app.route('/')
def home():
    global game 
    game = GameOfLife(width=20, height=20)
    return render_template('index.html', game=game)

@app.route('/live')
def live():
    global game
    if game.counter > 1:
        game.form_new_generation()
    game.counter  += 1
    return render_template('live.html', world = game.world, counter = game.counter, old_world = game.old_world)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000, debug=True)
