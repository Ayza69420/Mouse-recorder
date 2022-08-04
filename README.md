# Mouse Recorder

Provides a single python class that records mouse events and play them with two functions

# Instructions

You have to create an instance of the ``Mouse`` class, it takes two optional arguments:
  - *The delay between each event, it will be used for both recording and playing to get an accurate/equal result.*
  - *The stop key which will be used to stop recording or playing (playing will only play once unless it's being looped, the stop key here will be used to forcefully stop it in the middle of playing and in any case)*

Recording can be done using the ``record`` function, which will record all events until the stop key is pressed, all events will be stored in the ``events`` variable which will then later be used by the ``replay`` function to play all the events.

While It's not a feature to save recorded events yet and probably never, you could do it yourself and print the ``events`` variable once you finished recording which then you could replace the variable's value as a way of "saving" what you recorded.

**Fun fact: There are 0 required arguments**

# Installation

- Clone the repository with git using ``git clone https://github.com/Ayza69420/Mouse-recorder.git``
- Run ``cd Mouse-recorder``
- Run ``pip install -r requirements.txt`` to install the required libraries

Required libraries:
  - keyboard
  - mouse

# Main Functions

- **record**
  - *Takes one optional argument `delay_before_recording` set to 0 by default, this is the amount of time to wait before starting to record*

- **replay**
  - *Takes one optional argument `loop` set to False by default, this is whether you want the program to constantly replay the events until stop key is fired*

# Code example

```py
# All the arguments here are the default ones, I put them to make things clear

m = Mouse(1e-20, "esc") # Creating an instance of the Mouse class with a 1e-20 event delay and escape stop key
m.record(0) # Recording all events until escape key is pressed, wait 0 seconds before starting
m.replay(False) # Playing all events, setting loop to False```
