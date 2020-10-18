
from threading import Lock
class TrafficLight:
    def __init__(self):
        self.directions12 = (1,2)
        self.dir12_lock = Lock()
        self.dir34_lock = Lock()
        
        self.dir12_lock.acquire()

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        if direction in self.directions12:
            if self.dir34_lock.locked():  #  Other roda is green
                self.dir34_lock.release()
                self.dir12_lock.acquire()
                turnGreen()
        else:
            if self.dir12_lock.locked():
                self.dir12_lock.release()
                self.dir34_lock.acquire()
                turnGreen()
            
        crossCar()
