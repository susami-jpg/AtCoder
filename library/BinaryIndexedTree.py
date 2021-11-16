
#1-indexなので注意
#sum
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def get(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_


#1-indexなので注意
#max
class Bit_max:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def get(self, i):
        s = 0
        while i > 0:
            s = max(s, self.tree[i])
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = max(self.tree[i], x)
            i += i & -i
 
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ = max(sum_, self.tree[k])
                pos += 1 << i
        return pos + 1, sum_

#1-indexなので注意
#min
class Bit_min:
    def __init__(self, n):
        self.size = n
        self.tree = [10**15] * (n + 1)
        self.depth = n.bit_length()
 
    def get(self, i):
        s = 0
        while i > 0:
            s = min(s, self.tree[i])
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = min(self.tree[i], x)
            i += i & -i
 
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ = min(sum_, self.tree[k])
                pos += 1 << i
        return pos + 1, sum_