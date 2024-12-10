def add_vote(x) -> int:
    """
    Adds a vote to the candidate
    """
    try:
        int(x)
        x += 1
    except:
        quit("Error")
    return x

def total_votes(x, y) -> int:
    """
    Gives the total amount of votes cast
    """

    try:
        total = x + y
        int(total)
    except:
        quit("Error")
    return total


