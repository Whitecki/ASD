class Counter():
    def __init__(self):
        self.val = 0
        self.cnt = 0
    
    def change_position(self, x):
        self.val = x
        self.cnt += 1

    def go_back(self):
        self.val -= 1
        self.cnt += 1

    def get_value(self):
        return self.val
    
    def get_usage(self):
        return self.cnt
    

class Truck():
    def __init__(self):
        self.range = 0
        self.stops = 0

    def add_range(self, val):
        self.range += val
        self.stops += 1

    def go(self):
        self.range -= 1

    def cant_go(self):
        return self.range == 0

    def get_stops_num(self):
        return self.stops


def truck_run(arr):
    n = len(arr)
    T = [0 for _ in range(n)]
    maxi = Counter()
    truck = Truck()
    pos = 0
    
    while pos < n:
        if arr[pos] > 0:
            if arr[pos] > n - pos:
                truck.add_range(arr[pos])
                return maxi.get_usage(), truck.get_stops_num()
            T[arr[pos]] += 1

        if arr[pos] > maxi.get_value():
            maxi.change_position(arr[pos])
        pos += 1

        if truck.cant_go():
            if maxi.get_value() == 0:
                return maxi.get_usage(), False
            
            truck.add_range(maxi.get_value())
            T[maxi.get_value()] -= 1

            while T[maxi.get_value()] == 0 and maxi.get_value() > 0:
                maxi.go_back()

        truck.go()
    return maxi.get_usage(), truck.get_stops_num()

test_cases = [
    ([3, 0, 2, 8, 1, 1, 1, 1, 0, 0, 0, 0, 0], 3),
    ([1, 1, 1, 1, 1, 10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 6),
    ([0, 1000, 0], False)

]
for test_case, correct_ans in test_cases:
    test_cnt, test_output = truck_run(test_case)
    assert test_cnt < 2 * len(test_case)
    assert test_output == correct_ans
    print("OK", test_case, correct_ans)