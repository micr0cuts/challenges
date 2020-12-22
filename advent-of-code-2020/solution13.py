from operator import itemgetter

inp = open('input13.txt', encoding='utf8').readlines()
timestamp = int(inp[0])
busses = {int(i) for i in inp[1].split(',') if i != 'x'}

toy_t = 939
toy_busses = {int(i) for i in [7, 13, 'x', 'x', 59, 'x', 31, 19] if i != 'x'}

def find_earliest_bus(t, busses):    
    waiting_time = max(busses)
    earliest_bus = max(busses)
    for bus in busses:
        mod = abs((t % bus) - bus)
        if mod < waiting_time:
            waiting_time = mod
            earliest_bus = bus
    return(waiting_time*earliest_bus)

assert find_earliest_bus(toy_t, toy_busses) == 295, find_earliest_bus(toy_t, toy_busses)
print("Solution for part 1 is:", find_earliest_bus(timestamp, busses))

# part 2

def find_bus_choreography(timetable):
    pattern = []
    for offset, bus in enumerate([i for i in timetable[1].split(',')]):
        if bus != 'x':
            pattern.append((offset, int(bus)))

    sorted_pattern = sorted(pattern, key=itemgetter(1), reverse=True)
    print(sorted_pattern)

    t = 0
    how_far_through_the_loop = 0 
    while how_far_through_the_loop != len(pattern)-1:
        #print(t, how_far_through_the_loop)    
        for i, (offset, bus) in enumerate(sorted_pattern):
            if t+offset % bus != 0:
                break
            how_far_through_the_loop = i
        t += pattern[0][1]
    return t-1

print("Asserting test case")
assert find_bus_choreography(["1000390\n", "17,x,13,19\n"]) == 3417, find_bus_choreography(["1000390\n", "17,x,13,19\n"])
print("Solution for part 2 is:", find_bus_choreography(inp))

    