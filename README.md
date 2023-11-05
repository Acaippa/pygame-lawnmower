# pygame-lawnmower
Lawnmower game made in pygame.

Mowe the lawn and sell the grass to buy better mowers!

The folder structure of this project isn't really ideal, and i hope to be able to update it soon.

# Installation (ver 0.3)
To run `main.py`, youll first of all need to download and install [Python](https://www.python.org/downloads/).

Then, install the requirements with `pip install -r requirements.txt`.

`python main.py` then runs the game! (Alternatively, you can just double click the file)

# Showcase
Here i'll show the the newest version of the game (ver 0.3)

<img src="https://github.com/Acaippa/pygame-lawnmower/assets/106773288/9cf76edf-d7f0-4eb1-a0a3-0a93ae5ec836" width="50%">

This is just a normal main game screen, with cheesy main text.

<br>

<img src="https://github.com/Acaippa/pygame-lawnmower/assets/106773288/13a65b03-87d8-4d3d-942c-56a757e1668f" width="25%">

Up in the left corner in the game, we also see a debug of the current framerate.

<br>

<img src="https://github.com/Acaippa/pygame-lawnmower/assets/106773288/f36891cb-58c8-4cb0-9754-69273ee42d77" width="50%">

Next up is the level selector. Per now there is only a `test_level` where all development has been done in.

<br>

<img src="https://github.com/Acaippa/pygame-lawnmower/assets/106773288/5d436103-281a-4ca2-9739-af0375ede11e" width="50%">

This is the actual gameplay screen. Using the arrow keys, you can move the mower around, and the grass then is removed behind it.

<br>

<img src="https://github.com/Acaippa/pygame-lawnmower/assets/106773288/88d05ed7-8d28-4c58-9b69-9e005eab8831" width="50%">

When the shop button is clicked, a menu will slide down, and you can then click to change out what mower you are currently using.

The grass counter, aswell as the money counter does not work in this version.

The field underneath the mower also has a very simple chunking system, whereas the field is divided into squares, and subsequent grass gets assign their own square. 
The game then loops through all the squares and updates every piece of grass inside that square. 
This has helped alot with performance, and i hope to get threading implemented later for a smoother experience.
