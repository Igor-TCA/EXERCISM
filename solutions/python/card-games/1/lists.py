"""Functions for tracking poker hands and assorted card tasks"""

def get_rounds(number):
    """Create a list containing the current and next two round numbers"""
    return list(range(number, number +3))


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    return list(rounds_1 + rounds_2)


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return (number in rounds)


def card_average(hand):
    """Calculate and returns the average card value from the list."""
    return (sum(hand)/len(hand))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average"""
    return  (sum(hand)/len(hand)) == hand[len(hand)//2] or (sum(hand)/len(hand)) == ((hand[0]+hand[-1])/2)
        
                                
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    evens = hand[::2]
    odds = hand[1::2]

    return (sum(evens)/len(evens)) == (sum(odds)/len(odds))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2."""
    if hand[-1] == 11:
        jack = hand[-1]
        hand[-1] = jack * 2

    return hand


    
    