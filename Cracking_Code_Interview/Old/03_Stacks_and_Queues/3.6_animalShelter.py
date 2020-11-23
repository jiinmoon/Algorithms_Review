""" 3.6 Animal Shelter

Question:

    An animal shelter, which holds only dogs and cats, operates on a strctly
    FIFO basis. People must adopt either the oldest based on arrival time of all
    animals at the shelter, or they can select whether they would prefer a dog
    or a cat ( and will receive the oldest animal of tha type ). They cannot
    select which specific animal they would like. Create the data structures to
    maintain this system and implemenet operations such as enqueue, dequeueAny,
    dequeueDog, and dequeueCat. You may use the LinkedList data struct.

---

This is a particular OOP challenge of how you will design the class structures
and utilize the types to your advantage.

In this case, it would make sense to maintain a two seperate queues: catQueue
and dogQueue. And each cat and dog objects should be separate and their types
should contain sort of time stamp of when they are admitted in the system.

Thus, when we dequeueAny, we can compare the peek of two queues to return the
oldest timestamp'd animal. Otherwise, just continue.

The timestamp can be anything but it would be preferred to have it as a class
variable.

"""

class Animal(object):
    timeStamp = 0

    def __init__(self, name):
        self.timeStamp += 1
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Cat'

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Dog'

class AnimalShelter():

    def __init__(self):
        self.catQueue = []
        self.dogQueue = []

    def enqueue(self, animal):
        if animal.__repr__ == 'Cat': self.catQueue.enqueue(animal)
        else: self.dogQueue.enqueue(animal)

    def dequeueAny(self):
        if self.catQueue.isEmpty() and self.dogQueue.isEmpty():
            return None
        elif self.catQueue.isEmpty():
            return self.dogQueue.dequeue()
        elif self.dogQueue.isEmpty():
            return self.catQueue.dequeue()
        else:
            topCat = self.catQueue.peek()
            topDog = self.dogQueue.peek()
            return topCat if topCat.timeStamp > topDog.timeStamp else topDog

    def dequeueCat(self):
        if self.catQueue.isEmpty(): return None
        return self.catQueue.dequeue()

    def dequeueDog(self):
        if self.dogQueue.isEmpty(): return None
        return self.dogQuene.dequeue()

