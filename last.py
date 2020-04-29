#read the last line of the file and check if it is a valid
# wtmp file if not write to error file

import re
import os
import abc

#line_to_test = 'guthriee pts/2        Sat Oct 29 17:37:45 2016 - Sat Oct 29 17:41:19 2016  (00:03)     ec2-54-69-152-243.us-west-2.compute.amazonaws.com'
line_to_test = 'robertsonbt pts/14       Thu Mar 31 00:00:54 2016 - Thu Mar 31 00:14:59 2016  (00:14)     96-33-0-219.dhcp.jcsn.tn.charter.com'
class Handler(metaclass=abc.ABCMeta):
    """
    Define an interface for handling requests.
    Implement the successor link.
    """

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self):
        pass

class ConcreteHandler1(Handler):
    """
    Handle Complete Session Record
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self):
        if re.match(r'^[a-z0-9_-]{3,15}\s+(pts\/|tty)\d{1,3}\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+[-]\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+\((\d{1,3})?\+?(\d{2}):(\d{2})\)\s+(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$',line_to_test):
            print(line_to_test)
            print('handled by concrete_handler_1')
        # if True:  # if can_handle:
            pass
        elif self._successor is not None:
            self._successor.handle_request()


class ConcreteHandler2(Handler):
    """
    Handle System Crash
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self):
        if re.match(r'^[a-z0-9_-]{3,15}\s+(pts\/|tty)\d{1,3}\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+[-]\s+\b(\w*down\w*)\b',line_to_test):
            print(line_to_test)
            print('handled by concrete_handler_2')
        # if False:  # if can_handle:
            pass
        elif self._successor is not None:
            self._successor.handle_request()

class ConcreteHandler3(Handler):
    """
    Handle System Shutdown
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self):
        if re.match(r'^\b(\w*shutdown system down\w*)\b\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+[-]\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+\((\d{1,3})?\+?(\d{2}):(\d{2})\)\s+(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$',line_to_test):
            print(line_to_test)
            print('handled by concrete_handler_3')
        # if False:  # if can_handle:
            pass
        elif self._successor is not None:
            self._successor.handle_request()


class ConcreteHandler4(Handler):
    """
    System Reboot
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self):
        if re.match(r'^\b(\w*reboot\s+ system boot\w*)\b\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+[-]\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+\((\d{1,3})?\+?(\d{2}):(\d{2})\)\s+(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$',line_to_test):
            print(line_to_test)
            print('handled by concrete_handler_4')
        # if False:  # if can_handle:
            pass
        elif self._successor is not None:
            self._successor.handle_request()


class ConcreteHandler5(Handler):
    """
    complete login from known terminal - session ended due to system crash
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self):
        if re.match(r'^[a-z0-9_-]{3,15}\s+(pts\/|tty)\d{1,3}\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+[-]\s+\b(\w*down\w*)\b\s+\((\d{1,3})?\+?(\d{2}):(\d{2})\)\s+(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$',line_to_test):
            print(line_to_test)
            print('handled by concrete_handler_5')
        # if False:  # if can_handle:
            pass
        elif self._successor is not None:
            self._successor.handle_request()



class ConcreteHandler6(Handler):
    """
    complete login from known terminal - known logoff time
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self):
        if re.match(r'^[a-z0-9_-]{3,15}\s+(pts\/|tty)\d{1,3}\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+[-]\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s+\d{4}\s+\((\d{1,3})?\+?(\d{2}):(\d{2})\)\s+(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$',line_to_test):
            print(line_to_test)
            print('handled by concrete_handler_6')
        # if False:  # if can_handle:
            pass
        elif self._successor is not None:
            self._successor.handle_request()



def main():
    concrete_handler_1 = ConcreteHandler1()
    concrete_handler_2 = ConcreteHandler2(concrete_handler_1)
    concrete_handler_3 = ConcreteHandler3(concrete_handler_2)
    concrete_handler_4 = ConcreteHandler4(concrete_handler_3)
    concrete_handler_5 = ConcreteHandler5(concrete_handler_4)
    concrete_handler_6 = ConcreteHandler6(concrete_handler_5)
    concrete_handler_6.handle_request()


if __name__ == "__main__":
    main()
