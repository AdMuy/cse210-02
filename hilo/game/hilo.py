import random

class Card:
    """A card with a number from 1 to 13.

    The responsibility of Card is to keep track of the number on the card and calculate the points for 
    it.
   
    Attributes:
        value (int): The number on the card.
        points (int): The number of points the guess is worth.
    """

    def __init__(card):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (card): An instance of Card.
        """
        card.value = 0
        card.points = 0

    def face(card, guess):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
            guess: The guess from the user.
        """
        card.lastvalue = random.randint(1, 13)
        card.value = random.randint(1, 13)
        if guess == "l":
            if card.value < card.lastvalue:
                card.points += 100
                print(f'The card was {card.value}')
                print(f'Your total score is: {card.points}')
            else:
                card.points += 0 
                print(f'The card was {card.value}')
                print(f'Your total score is: {card.points}')
        if guess == "h":
            if card.value > card.lastvalue:
                card.points += 100
                print(f'The card was {card.value}')
                print(f'Your total score is: {card.points}')
            else: 
                card.points += 0 
                print(f'The card was {card.value}')
                print(f'Your total score is: {card.points}')
