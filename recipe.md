# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car
----------------------------------------------------------------------------------------------------------
As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth
----------------------------------------------------------------------------------------------------------
As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings
----------------------------------------------------------------------------------------------------------
As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Car                        │
│                            │
│ - (arg)Tyre
  - (method) add_entry() - LR.add_data(Tyre)
│ - (method) retrieve_data() -   LR.retrieve_data()                       │
│ -                          │
│   =>                       │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Tyre(pressure, tread-depth)│
│                         │
│ - (arg)pressure         │
│ - (arg)tread-depth      │
│ - (method) record_data() - dict: datetime: {pressure: tread-depth} for k, v
│ 
│   =>                    │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car:
    # User-facing properties:
    #   tracks: list of instances of Tyre

    def __init__(self):
        pass # No code here yet

    def add_entry(self, Tyre):
        # Parameters:
        #   Tyre: an instance of Tyre
        # Side-effects:
        #   Adds the tyre data to the list of tyres
        pass # No code here yet

    def retrieve_data(self, Tyre):
        # Parameters:
        #   Tyre: an instance of Tyre
        # Returns:
        #   A dictionary of tyre's parameters sorted by chronological order (using datetime)
        pass # No code here yet

    def overview(self):
        # Parameters


class Tyre:
    # User-facing properties:
    #   pressure: string
    #   tread-depth: string
    #   time: datetime.now()

    def __init__(self, pressure, depth):
        # Parameters:
        #   readings: dictionary
        # Side-effects:
        #   Creates a dictionary
        #   Add a datetime.now() entry to the dictionary as a key.
        pass # No code here yet

    def record_data(self, pressure, depth):
        # Parameters:
        #   pressure: string
        #   depth: string
        # Side-Effects:
        #   Adds a new entry to the dictionary with datetime.now() as a key
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Create a car
We create, then we add one tyre (FR)
We see that tyre is an object within car as an instance of tyre.
"""
car = Car()
Front-Right = Tyre("pressure", "depth")
car.add(Front-Right)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
