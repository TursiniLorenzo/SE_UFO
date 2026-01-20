import datetime
from dataclasses import dataclass

@dataclass
class Sighting :
    id : int
    s_datetime : datetime.datetime
    city : str
    state : str
    country : str
    shape : str
    duration : int
    duration_hm : str
    comments : str
    date_posted : str
    latitude : float
    longitude : float

    def __str__ (self) :
        return f"{self.shape}"

    def __hash__ (self) :
        return hash (self.shape)

