roster = ["Beshansky",
          "Collins",
          "Fischer",
          "Giovanucci",
          "Jain",
          "Kim",
          "Lauture",
          "Lee",
          "Maddox",
          "Martinez",
          "Mendez",
          "Oh",
          "Petrone",
          "Posada",
          "Rule",
          "Schilb",
          "Tariq",
          "Wang",
          "Wolf"]

import random


def call_three(roster):
    """
    print three names randomly

    roster: a list of strings
    """
    print(random.sample(roster, 3))

call_three(roster)
