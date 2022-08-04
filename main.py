import mouse
import keyboard
import time

class Mouse:
    """
    Allows you to record mouse events and play them
    """
    
    def __init__(self, delay_between_events=1e-20, stop_key="esc"):
        """
        # Arguments

            delay_between_events: An integer for the delay between each event for listening and executing
            stop_key: A string containing the key to listen to in order to stop playing or recording, defaulted to escape key (You can combine characters such as ctrl+esc)
        """
        self.events = []
        self.delay = delay_between_events
        self.stop_key = stop_key
        self.recording = False

    def _pass_event(self, event):
        if self.recording:
            if type(event) == mouse.MoveEvent:
                self.events.append(["move", mouse.get_position()])

            elif type(event) == mouse.ButtonEvent:
                if event.event_type != "double":
                    self.events.append(["click", event.button])
                else:
                    self.events.append(["double", event.button])

            elif type(event) == mouse.WheelEvent:
                self.events.append(["wheel", event.delta])

    def record(self, delay_before_recording=0):
        """
        Waits delay_before_recording seconds then records mouse events until the stop key is pressed

        # Arguments

            delay_before_recording: An integer represting the delay before recording in seconds
        """
        time.sleep(delay_before_recording)

        self.recording = True

        hook = mouse.hook(self._pass_event)
        keyboard.wait(self.stop_key)
        mouse.unhook(hook)

    def play(self, loop=False):
        """
        plays the recorded events

        # Arguments

            loop: A bool to specify whether you want the program to constantly play the events
        """
        
        recording = True
        def stop_recording(): 
            nonlocal recording

            recording = False

        keyboard.add_hotkey(self.stop_key, stop_recording)

        while True:
            for i in self.events:
                if not recording:
                    return

                if i[0] == "move":
                    mouse.move(*i[1])
                elif i[0] == "click":
                    mouse.click(i[1])
                elif i[0] == "wheel":
                    mouse.wheel(i[1])
                elif i[0] == "double":
                    mouse.double_click(i[1])
                
                time.sleep(self.delay)
        
            if loop:
                continue
            break
