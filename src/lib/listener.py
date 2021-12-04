class Listener:

    def __init__(self):
        self._events = {}   


    def dispatch(self, event: str):

        """This method dispatches every callbakcs with the index `event`"""
        
        if event in self._events:

            if isinstance(self._events[event], list):

                for callback in self._events[event]:
                    callback()


    def add(self, event: str, *callbacks: callable):

        """This method add every events callbacks passed as `*callbacks`"""

        for callback in callbacks:
            
            if event in self._events:
                self._events[event].append(callback)

            else:
                self._events[event] = [callback]


    def remove(self, event: str, *callbacks: callable):

        """This method remove every events callbacks passed as `*callbacks`"""
        
        for callback in callbacks:

            if event in self._events:

                if callback in self._events[event]:
                    index = self._events[event].index(callback)

                    self._events[event].pop(index)
