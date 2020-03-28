import time

# Timer inspired by https://realpython.com/python-timer/

class Timer:
    def __init__(self):
        self.start_time = None
    
    def start(self):
        if self.start_time is not None:
            raise TimerAlreadyRunning
            
        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is None:
            raise TimerNotRunning
            
        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
        return(elapsed_time)

class TimerAlreadyRunning(Exception):
    pass

class TimerNotRunning(Exception):
    pass