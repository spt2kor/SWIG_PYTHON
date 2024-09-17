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
    from . import _Perl5ToCpp
else:
    import _Perl5ToCpp

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



def new_intp():
    return _Perl5ToCpp.new_intp()

def copy_intp(value):
    return _Perl5ToCpp.copy_intp(value)

def delete_intp(obj):
    return _Perl5ToCpp.delete_intp(obj)

def intp_assign(obj, value):
    return _Perl5ToCpp.intp_assign(obj, value)

def intp_value(obj):
    return _Perl5ToCpp.intp_value(obj)

def new_double_p():
    return _Perl5ToCpp.new_double_p()

def copy_double_p(value):
    return _Perl5ToCpp.copy_double_p(value)

def delete_double_p(obj):
    return _Perl5ToCpp.delete_double_p(obj)

def double_p_assign(obj, value):
    return _Perl5ToCpp.double_p_assign(obj, value)

def double_p_value(obj):
    return _Perl5ToCpp.double_p_value(obj)

def add(x, y):
    return _Perl5ToCpp.add(x, y)
class Add(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    m_x = property(_Perl5ToCpp.Add_m_x_get, _Perl5ToCpp.Add_m_x_set)
    m_y = property(_Perl5ToCpp.Add_m_y_get, _Perl5ToCpp.Add_m_y_set)
    m_sum = property(_Perl5ToCpp.Add_m_sum_get, _Perl5ToCpp.Add_m_sum_set)

    def add(self, x, y):
        return _Perl5ToCpp.Add_add(self, x, y)

    def __init__(self):
        _Perl5ToCpp.Add_swiginit(self, _Perl5ToCpp.new_Add())
    __swig_destroy__ = _Perl5ToCpp.delete_Add

# Register Add in _Perl5ToCpp:
_Perl5ToCpp.Add_swigregister(Add)

class Callback(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _Perl5ToCpp.Callback_swiginit(self, _Perl5ToCpp.new_Callback())
    __swig_destroy__ = _Perl5ToCpp.delete_Callback

    def run(self):
        return _Perl5ToCpp.Callback_run(self)

    def baseName(self):
        return _Perl5ToCpp.Callback_baseName(self)

# Register Callback in _Perl5ToCpp:
_Perl5ToCpp.Callback_swigregister(Callback)

class Caller(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _Perl5ToCpp.Caller_swiginit(self, _Perl5ToCpp.new_Caller())
    __swig_destroy__ = _Perl5ToCpp.delete_Caller

    def delCallback(self):
        return _Perl5ToCpp.Caller_delCallback(self)

    def setCallback(self, cb):
        return _Perl5ToCpp.Caller_setCallback(self, cb)

    def call(self):
        return _Perl5ToCpp.Caller_call(self)

# Register Caller in _Perl5ToCpp:
_Perl5ToCpp.Caller_swigregister(Caller)



