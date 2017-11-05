from datetime import datetime, timedelta

def datetime_range(start, end, delta, value, step):
    current = start
    while current < end:
        yield current, "%.4f" % value
        current += delta
        value += step


four_to_eight = [(dt[0].strftime('%H:%M'), dt[1]) for dt in
       datetime_range(datetime(2016, 4, 13, 5, 20), datetime(2016, 4, 13, 8, 0),
       timedelta(minutes=1), 0, 0.00234)]

print(four_to_eight)

eight_to_twelve = [(dt[0].strftime('%H:%M'), dt[1]) for dt in
       datetime_range(datetime(2016, 4, 13, 8, 0), datetime(2016, 4, 13, 12, 0),
       timedelta(minutes=1), 0.3721, 0.0101)]

print(eight_to_twelve)

twelve_to_fourteen = [(dt[0].strftime('%H:%M'), dt[1]) for dt in
       datetime_range(datetime(2016, 4, 13, 12, 0), datetime(2016, 4, 13, 14, 0),
       timedelta(minutes=1), 2.7860, 0.0035)]

print(twelve_to_fourteen)


fourteen_to_seventeen = [(dt[0].strftime('%H:%M'), dt[1]) for dt in
       datetime_range(datetime(2016, 4, 13, 14, 0), datetime(2016, 4, 13, 17, 0),
       timedelta(minutes=1), 3.2025, -0.0023)]

print(fourteen_to_seventeen)


seventeen_to_twenty = [(dt[0].strftime('%H:%M'), dt[1]) for dt in
       datetime_range(datetime(2016, 4, 13, 17, 0), datetime(2016, 4, 13, 20, 0),
       timedelta(minutes=1), 2.7908, -0.0144)]

print(seventeen_to_twenty)

twenty_to_tweenty_one = [(dt[0].strftime('%H:%M'), dt[1]) for dt in
       datetime_range(datetime(2016, 4, 13, 20, 0), datetime(2016, 4, 13, 21, 0),
       timedelta(minutes=1), 0.2132, -0.004)]

print(twenty_to_tweenty_one)