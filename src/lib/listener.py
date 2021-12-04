class Listener:


    def __init__(self):
        self._events = {}   

    def _default_event(self, event: dict):
        
        if not 'cancelable' in event:
            event['cancelable'] = True
        
        if not 'content' in event:
            event['content'] = {}


    def _default_event_listener(self, event_type: str):

        if not event_type in self._events:
            self._events[event_type] = []


    def dispatch(self, event: dict):

        """This method dispatches every callbakcs with the index of the event type (event name)

        ```python
        event = {
            'type': str,
            'cancelable': bool,
            'content': dict
        }
        ```
        """

        event_type = event['type']

        self._default_event_listener(event_type)

        self._default_event(event)

        if event_type in self._events:

            if isinstance(self._events[event_type], list):

                for callback in self._events[event_type]:
                    continue_ = callback(event)

                    if event['cancelable'] and continue_ == False: return


    def add(self, event_type: str, *callbacks: callable):

        """This method add every events callbacks passed as `*callbacks`"""

        self._default_event_listener(event_type)

        for callback in callbacks:
            
            self._events[event_type].append(callback)


    def remove(self, event_type: str, *callbacks: callable):

        """This method remove every events callbacks passed as `*callbacks`"""

        self._default_event_listener(event_type)
        
        for callback in callbacks:
        
            if callback in self._events[event_type]:
                index = self._events[event_type].index(callback)

                self._events[event_type].pop(index)
