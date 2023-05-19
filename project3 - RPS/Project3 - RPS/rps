#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def __init__(self):
        self.their_move = None
        self.my_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        move = ""
        while (move not in moves):
            move = input("choose your move: Rock, Paper, Scissors \n").lower()
            if (move in moves):
                return move
            else:
                print("Wrong input, Try again!")
                continue


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return RandomPlayer.move(self)
        return self.their_move


class CyclePlayer(Player):

    def move(self):
        if self.my_move is None:
            return RandomPlayer.move(self)
        else:
            # [rock,paper,scissors, keshav, shaina]
            # take the index from the moves array of the current move,
            # get the next index. if the next index is more than MaxIndex,
            # subtract maxindex from the index to get the next element else,
            # you have nextindex
            current_index = moves.index(self.my_move)
            next_index = current_index + 1
            max_index = len(moves) - 1
            if next_index > max_index:
                next_index = next_index - len(moves)
            return moves[next_index]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if move1 == move2:
            self.p1.score += 1
            self.p2.score += 1
        else:
            if (beats(move1, move2)):
                self.p1.score += 1
            else:
                self.p2.score += 1

        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\nGame start!\n")
        retryInput = True
        while (retryInput):
            try:
                rounds = int(input("How many rounds do you want to play?\n"))
                retryInput = False
            except ValueError:
                print("Invalid Input, Try again")

        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
            print("Player1 score- {}, Player2 score- {}"
                  .format(self.p1.score, self.p2.score))

        print("\nFinal Score: \n")
        if self.p1.score == self.p2.score:
            print("Player1 score- {}, Player2 score- {}"
                  .format(self.p1.score, self.p2.score))
            print("It's a Tie")
        elif self.p1.score > self.p2.score:
            print("Player1 score- {}, Player2 score- {}"
                  .format(self.p1.score, self.p2.score))
            print("Player 1 wins this game")
        else:
            print("Player2 score- {}, Player1 score- {}"
                  .format(self.p2.score, self.p1.score))
            print("Player 2 wins this game")

        print("\nGame over!")


if __name__ == '__main__':
    # write down choices and choose your rival
    choices = {
        "human": HumanPlayer(),
        "random": RandomPlayer(),
        "reflect": ReflectPlayer(),
        "cycle": CyclePlayer()
    }
    nextRound = True
    while nextRound:
        print("Rock, Paper, Scissors Game")
        selectedChoice = input("\nChoose Your Rival: " +
                               "(Reflect / Random / Human / Cycle)\n").lower()
        if selectedChoice in choices:
            # Game object with HumanPlayer and selected Player
            game = Game(HumanPlayer(), choices[selectedChoice])
            game.play_game()
        else:
            print("\nInvalid move, Enter correct move\n")

        play_game = input("\nDo you want to continue the game?"
                          + "Yes / No \n").lower()

        if play_game == 'no':
            nextRound = False
            print("\nThanks for Playing! Bye\n")
        elif play_game == 'yes':
            nextRound = True
        else:
            print("\nwrong input, exiting the game\n")
            print("\nThanks for Playing! Bye\n")
            nextRound = False
