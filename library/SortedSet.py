# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
from math import sqrt, ceil
from bisect import bisect_left, bisect_right
from typing import Iterable, TypeVar, Union, Tuple
T = TypeVar('T')

"""
SortedSet
ソート済み列をいくつかのバケットに分割して管理します。このとき、(バケットの個数) : (バケット内の個数) = 1 : 50 くらいにします。(insert / erase の定数倍が軽く、バケット再構築の定数倍が重いため) あるバケットが空になったり、多すぎたりしたら、1 度まとめて、均等にバケットに分割します。 基本的に、要素の変更を伴う操作は O(√N) 、伴わない操作は O(log N) と思って良いです。

SortedSet(a=[])
iterable から SortedSet を作ります。重複がなく、かつソートされていれば O(N) 、そうでなければ O(N log N) です。

s.a
SortedSet の中身です。list の list になっていて、中には要素が昇順に並んでいます。各バケットには要素が存在することが保証されます。

len(s)
O(1)

x in s / x not in s
O(log N)

s.add(x)
x が s に含まれていなければ x を追加し、True を返します。O(√N) amotized / O(N) worst

s.discard(x)
x が s に含まれていれば x を削除し、True を返します。O(√N) amotized / O(N) worst
　　
s.lt(x) / s.le(x) / s.gt(x) / s.ge(x)
x より小さい / 以下 / より大きい / 以上で 最小 / 最大 の要素を返します。存在しなければ None をを返します。O(log N)

s.lower_bound(x) / s.upper_bound(x)
s.ge(x) / s.gt(x) で、要素を返す代わりにその要素がどのバケットの何番目にあるかを返します。存在しなければ (len(s.a), 0) をを返します。一度見つけた場所の周辺を走査するのに使ってください。add(x) / discard(x) 等でバケットの再構築が起こると壊れるので、再びこの関数で探し出す必要があります。O(log N)

s[x]
下から x 番目 / 上から ~x 番目 の要素を返します。存在しない場合は IndexError を返します。O(√N) (定数倍がとても小さい)

s[(i, j)]
i 番目のバケットの j 番目の要素を返します。存在しない場合は IndexError を返します。O(1)

s.index(x)
x が何番目かを返します。存在しない場合は ValueError を返します。O(√N) (定数倍がとても小さい) + O(log N)
"""

class SortedSet:
	BUCKET_RATIO = 50
	REBUILD_RATIO = 170

	@classmethod
	def _new_bucket_size(cls, size: int) -> int:
		return int(ceil(sqrt(size / cls.BUCKET_RATIO)))

	def _build(self, a: list):
		size = self.size = len(a)
		bucket_size = self._new_bucket_size(self.size)
		self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
	
	def __init__(self, a: Iterable = []):
		"Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
		a = list(a)
		if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
			a = sorted(set(a))
		self._build(a)

	def __iter__(self):
		for i in self.a:
			for j in i: yield j

	def __reversed__(self):
		for i in reversed(self.a):
			for j in reversed(i): yield j
	
	def __len__(self) -> int:
		return self.size
	
	def __repr__(self) -> str:
		return str(self.a)
	
	def __str__(self) -> str:
		s = str(list(self))
		return "{" + s[1 : len(s) - 1] + "}"

	def _bucket_index(self, x: T) -> int:
		"Find the index of the bucket which should contain x. / O(log N)"
		ok = -1
		ng = len(self.a)
		a = self.a
		while ng - ok > 1:
			mid = (ng + ok) >> 1
			if a[mid][0] <= x: ok = mid
			else: ng = mid
		if ok == -1: return 0
		if ng == len(self.a): return ok
		if a[ok][-1] < x:
			return ok + (len(a[ok]) > len(a[ok + 1]))
		return ok

	def __contains__(self, x: T) -> bool:
		"O(log N)"
		if self.size == 0: return False
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		return i != len(a) and a[i] == x

	def add(self, x: T) -> bool:
		"Add an element and return True if added. / O(N ** 0.5)"
		if self.size == 0:
			self._build([x])
			return True
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		if i != len(a) and a[i] == x: return False
		a.insert(i, x)
		self.size += 1
		if len(a) > len(self.a) * self.REBUILD_RATIO:
			self._build(list(self))
		return True

	def discard(self, x: T) -> bool:
		"Remove an element and return True if removed. / O(N ** 0.5)"
		if self.size == 0: return False
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		if i == len(a) or a[i] != x: return False
		a.pop(i)
		self.size -= 1
		if len(a) == 0:
			self._build(list(self))
		return True
	
	def lt(self, x: T) -> Union[T, None]:
		"Return the largest element < x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][0] >= x:
			return a[i - 1][-1] if i else None
		return a[i][bisect_left(a[i], x) - 1]

	def le(self, x: T) -> Union[T, None]:
		"Return the largest element <= x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][0] > x:
			return a[i - 1][-1] if i else None
		return a[i][bisect_right(a[i], x) - 1]

	def gt(self, x: T) -> Union[T, None]:
		"Return the smallest element > x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] <= x:
			return a[i + 1][0] if i + 1 < len(self.a) else None
		return a[i][bisect_right(a[i], x)]

	def ge(self, x: T) -> Union[T, None]:
		"Return the smallest element >= x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] < x:
			return a[i + 1][0] if i + 1 < len(self.a) else None
		return a[i][bisect_left(a[i], x)]
	
	def __getitem__(self, x: int) -> T:
		"Take (i, j) and return the j-th element in the i-th bucket, or IndexError if it doesn't exist. / O(1)"
		"Take x and return the x-th element, or IndexError if it doesn't exist. / O(N ** 0.5) (fast)"
		if isinstance(x, tuple):
			return self.a[x[0]][x[1]]
		if x < 0: x += self.size
		if x < 0 or x >= self.size: raise IndexError
		for a in self.a:
			if x < len(a): return a[x]
			x -= len(a)
		assert False
	
	def index(self, x: T) -> int:
		"Return the index of x, or ValueError if it doesn't exist. / O(N ** 0.5) (fast)"
		if self.size == 0: raise ValueError
		idx = self._bucket_index(x)
		a = self.a[idx]
		i = bisect_left(a, x)
		if i == len(a) or a[i] != x: raise ValueError
		for j in range(idx): i += len(self.a[j])
		return i

	def lower_bound(self, x: T) -> Tuple[int, int]:
		"Find the smallest element self.a[i][j] >= x and return (i, j), or (len(a), 0) if it doesn't exist. / O(log N)"
		if self.size == 0:
			return (0, 0)
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] < x:
			return (i + 1, 0)
		return (i, bisect_left(a[i], x))

	def upper_bound(self, x: T) -> Tuple[int, int]:
		"Find the smallest element self.a[i][j] > x and return (i, j), or (len(a), 0) if it doesn't exist. / O(log N)"
		if self.size == 0:
			return (0, 0)
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] <= x:
			return (i + 1, 0)
		return (i, bisect_right(a[i], x))