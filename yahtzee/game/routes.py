from flask import render_template, url_for, request, redirect, Blueprint
from yahtzee.game.utils import roll_dice, get_dice_imgs
from yahtzee.game.vars import Game

game = Blueprint('game', __name__)


@game.route("/game/new")
def new_game():
    global cur_game
    cur_game = Game(1)
    return render_template('new.html', title='New Game', game=cur_game)


@game.route("/game/play")
def play():
    try:
        d_imgs = get_dice_imgs(cur_game.dice, cur_game.held)

        return render_template('play.html', title='Play', game=cur_game, d_imgs=d_imgs)
    except Exception as e:
        print(e)
        print("Could not load game; Redirecting to '/game/new'")
        return redirect(url_for('game.new_game'))


@game.route("/game/roll")
def roll():
    try:
        cur_game.dice = roll_dice(cur_game.dice, cur_game.held)
        cur_game.roll += 1 # Increment roll num

        return redirect(url_for('game.play'))
    except Exception as e:
        print(e)
        print("Could not roll dice; Redirecting to '/game/new'")
        return redirect(url_for('game.new_game'))


@game.route("/game/hold/<int:d>")
def hold(d):
    if d not in cur_game.held:
        cur_game.held.append(d)
    else:
        cur_game.held.remove(d)

    return redirect(url_for('game.play'))
