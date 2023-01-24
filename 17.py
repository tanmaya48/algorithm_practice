#https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/


def platforms_required(arrivals,departures):
    event_times = set(arrivals+departures)
    max_trains_present= 0
    for time in event_times:
        trains_present =0
        for arrive_time,depart_time in zip(arrivals,departures):
            if (time - arrive_time)*(time - depart_time) <= 0:
                trains_present+=1
        max_trains_present = max(trains_present,max_trains_present)
    return max_trains_present



def main():
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000 ]
    print(platforms_required(arrivals, departures))


if __name__ == '__main__':
    main()