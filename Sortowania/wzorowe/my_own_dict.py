class MyDictionary:
    def __init__(self):
        self.entries = []

    def __setitem__(self, key, value):
        for entry in self.entries:
            if entry[0] == key:
                entry[1] = value
                return
        self.entries.append([key, value])

    def __getitem__(self, key):
        for entry in self.entries:
            if entry[0] == key:
                return entry[1]
        raise KeyError(key)

    def __delitem__(self, key):
        for i in range(len(self.entries)):
            if self.entries[i][0] == key:
                del self.entries[i]
                return
        raise KeyError(key)

    def __contains__(self, key):
        for entry in self.entries:
            if entry[0] == key:
                return True
        return False

    def keys(self):
        return [entry[0] for entry in self.entries]

    def values(self):
        return [entry[1] for entry in self.entries]

    def items(self):
        return self.entries.copy()

    def __len__(self):
        return len(self.entries)
