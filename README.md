# Yahtzee

The classic dice game Yahtzee, recreated using Python and Flask.

For a video demonstration of this project, [click here.](https://www.youtube.com/watch?v=l2iZLh5wNi4)

## Description

The game of Yahtzee is simple to learn (Visit [Dice Game Depot](https://www.dicegamedepot.com/yahtzee-rules/) for complete rule details) as it relies heavily on random dice rolls. Still, there is enough strategy involved to make it enjoyable. 

This project was primarily intended as practice for creating larger more complex web applications using Flask or similar web frameworks. Additionally, it is intended to satisfy the 'final project' requirements for Harvard CS50's course on edX.org.

## Gameplay

#### Starting the Game
While on the home page, you can select the number of players using the 4 colored buttons. This will then take you to a page where you will be given the chance to edit each player's name or stick with the defaults. Click the button at the bottom to start playing.

#### Playing the Game
Each player takes turns rolling the 5 dice (3 rolls per turn) and tries to achieve the highest score in each category possible. Pressing the hold button under a dice face will 'freeze' that dice and it will turn gray, signifying it will not be re-rolled. You can click this button again to 'unfreeze' the dice so that it can be re-rolled.

You can select a scoring category at any point after your first roll, which will immediately end your turn and update your score. The list of scoring categories is refreshed after each roll with the highest scoring category at the top.

If you score a category as 0 at any point, you will not be allowed to score it on following turns. You'll be able to see these categories under 'Void Categories'.

**Bonus** (35 pts) can be obtained if you get 63 pts or more in the ones-sixes categories.

**Yahtzee** (50 pts) can be scored multiple times.

#### End of Game
When all players have completed their turns, the game is over and the results screen is shown. Here you can compare scores and the winner will be displayed in proud **bold text**.

## Usage

You can start the program using the following command while in the main application directory (/yahtzee_flask).

```
python run.py
```

This will start the flask web server and create an application instance. You can access the server though the local-host URL (usually http://127.0.0.1:5000/) which Flask will display in the cmd-line.

## Requirements

You'll need the following main packages in order to run this application as well as their dependencies. These should be automatically installed by pip.

- flask
- flask_wtf
- wt_forms

You can install these using the following command as an example.

```
pip install flask
```

## Feedback

If you'd like to provide feedback on this project, you can get in touch with me through [github.com/d-spence](https://github.com/d-spence). 

## Acknowledgement

Much appreciation goes to [CS50](https://cs50.harvard.edu/x/2020/) and YouTuber [Corey Schafer](https://www.youtube.com/c/Coreyms/featured) for his Python/Flask tutorials.
