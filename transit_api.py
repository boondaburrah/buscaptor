__author__ = 'lukeberr'
from os import environ
from requests import get


class Transit:
    def __init__(self):
        self.api_key = environ.get("TRANSIT_API_KEY")
        pass

    def get_stop(self, stop_id):
        stop_arrivals = get("http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/"
                            + stop_id
                            + ".json?key="
                            + self.api_key).json()
        stop_info = get("http://api.pugetsound.onebusaway.org/api/where/stop/"
                        + stop_id
                        + ".json?key="
                        + self.api_key).json()
        return Stop(stop_info, stop_arrivals)

    def get_stops(self, location):
        pass


class Stop:
    def __init__(self, stop_info, stop_arrivals):
        self.id = stop_info['data']['entry']['id']
        self.heading = stop_info['data']['entry']['direction']
        if self.id != stop_arrivals['data']['entry']['stopId']:
            raise RuntimeError("API returned arrivals for wrong stop!")
