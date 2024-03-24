
def strhash(key):
    h = 0
    primes = [10993, 12277, 11, 7927, 19, 12253, 9293]
    for i in range(len(key)):
        h ^= ord(key[i]) * primes[i % len(primes)]
    return h


class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def get(self, key):
        i = strhash(key) % self.size
        for record in self.buckets[i]:
            if record[0] == key:
                return record[1]
        self.buckets[i].append([key, 0])
        return 0

    def inc(self, key):
        i = strhash(key) % self.size
        for j in range(len(self.buckets[i])):
            if self.buckets[i][j][0] == key:
                self.buckets[i][j][1] += 1
                return
        self.buckets[i].append([key, 1])
        return

    def find(self, key):
        i = strhash(key) % self.size
        for record in self.buckets[i]:
            if record[0] == key:
                return True
        return False

    def get_max(self):
        return max(max(bucket, key=lambda x: x[1])[1] if bucket else 0 for bucket in self.buckets)




