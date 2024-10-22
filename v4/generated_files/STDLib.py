# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _STDLib
else:
    import _STDLib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def UpdateStr(perltxt):
    return _STDLib.UpdateStr(perltxt)

def PrintStr(perltxt):
    return _STDLib.PrintStr(perltxt)

def changePerlStr(perltxt):
    return _STDLib.changePerlStr(perltxt)

def changePerlStrPtr(perltxt):
    return _STDLib.changePerlStrPtr(perltxt)
class StrTest(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    m_perltxt = property(_STDLib.StrTest_m_perltxt_get, _STDLib.StrTest_m_perltxt_set)

    def __init__(self):
        _STDLib.StrTest_swiginit(self, _STDLib.new_StrTest())
    __swig_destroy__ = _STDLib.delete_StrTest

    def UpdateStr(self, perltxt):
        return _STDLib.StrTest_UpdateStr(self, perltxt)

# Register StrTest in _STDLib:
_STDLib.StrTest_swigregister(StrTest)
cvar = _STDLib.cvar
fileName = cvar.fileName
StrTest.m_fileName = _STDLib.cvar.StrTest_m_fileName

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _STDLib.delete_SwigPyIterator

    def value(self):
        return _STDLib.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _STDLib.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _STDLib.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _STDLib.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _STDLib.SwigPyIterator_equal(self, x)

    def copy(self):
        return _STDLib.SwigPyIterator_copy(self)

    def next(self):
        return _STDLib.SwigPyIterator_next(self)

    def __next__(self):
        return _STDLib.SwigPyIterator___next__(self)

    def previous(self):
        return _STDLib.SwigPyIterator_previous(self)

    def advance(self, n):
        return _STDLib.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _STDLib.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _STDLib.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _STDLib.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _STDLib.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _STDLib.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _STDLib.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _STDLib:
_STDLib.SwigPyIterator_swigregister(SwigPyIterator)

class vectori(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _STDLib.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _STDLib.vectori___nonzero__(self)

    def __bool__(self):
        return _STDLib.vectori___bool__(self)

    def __len__(self):
        return _STDLib.vectori___len__(self)

    def __getslice__(self, i, j):
        return _STDLib.vectori___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _STDLib.vectori___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _STDLib.vectori___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _STDLib.vectori___delitem__(self, *args)

    def __getitem__(self, *args):
        return _STDLib.vectori___getitem__(self, *args)

    def __setitem__(self, *args):
        return _STDLib.vectori___setitem__(self, *args)

    def pop(self):
        return _STDLib.vectori_pop(self)

    def append(self, x):
        return _STDLib.vectori_append(self, x)

    def empty(self):
        return _STDLib.vectori_empty(self)

    def size(self):
        return _STDLib.vectori_size(self)

    def swap(self, v):
        return _STDLib.vectori_swap(self, v)

    def begin(self):
        return _STDLib.vectori_begin(self)

    def end(self):
        return _STDLib.vectori_end(self)

    def rbegin(self):
        return _STDLib.vectori_rbegin(self)

    def rend(self):
        return _STDLib.vectori_rend(self)

    def clear(self):
        return _STDLib.vectori_clear(self)

    def get_allocator(self):
        return _STDLib.vectori_get_allocator(self)

    def pop_back(self):
        return _STDLib.vectori_pop_back(self)

    def erase(self, *args):
        return _STDLib.vectori_erase(self, *args)

    def __init__(self, *args):
        _STDLib.vectori_swiginit(self, _STDLib.new_vectori(*args))

    def push_back(self, x):
        return _STDLib.vectori_push_back(self, x)

    def front(self):
        return _STDLib.vectori_front(self)

    def back(self):
        return _STDLib.vectori_back(self)

    def assign(self, n, x):
        return _STDLib.vectori_assign(self, n, x)

    def resize(self, *args):
        return _STDLib.vectori_resize(self, *args)

    def insert(self, *args):
        return _STDLib.vectori_insert(self, *args)

    def reserve(self, n):
        return _STDLib.vectori_reserve(self, n)

    def capacity(self):
        return _STDLib.vectori_capacity(self)
    __swig_destroy__ = _STDLib.delete_vectori

# Register vectori in _STDLib:
_STDLib.vectori_swigregister(vectori)

class vectord(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _STDLib.vectord_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _STDLib.vectord___nonzero__(self)

    def __bool__(self):
        return _STDLib.vectord___bool__(self)

    def __len__(self):
        return _STDLib.vectord___len__(self)

    def __getslice__(self, i, j):
        return _STDLib.vectord___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _STDLib.vectord___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _STDLib.vectord___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _STDLib.vectord___delitem__(self, *args)

    def __getitem__(self, *args):
        return _STDLib.vectord___getitem__(self, *args)

    def __setitem__(self, *args):
        return _STDLib.vectord___setitem__(self, *args)

    def pop(self):
        return _STDLib.vectord_pop(self)

    def append(self, x):
        return _STDLib.vectord_append(self, x)

    def empty(self):
        return _STDLib.vectord_empty(self)

    def size(self):
        return _STDLib.vectord_size(self)

    def swap(self, v):
        return _STDLib.vectord_swap(self, v)

    def begin(self):
        return _STDLib.vectord_begin(self)

    def end(self):
        return _STDLib.vectord_end(self)

    def rbegin(self):
        return _STDLib.vectord_rbegin(self)

    def rend(self):
        return _STDLib.vectord_rend(self)

    def clear(self):
        return _STDLib.vectord_clear(self)

    def get_allocator(self):
        return _STDLib.vectord_get_allocator(self)

    def pop_back(self):
        return _STDLib.vectord_pop_back(self)

    def erase(self, *args):
        return _STDLib.vectord_erase(self, *args)

    def __init__(self, *args):
        _STDLib.vectord_swiginit(self, _STDLib.new_vectord(*args))

    def push_back(self, x):
        return _STDLib.vectord_push_back(self, x)

    def front(self):
        return _STDLib.vectord_front(self)

    def back(self):
        return _STDLib.vectord_back(self)

    def assign(self, n, x):
        return _STDLib.vectord_assign(self, n, x)

    def resize(self, *args):
        return _STDLib.vectord_resize(self, *args)

    def insert(self, *args):
        return _STDLib.vectord_insert(self, *args)

    def reserve(self, n):
        return _STDLib.vectord_reserve(self, n)

    def capacity(self):
        return _STDLib.vectord_capacity(self)
    __swig_destroy__ = _STDLib.delete_vectord

# Register vectord in _STDLib:
_STDLib.vectord_swigregister(vectord)


def average(v):
    return _STDLib.average(v)

def half(v):
    return _STDLib.half(v)

def halve_in_place(v):
    return _STDLib.halve_in_place(v)
class map_ii(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _STDLib.map_ii_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _STDLib.map_ii___nonzero__(self)

    def __bool__(self):
        return _STDLib.map_ii___bool__(self)

    def __len__(self):
        return _STDLib.map_ii___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _STDLib.map_ii___getitem__(self, key)

    def __delitem__(self, key):
        return _STDLib.map_ii___delitem__(self, key)

    def has_key(self, key):
        return _STDLib.map_ii_has_key(self, key)

    def keys(self):
        return _STDLib.map_ii_keys(self)

    def values(self):
        return _STDLib.map_ii_values(self)

    def items(self):
        return _STDLib.map_ii_items(self)

    def __contains__(self, key):
        return _STDLib.map_ii___contains__(self, key)

    def key_iterator(self):
        return _STDLib.map_ii_key_iterator(self)

    def value_iterator(self):
        return _STDLib.map_ii_value_iterator(self)

    def __setitem__(self, *args):
        return _STDLib.map_ii___setitem__(self, *args)

    def asdict(self):
        return _STDLib.map_ii_asdict(self)

    def __init__(self, *args):
        _STDLib.map_ii_swiginit(self, _STDLib.new_map_ii(*args))

    def empty(self):
        return _STDLib.map_ii_empty(self)

    def size(self):
        return _STDLib.map_ii_size(self)

    def swap(self, v):
        return _STDLib.map_ii_swap(self, v)

    def begin(self):
        return _STDLib.map_ii_begin(self)

    def end(self):
        return _STDLib.map_ii_end(self)

    def rbegin(self):
        return _STDLib.map_ii_rbegin(self)

    def rend(self):
        return _STDLib.map_ii_rend(self)

    def clear(self):
        return _STDLib.map_ii_clear(self)

    def get_allocator(self):
        return _STDLib.map_ii_get_allocator(self)

    def count(self, x):
        return _STDLib.map_ii_count(self, x)

    def erase(self, *args):
        return _STDLib.map_ii_erase(self, *args)

    def find(self, x):
        return _STDLib.map_ii_find(self, x)

    def lower_bound(self, x):
        return _STDLib.map_ii_lower_bound(self, x)

    def upper_bound(self, x):
        return _STDLib.map_ii_upper_bound(self, x)
    __swig_destroy__ = _STDLib.delete_map_ii

# Register map_ii in _STDLib:
_STDLib.map_ii_swigregister(map_ii)

class map_sd(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _STDLib.map_sd_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _STDLib.map_sd___nonzero__(self)

    def __bool__(self):
        return _STDLib.map_sd___bool__(self)

    def __len__(self):
        return _STDLib.map_sd___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _STDLib.map_sd___getitem__(self, key)

    def __delitem__(self, key):
        return _STDLib.map_sd___delitem__(self, key)

    def has_key(self, key):
        return _STDLib.map_sd_has_key(self, key)

    def keys(self):
        return _STDLib.map_sd_keys(self)

    def values(self):
        return _STDLib.map_sd_values(self)

    def items(self):
        return _STDLib.map_sd_items(self)

    def __contains__(self, key):
        return _STDLib.map_sd___contains__(self, key)

    def key_iterator(self):
        return _STDLib.map_sd_key_iterator(self)

    def value_iterator(self):
        return _STDLib.map_sd_value_iterator(self)

    def __setitem__(self, *args):
        return _STDLib.map_sd___setitem__(self, *args)

    def asdict(self):
        return _STDLib.map_sd_asdict(self)

    def __init__(self, *args):
        _STDLib.map_sd_swiginit(self, _STDLib.new_map_sd(*args))

    def empty(self):
        return _STDLib.map_sd_empty(self)

    def size(self):
        return _STDLib.map_sd_size(self)

    def swap(self, v):
        return _STDLib.map_sd_swap(self, v)

    def begin(self):
        return _STDLib.map_sd_begin(self)

    def end(self):
        return _STDLib.map_sd_end(self)

    def rbegin(self):
        return _STDLib.map_sd_rbegin(self)

    def rend(self):
        return _STDLib.map_sd_rend(self)

    def clear(self):
        return _STDLib.map_sd_clear(self)

    def get_allocator(self):
        return _STDLib.map_sd_get_allocator(self)

    def count(self, x):
        return _STDLib.map_sd_count(self, x)

    def erase(self, *args):
        return _STDLib.map_sd_erase(self, *args)

    def find(self, x):
        return _STDLib.map_sd_find(self, x)

    def lower_bound(self, x):
        return _STDLib.map_sd_lower_bound(self, x)

    def upper_bound(self, x):
        return _STDLib.map_sd_upper_bound(self, x)
    __swig_destroy__ = _STDLib.delete_map_sd

# Register map_sd in _STDLib:
_STDLib.map_sd_swigregister(map_sd)


def printMapII(mp):
    return _STDLib.printMapII(mp)

def printMapSD(mp):
    return _STDLib.printMapSD(mp)

def PrintMapCR(mp):
    return _STDLib.PrintMapCR(mp)


