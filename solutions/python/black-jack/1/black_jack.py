"""Hashmap das cartas com letras"""
FACE_CARDS = {'J': 10 , 'Q': 10, 'K': 10, 'A': 1}

def value_of_card(card) -> int:
    """Determine the scoring value of a card"""
    if card in FACE_CARDS:
        return int(FACE_CARDS[card])  
    return int(card)

def higher_card(card_one, card_two):
    """Comparo e retorno o maior ou ambos."""
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_two) > value_of_card(card_one):
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card"""
    if card_one == 'A':
        card_one = 11
    if card_two == 'A':
        card_two = 11
    if (value_of_card(card_one) + value_of_card(card_two) + 11) > 21:
        return 1
    return 11
        


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    ten_cards = {'10', 'J', 'Q', 'K'}
    if card_one == 'A' and card_two in ten_cards:
        return True
    if card_two == 'A' and card_one in ten_cards:
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    face_cards = {'J', 'Q', 'K'}
    if card_one in face_cards and card_two in face_cards:
        return True
    if card_one == card_two:
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    if 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11:
        return True
    return False