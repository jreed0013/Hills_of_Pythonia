"""The Hills of Pythonia."""

__author__ = "730408704"

from random import randint

player: str = ""
points: int = 0
NAMED_CONSTANT: str = '\U0001F606'


def main() -> None:
    """Main function of 'The Hills of Pythonia."""
    global points
    greet()
    player: str = input()
    print(f"King Guido: {player}, our land has been plagued by attacks from beasts and monsters of unfathomable strength. Are you up to the challenge of defending our hopeless citizens and crowning yourself a hero of Pythonia?")
    points = 0
    choice1: int = int(input("To help Pythonia and slay the beast, press 1. To seek a new adventure in the kingdom of Javainia, press 2. To flee, press 3. "))
    if choice1 == (1 or 2 or 3):
        while choice1 < 3:
            while choice1 <= 1:
                dragon(player)
                print(f"Your Current adventure points are: {points}")
                returnchoicepdrag: int = int(input("1 to stay and continue fending off the Pythonian Dragon. Press 2 to find a new adventure. Press 3 to bask in victory and retire from your fighting days. "))
                choice1 = returnchoicepdrag
            while choice1 == 2:
                minotaur(player)
                print(f"Your Current adventure points are: {points}")
                returnchoicejmin: int = int(input("Press 1 to fight the Pythonian Dragon. Press 2 to stay and continue fending off the Javainian Minotaur. Press 3 or greater to bask in victory and retire from your fighting days. "))
                choice1 = returnchoicejmin
        end()
    else:
        print("King Guido: Sorry, this kingdom's savior can probably follow directions properly...")
        end()


def greet() -> None:
    """Greeting of program."""
    print("King Guido: Oh brave soul that has come across the kingdom of Pythonia, what is your name? ")


def dragon(player: str) -> None:
    """Dragon fight encounter."""
    global points
    print(f"King Guido: {player}, the beast comes out at night; be prepared to fight then...")
    print("Night falls.. you feel chills down your spine...")
    print("The Pythonian Dragon has appeared!")
    phealth: int = 500
    health: int = 100
    print("Make your first move.")
    while phealth > 0 and health > 0:
        print("It is now your turn to attack.")
        playeraha: int = int(input("To attack, press 1. To heal, press 2. To assess target, press 3. "))
        if playeraha == 1:
            achoice: int = int(input("To use bow, press 1. To use magic, press 2. To use uppercut, press 3. "))
            if achoice == 1:
                phealth -= 3
                print(f"Damage done. Dragon health: {phealth}/500")
            elif achoice == 2:
                phealth -= 5
                print(f"Damage done. Dragon health: {phealth}/500")
            elif achoice == 3:
                phealth -= 100
                print(f"Critical attack! Dragon health: {phealth}/500")
            else:
                print("invalid choice, loss of turn.")
        elif playeraha == 2:
            health += 30
            print(f"You have healed yourself! Player health: {health}/100")
            if health > 100:
                print("You're more healthy than thought humanly possible. This is groundbreaking!")
        elif playeraha == 3:
            print("You have chosen to assess your target.")
            print("The pythonian dragon has 500 health points. The dragon can use firey breath to inflict 20 points of damage onto you. When enraged, it will whip its tail around to do 15 points of damage. It takes little damage from ranged weapons and magic; however, it is particularly weak to uppercuts.")
        else:
            print("invalid choice, loss of turn.")
        print("It is now the Pythonian Dragon's Turn to attack.")
        pdragaha: int = randint(1, 3)
        if pdragaha == 1:
            health -= 20
            print(f"The Pythonian Dragon used Firey Breath. Player health: {health}/100")
        elif pdragaha == 2:
            health -= 15
            print(f"The Pythonian Dragon used Tail Whip. Player health: {health}/100")
        elif pdragaha == 3:
            phealth += 10
            print(f"The Pythonian Dragon has healed itself. Dragon health: {phealth}/500")
        print(f"{player}'s health: {health}/100")
        print(f"Pythonian Dragon's health: {phealth}/500")
    if phealth <= 0:
        print(f"King Guido: Congrats {player}, you have slain the dragon. We are eternally in debt to you! Would you like to stay around for a while. Though you hurt it pretty bad, the pesky dragon might come back sometime soon!")
        points += 1
    else:
        print(f"King Guido: It appears the Pythonian Dragon has bested {player} in combat. They were a kind soul and will be remembered fondly.")


def minotaur(player: str) -> None:
    """Minotaur fight encounter."""
    global points
    print(f"King Goslin: I am the king of Javainia. King Guido tells me you have come to save us. Thank you for your service {player}, the beast strikes at dawn; be prepared to fight then...")
    print("Dawn approaches.. a sense of dread washes over you...")
    print("The Javainian Minotaur has appeared!")
    phealth: int = 1000
    health: int = 100
    print("Make your first move.")
    while phealth > 0 and health > 0:
        print("It is now your turn to attack.")
        playeraha: int = int(input("To attack, press 1. To heal, press 2. To assess target, press 3. "))
        if playeraha == 1:
            achoice: int = int(input("To use magic, press 1. To use bow, press 2. To use uppercut, press 3. "))
            if achoice == 1:
                phealth -= 100
                print(f"Critical Attack! Minotaur health: {phealth}/1000")
            elif achoice == 2:
                phealth -= 5
                print(f"Damage done. Minotaur health: {phealth}/1000")
            elif achoice == 3:
                phealth -= 3
                print(f"Damage done. Minotaur health: {phealth}/1000")
            else:
                print("invalid choice, loss of turn.")
        elif playeraha == 2:
            health += 30
            print(f"You have healed yourself! Player health: {health}/100")
            if health > 100:
                print("You're more healthy than thought humanly possible. This is groundbreaking!")
        elif playeraha == 3:
            print("You have chosen to assess your target.")
            print("The Javanian Minotaur has 1000 health points. The minotaur can use ground pound to inflict 10 points of damage onto you. When enraged, it will hurl a boulder at you to do 10 points of damage. It takes little damage from ranged weapons and melee attacks; however, it is particularly weak to magic.")
        else:
            print("invalid choice, loss of turn.")
        print("It is now the Javainian Minotaur's Turn to attack.")
        pminaha: int = randint(1, 3)
        if pminaha == 1:
            health -= 10
            print(f"The Javanian Minotaur used ground pound. Player health: {health}/100")
        elif pminaha == 2:
            health -= 10
            print(f"The Javanian Minotaur used Boulder Hurl. Player health: {health}/100")
        elif pminaha == 3:
            phealth += 10
            print(f"The Javanian Minotaur has healed itself. Minotaur health: {phealth}/1000")
        print(f"{player}'s health: {health}/100")
        print(f"Javainian Minotaur's health: {phealth}/1000")
    if phealth <= 0:
        print(f"King Gosling: Congrats {player}, you have slain the minotaur. We are eternally in debt to you! Would you like to stay around for a while. Though you hurt him pretty bad, the pesky minotaur might come back sometime soon!")
        points += 1
    else:
        print(f"King Guido: It appears the Javainian has bested {player} in combat. They were a kind soul and will be remembered fondly.")


def end() -> None:
    """End of main function message."""
    global points
    if points > 0:
        print(f"You finished the game with {points} adventure point(s). You will go down in history as a hero. Congrats on all of your achievements and be well.{NAMED_CONSTANT}")
    else:
        print(f"You finished the game with {points} adventure points. Better luck next time.")


if __name__ == "__main__":
    main()