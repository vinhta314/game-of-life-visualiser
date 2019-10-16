# game-of-life-visualiser
## Introduction
### Game of Life
The "Game of Life" is a cellular automation model that was devised to simulate the evolutionary process. The model consists of a 2-dimenstional grid where the cells can take on one of two states, `dead` or `alive`. The next evolutionary state is determined by current grid state. The evolutionary process is therefore entirely dependant on the initial state, making it a zero-player game. 

The next state of a cell is determined by the current state of its eight nearest neighbours. The rules are:
* Any `alive` cell with fewer than two `alive` neighbours dies
* Any `alive` cell with two or three `alive` neighbours remains `alive`
* Any `alive` cell with more than three `alive` neighbours dies
* Any `dead` cell with three `alive` neighbours is revived

Learn more about the "Game of Life" [here](http://mathworld.wolfram.com/GameofLife.html).

### Application
This project provides a visual representation of the game of life which uses Python to model the grid evolutions and WebSockets to communicate to the client. The application is designed to allow users to change the state of cells on the client side during the evolutionary process, meaning the model is no longer a zero-player game. 

## Setup
Clone the repository locally using 
```
git clone
```
In a python `virtualenv`, install the required packages from the `requirements.txt` using 
```
pip install
```
To start the app, move to the root directory `game-of-life-visualiser` and run the command
```
python game_of_life.py
```
The app will now be running locally at `http://0.0.0.0:5000/`

## Functionality 


![image](https://user-images.githubusercontent.com/48162231/66879688-29273600-efb7-11e9-90ae-396d2024e4bd.png)
