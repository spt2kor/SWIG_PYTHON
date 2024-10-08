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
    from . import _INHRT
else:
    import _INHRT

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


import weakref

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _INHRT.delete_SwigPyIterator

    def value(self):
        return _INHRT.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _INHRT.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _INHRT.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _INHRT.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _INHRT.SwigPyIterator_equal(self, x)

    def copy(self):
        return _INHRT.SwigPyIterator_copy(self)

    def next(self):
        return _INHRT.SwigPyIterator_next(self)

    def __next__(self):
        return _INHRT.SwigPyIterator___next__(self)

    def previous(self):
        return _INHRT.SwigPyIterator_previous(self)

    def advance(self, n):
        return _INHRT.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _INHRT.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _INHRT.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _INHRT.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _INHRT.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _INHRT.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _INHRT.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _INHRT:
_INHRT.SwigPyIterator_swigregister(SwigPyIterator)

class Employee(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, n):
        if self.__class__ == Employee:
            _self = None
        else:
            _self = self
        _INHRT.Employee_swiginit(self, _INHRT.new_Employee(_self, n))

    def getTitle(self):
        return _INHRT.Employee_getTitle(self)

    def getName(self):
        return _INHRT.Employee_getName(self)

    def getPosition(self):
        return _INHRT.Employee_getPosition(self)
    __swig_destroy__ = _INHRT.delete_Employee
    def __disown__(self):
        self.this.disown()
        _INHRT.disown_Employee(self)
        return weakref.proxy(self)

# Register Employee in _INHRT:
_INHRT.Employee_swigregister(Employee)

class Manager(Employee):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, n):
        if self.__class__ == Manager:
            _self = None
        else:
            _self = self
        _INHRT.Manager_swiginit(self, _INHRT.new_Manager(_self, n))

    def getPosition(self):
        return _INHRT.Manager_getPosition(self)
    __swig_destroy__ = _INHRT.delete_Manager
    def __disown__(self):
        self.this.disown()
        _INHRT.disown_Manager(self)
        return weakref.proxy(self)

# Register Manager in _INHRT:
_INHRT.Manager_swigregister(Manager)

class EmployeeList(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _INHRT.EmployeeList_swiginit(self, _INHRT.new_EmployeeList())

    def addEmployee(self, p):
        return _INHRT.EmployeeList_addEmployee(self, p)

    def get_item(self, i):
        return _INHRT.EmployeeList_get_item(self, i)
    __swig_destroy__ = _INHRT.delete_EmployeeList

# Register EmployeeList in _INHRT:
_INHRT.EmployeeList_swigregister(EmployeeList)



