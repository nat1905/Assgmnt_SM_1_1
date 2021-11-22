from python_loc_counter import LOCCounter
import pprint


def loc():
    """calculate LOC"""
    counter = LOCCounter("ex1.py")
    loc_data = counter.getLOC()
    print("LOC", loc_data)
    pprint.pprint(loc_data)
    for k in loc_data:
        print(f"{k}: {loc_data[k]}")


if __name__ == "__main__":
    loc()
