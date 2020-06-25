""" 7.1 Deck Of Cards


Question:

    Design the data structures for a generic deck of cards. Explain how you
    would subclass the data structures to implement blackjack.

---

This is a recollection on good OOP principles that we have learned before. How
would you represent cards and deck? What are acceptable practices? What kind of
OOP patterns would be utilize to solve the problem in hand?

For example, we maybe tempted to represent each cards in the deck as integer
numbered from 1 to 52. But would such approach be the best approach? First-able,
unless it is explicitly agreed upon, we would have no idea what specific number
corresponds to which card. And just as a int value itself, it is exposed and
vulnearable to be changes at whim.

To avoid this, we use Objects to represent our ideas. For example, the card
should be an object that has information about its suit and number. Then, the
deck would be another objct that maintains the list of card objects (maintaining
its lifecycles) that support various functionalities that a generic deck would
be expected to perform (i.e. shuffle, deal cards)...

"""
