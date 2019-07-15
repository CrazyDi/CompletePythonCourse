from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        """
        :return: string in the format of CLF -> LHR -> CAN
        """
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return '->'.join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)


fligth = Flight([Segment('GLA', 'LHR')])
print(fligth)
fligth.departure_point = 'EDI'
print(fligth)
