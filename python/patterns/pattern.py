
# Patterns as they might apply in simulations

"""
+ Allows for efficient communication between sim components.
+ one to many dependency relationship.  Where observer objects(selfobservers) are notified
    of changes in the state of the subject object(selfobservable).
"""
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement update method.")

class ConcreteObserver(Observer):
    def update(self, message):
        print("Received message: ", message)

def observerPatternExample():
    subject = Subject()
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify("Hello, observers!")

    subject.detach(observer2)
    subject.notify("Observer2 detached.")


"""
+ Useful for creating simulation objects without explicitly specifying their classes.
+ Provides an interface(factory) for creating objects of various types
+ Flexibility and extensibility
"""
class FactoryPattern:
    def __init__(self):
        pass

"""
+ Suitable for representing hierarchical structures in simulations.
+ Objects can be composed into tree-like structures, where individual objects and groups of
    objects are treated uniformly.
"""
class CompositePattern:
    def __init__(self):
        pass

"""
+ enables simulations to change their behavior dynamically based on their internal state.
+ encapsulates different states of an object as separate classes, allowing cleaner and more
    manageable code.
"""
class StatePattern:
    def __init__(self):
        pass

"""
+ provides a way to iterate over elements of a simulation object or collection without exposing
    its internal structure.
+ separates traversal logic from the underlying data structure, enhances readability.
"""
class IteratorPattern:
    def __init__(self):
        pass

"""
+ allows simulations to dynamically select algorithms or behaviors at runtime.
+ encapsualtes different algorithms or startegies as separate classes and enables them to be interchanged seamlessly.
"""
class StrategyPattern:
    def __init__(self):
        pass

"""
+ enhances the functionality of simulation objects dynamically by wrapping them with additional behavior.
+ provides flexible alternative to subclassing and allows for the coposition of behaviors.
"""
class DecoratorPattern:
    def __init__(self):
        pass

"""
+ ensures taht only one instance of a simulation object is created throughout the simulation.
+ useful when there should be a single point of access to a shared resource.
"""
class SingletonPattern:
    def __init__(self):
        pass
