# Worst case scenario is 14 drops which is the solution to the given equation:
# x * (x+1)/2 = 100
# Therefore I need to start dropping eggs from 14th floor and continue
# You can find a good explanation to this here:
# https://medium.com/@khopsickle/2-eggs-and-100-floors-a032beb77aaa#:~:text=A%20building%20has%20100%20floors,can%20drop%20the%20egg%20again.

FLOOR_COUNT = 100
# As I stated above I start dropping from floor 14 but this can be generalized
# like start_floor = (start_floor+1)/egg_count = floor_count

def drop_egg(break_point):
    min_floor = 0
    step_size = 14
    max_floor = step_size

    while(max_floor < FLOOR_COUNT):
        if max_floor >= break_point:
            for i in range(min_floor, max_floor):
                if i >= break_point:
                    return i - 1
        else:
            min_floor = max_floor + 1
            max_floor = max_floor + step_size - 1
            step_size = step_size - 1

    if min_floor >= break_point:
        return min_floor - 1
    else:
        return FLOOR_COUNT

print("For break_point 1 answer is: " + str(drop_egg(1)))
print("For break_point 100 answer is: " + str(drop_egg(100)))
print("For break_point 101 answer is: " + str(drop_egg(101)))
print("For break_point 61 answer is: " + str(drop_egg(61)))
