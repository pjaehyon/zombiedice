"""
Zombie Dice is by Steve Jackson Games
http://zombiedice.sjgames.com/


Zombie Dice simulator by Al Sweigart (al@inventwithpython.com)
(I'm not affiliated with SJ Games. This is a hobby project.)

Note: A "turn" is a single player's turn. A "round" is every player having one turn.
Note: Since all variables are public in Python, it is trivial to have a bot that hacks the tournament code. Inspect the bot code before running it.
Note: We don't use OOP for bots. A "zombie dice bot" simply implements a turn() method which calls a global roll() function as often as it likes. See documentation for details.
"""

import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program.')

VERBOSE = False # if True, program outputs the actions that happen during the game


def runGame(zombies):
    """Runs a single game of zombie dice. zombies is a list of zombie dice bot objects."""
    pass


def runTournament(zombies, numGames):
    """A tournament is one or more games of Zombie Dice. The bots are re-used between games, so they can remember previous games.
    zombies is a list of zombie bot objects. numGames is an int of how many games to run."""
    pass


def roll():
    """This global function is called by a zombie bot object to indicate that they wish to roll the dice.
    The state of the game and previous rolls are held in global variables."""
    pass


def rollDie(die):
    """Returns the result of a single die roll as a dictionary with keys 'color' and 'icon'.
    The die parameter is a string of the color of the die (i.e. 'green', 'yellow', 'red').
    The 'color' values in the return dict are one of 'green', 'yellow', 'red'.
    The 'icon' values are one of 'shotgun', 'footsteps', 'brains'."""
    pass



class ZombieBot_RandomCoinFlip(object):
    """After the first roll, this bot always has a fifty-fifty chance of deciding to roll again or stopping."""
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        results = roll() # first roll

        while results and random.randint(0, 1) == 0:
            results = roll()



def main():
    # fill up the zombies list with different bot objects, and then pass to runTournament()
    zombies = []
    zombies.append(ZombieBot_RandomCoinFlip('Alice'))
    zombies.append(ZombieBot_RandomCoinFlip('Bob'))
    runTournament(zombies, 1)


if __name__ == '__main__':
    main()