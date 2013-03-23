class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '({}, {})'.format(self.key, self.value)


class HashTable:
    def __init__(self):
        self.kv_store = [[]]

    def __delitem__(self, key):
        return self.delete(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def delete(self, key):
        """
        Deletes a KeyValue from the HashTable.
        """
        hash = self.hash(key)
        for i in range(len(self.kv_store[hash])):
            kv = self.kv_store[hash][i]
            if kv.key == key:
                del(self.kv_store[hash][i])
        return True

    def get(self, key):
        """
        Returns the value for the provided key.
        """
        hash = self.hash(key)
        for kv in self.kv_store[hash]:
            if kv.key == key:
                return kv.value
        return None

    def hash(self, key):
        """
        Returns the hash for a provided key.
        """
        return sum([ord(c) for c in key]) % len(self.kv_store)

    def pop(self, key):
        """
        Removes a key from the HashTable and returns its value.
        """
        hash = self.hash(key)
        value = None
        for i in range(len(self.kv_store[hash])):
            kv = self.kv_store[hash][i]
            if kv.key == key:
                value = kv.value
                del(self.kv_store[hash][i])
        return value

    def set(self, key, value):
        """
        Sets the value for a provided key.
        """
        hash = self.hash(key)
        key_found = False
        for kv in self.kv_store[hash]:
            if kv.key == key:
                key_found = True
                kv.value = value
        if not key_found:
            kv = KeyValue(key, value)
            self.kv_store[hash].append(kv)
        return True

    def size(self):
        """
        Returns the number of items in the HashTable.
        """
        return sum([len(hash) for hash in self.kv_store])

    def __repr__(self):
        return str(self.kv_store)


if __name__ == '__main__':
    print 'Initialize the HashTable'
    hash = HashTable()

    print 'Add and check values'

    print '> hash[\'Keith\'] = 555'
    hash['Keith'] = 555
    print hash['Keith']

    print '> hash.set(\'Jones\', \'123\')'
    hash.set('Jones', '123')
    print hash.get('Jones')

    print '> hash.set(\'Smith\', \'456\')'
    hash.set('Smith', '456')
    print hash.get('Smith')

    print '> hash.set(\'Smith\', \'XXX\')'
    hash.set("Smith", "XXX")
    print hash.get('Smith')

    print '> hash[\'Jones\'] = \'YYY\''
    hash['Jones'] = 'YYY'
    print hash['Jones']

    print '> print hash'
    print hash

    print '> print hash.size()'
    print hash.size()

    print '> del(hash[\'Smith\']'
    del(hash['Smith'])

    print '> hash.size()'
    print hash.size()

    print '> print hash'
    print hash

    print '> print hash.pop(\'Jones\')'
    print hash.pop('Jones')

    print '> print hash'
    print hash
