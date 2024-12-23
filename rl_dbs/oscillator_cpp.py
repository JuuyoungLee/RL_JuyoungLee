# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_oscillator_cpp')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_oscillator_cpp')
    _oscillator_cpp = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_oscillator_cpp', [dirname(__file__)])
        except ImportError:
            import _oscillator_cpp
            return _oscillator_cpp
        try:
            _mod = imp.load_module('_oscillator_cpp', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _oscillator_cpp = swig_import_helper()
    del swig_import_helper
else:
    import _oscillator_cpp
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def BvdP(t, y, ydot):
    return _oscillator_cpp.BvdP(t, y, ydot)
BvdP = _oscillator_cpp.BvdP

def Pertrubation(y, dkick):
    return _oscillator_cpp.Pertrubation(y, dkick)
Pertrubation = _oscillator_cpp.Pertrubation

def Make_step(y):
    return _oscillator_cpp.Make_step(y)
Make_step = _oscillator_cpp.Make_step

def init(nosc_, epsilon_, frrms_):
    return _oscillator_cpp.init(nosc_, epsilon_, frrms_)
init = _oscillator_cpp.init

def Calc_mfx(y):
    return _oscillator_cpp.Calc_mfx(y)
Calc_mfx = _oscillator_cpp.Calc_mfx

def Calc_mfy(y):
    return _oscillator_cpp.Calc_mfy(y)
Calc_mfy = _oscillator_cpp.Calc_mfy
class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _oscillator_cpp.new_doubleArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _oscillator_cpp.delete_doubleArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _oscillator_cpp.doubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _oscillator_cpp.doubleArray___setitem__(self, index, value)

    def cast(self):
        return _oscillator_cpp.doubleArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_oscillator_cpp.doubleArray_frompointer)
    else:
        frompointer = _oscillator_cpp.doubleArray_frompointer
doubleArray_swigregister = _oscillator_cpp.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(t):
    return _oscillator_cpp.doubleArray_frompointer(t)
doubleArray_frompointer = _oscillator_cpp.doubleArray_frompointer


def new_doubleP():
    return _oscillator_cpp.new_doubleP()
new_doubleP = _oscillator_cpp.new_doubleP

def copy_doubleP(value):
    return _oscillator_cpp.copy_doubleP(value)
copy_doubleP = _oscillator_cpp.copy_doubleP

def delete_doubleP(obj):
    return _oscillator_cpp.delete_doubleP(obj)
delete_doubleP = _oscillator_cpp.delete_doubleP

def doubleP_assign(obj, value):
    return _oscillator_cpp.doubleP_assign(obj, value)
doubleP_assign = _oscillator_cpp.doubleP_assign

def doubleP_value(obj):
    return _oscillator_cpp.doubleP_value(obj)
doubleP_value = _oscillator_cpp.doubleP_value
# This file is compatible with both classic and new-style classes.


