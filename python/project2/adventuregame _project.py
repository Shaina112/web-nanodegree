# your adventure game project.


import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(items, option):
    print_pause(
        "You find yourself standing in an open field," +
        " filled with grass and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a gorgon is somewhere around here, " +
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty" +
                "(but not very effective) dagger.")


def cave(items, option):

    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause(
            "You've been here before, and gotten all"
            " the good stuff. It's just an empty cave"
            " now."
        )
        print_pause("You walk back to the field.\n")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a " "rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take " +
                    "the sword with you.")
        print_pause("You walk back out to the field.")

        items.append("sword")
    fight(items, option)


def house(
    items,
    option,
):

    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens " +
        "and out steps a " + option + "."
    )
    print_pause("Eep! This is the " + option + " house!")
    print_pause("The " + option + " attacks you!")

    if "sword" not in items:
        print_pause(
            "You feel a bit under-prepared for this," +
            " what with only having a tiny dagger."
        )

    while True:
        field2 = input("Would you like to (1) fight or (2) " "run away?")

        if field2 == "1":

            if "sword" in items:
                print_pause(
                    "As the " + option + " moves to attack, "
                    "you unsheath your new sword."
                )
                print_pause(
                    "The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the "
                    "attack."
                )
                print_pause(
                    "But the " + option + " takes one look at "
                    "your shiny new toy and runs away!"
                )
                print_pause(
                    "You have rid the town of the " + option +
                    ". You are victorious!"
                )
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is " +
                            "no match for the " + option + ".")
                print_pause("You have been defeated!")
                play_again()
                break

        if field2 == "2":
            print_pause("You run back into the field. ")
            print_pause("Luckily, you don't seem " +
                        "to have been followed.")
            fight(items, option)
            break


def fight(items, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    while True:
        field = input("(Please enter 1 or 2.)")

        if field == "1":
            house(items, option)

        elif field == "2":
            cave(items, option)


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    items = []

    option = random.choice(["Hulk", "wicked witch",
                            "monster", "troll", "gorgon"])

    intro(items, option)
    fight(items, option)


play_game()
