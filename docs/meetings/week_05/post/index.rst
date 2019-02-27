Post: Reactive discussion + peer exercise
=========================================

Discuss briefly the need to work through tutorials.

Go over solutions to Quadratic question.

If time permits:

Discuss the idea of creating a fighting game::

    >>> class Warrior:
    ...    """
    ...    A class for a warrior
    ...    """
    ...    def __init__(self, hp, ap):
    ...        self.hp = hp
    ...        self.ap = ap
    ...    def is_alive(self):
    ...        return self.hp > 0

Having created this we can write a function to have one warrior attack another::

    >>> import random
    >>> def attack(attacker, defender):
    ...     defender.hp -= attacker.ap + random.choice([-1, 0, 1])
    >>> fighter_1 = Warrior(hp=50, ap=5)
    >>> fighter_2 = Warrior(hp=60, ap=4)
    >>> random.seed(0)
    >>> attack(fighter_1, fighter_2)
    >>> fighter_1.hp, fighter_2.hp
    (50, 55)

We could also make our Warrior class directly have this attack function **as a
method**. NOTE where the :code:`self` variable appears::

    >>> class Warrior:
    ...    """
    ...    A class for a warrior
    ...    """
    ...    def __init__(self, hp, ap):
    ...        self.hp = hp
    ...        self.ap = ap
    ...    def is_alive(self):
    ...        return self.hp > 0
    ...    def attack(self, other):
    ...        other.hp -= self.ap + random.choice([-1, 0, 1])


With this we can now write a function to simulate a match (time permitting, ask
students to do this in groups)::

    >>> def match(fighter_1, fighter_2):
    ...     while fighter_1.is_alive() and fighter_2.is_alive():
    ...         fighter_1.attack(fighter_2)
    ...         fighter_2.attack(fighter_1)
    ...     if fighter_1.is_alive():
    ...         return 0
    ...     if fighter_2.is_alive():
    ...         return 1
    ...     return None
    >>> superman = Warrior(hp=50, ap=5)
    >>> superwoman = Warrior(hp=60, ap=4)
    >>> random.seed(2)
    >>> match(fighter_1=superman, fighter_2=superwoman)
    1
