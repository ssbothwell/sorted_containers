"""
Sorted dictionary stubfile.
"""

from typing import TypeVar, Dict, Any, Iterator, Sequence, Tuple, Union, List

from collections import Set, Sequence
from collections import KeysView as AbstractKeysView
from collections import ValuesView as AbstractValuesView
from collections import ItemsView as AbstractItemsView
from sys import hexversion

from .sortedlist import SortedList, recursive_repr, SortedListWithKey
from .sortedset import SortedSet

T = TypeVar('T')

NONE = object()


class _IlocWrapper(object):
    def __init__(self, _dict: dict) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> T: ...
    def __delitem__(self, index: int) -> None: ...


class SortedDict(Dict):
    def __init__(self, *args: list, **kwargs: Dict) -> None: ...
    def key(self) -> Any: ...
    def clear(self) -> None: ...
    def __delitem__(self, key: int) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __reversed__(self) -> Iterator: ...
    def __setitem__(self, key: int, value: T) -> None: ...
    def copy(self) -> SortedDict: ...
    # fromkeys wont check even with Any types
    def fromkeys(cls, seq, value=None): ...
    def items(self) -> Union[ItemsView, Any]: ...
    def iteritems(self) -> Iterator[Tuple[int, T]]: ...
    def keys(self) -> Union[KeysView, Any]: ...
    def iterkeys(self) -> Iterator[int]: ...
    def values(self) -> Union[ValuesView, Any]: ...
    def itervalues(self) -> Iterator[T]: ...
    def pop(self, key: int, default: Any=NONE) -> T: ...
    def popitem(self, last: bool=True) -> Tuple[int, T]: ...
    def peekitem(self, index: int=-1) -> Tuple[int, T]: ...
    def setdefault(self, key: int, default: Any=None) -> Any: ...
    def update(self, *args: Any, **kwargs: dict) -> None: ...
    def viewkeys(self) -> KeysView: ...
    def viewvalues(self) -> ValuesView: ...
    def viewitems(self) -> ItemsView: ...
    # Cannot specify __reduce__ without violating Liskovs
    def __reduce__(self) -> Any: ...
    def __repr__(self) -> str: ...
    def _check(self) -> None: ...


class KeysView(AbstractKeysView, Set, Sequence):
    def __init__(self, sorted_dict: SortedDict) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: Any) -> bool: ...
    def __iter__(self) -> Iterator: ...
    # Cannot specify getitem without violating Liskovs
    def __getitem__(self, index: Any) -> Any: ...
    def __reversed__(self) -> Iterator: ...
    def index(self, value: T, start: int=None, stop: int=None) -> T: ...
    def count(self, value: T) -> int: ...
    def __eq__(self, that: Any) -> bool: ...
    def __ne__(self, that: Any) -> bool: ...
    def __lt__(self, that: Any) -> bool: ...
    def __gt__(self, that: Any) -> bool: ...
    def __le__(self, that: Any) -> bool: ...
    def __ge__(self, that: Any) -> bool: ...
    def __and__(self, that: Any) -> Any: ...
    def __or__(self, that: Any) -> Any: ...
    def __sub__(self, that: Any) -> Any: ...
    def __xor__(self, that: Any) -> Any: ...
    def isdisjoint(self, that: Any) -> bool: ...
    def __repr__(self) -> Any: ...


class ValuesView(AbstractValuesView, Sequence):
    def __init__(self, sorted_dict: SortedDict) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, value: Any) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __getitem__(self, index: Any) -> Any: ...
    def __reversed__(self) -> Iterator: ...
    def index(self, value): ...
    def __lt__(self, that: Any) -> bool: ...
    def __gt__(self, that: Any) -> bool: ...
    def __le__(self, that: Any) -> bool: ...
    def __ge__(self, that: Any) -> bool: ...
    def __and__(self, that: Any) -> Any: ...
    def __or__(self, that: Any) -> Any: ...
    def __sub__(self, that: Any) -> Any: ...
    def __xor__(self, that: Any) -> Any: ...
    def __repr__(self) -> Any: ...


class ItemsView(AbstractItemsView, Set, Sequence):
    def __init__(self, sorted_dict: SortedDict) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: Any) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __getitem__(self, index: Any) -> T: ...
    def __reversed__(self) -> Iterator: ...
    def index(self, value: T, start: int=None, stop: int=None) -> T: ...
    def count(self, item: T) -> int: ...
    def __eq__(self, that: Any) -> bool: ...
    def __ne__(self, that: Any) -> bool: ...
    def __lt__(self, that: Any) -> bool: ...
    def __gt__(self, that: Any) -> bool: ...
    def __le__(self, that: Any) -> bool: ...
    def __ge__(self, that: Any) -> bool: ...
    def __and__(self, that: Any) -> Any: ...
    def __or__(self, that: Any) -> Any: ...
    def __sub__(self, that: Any) -> Any: ...
    def __xor__(self, that: Any) -> Any: ...
    def __repr__(self) -> Any: ...
