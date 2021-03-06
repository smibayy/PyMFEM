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
    from . import _solvers
else:
    import _solvers

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

import mfem._ser.vector
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.sparsemat
import mfem._ser.densemat
class IterativeSolver(mfem._ser.operators.Solver):
    r"""Proxy of C++ mfem::IterativeSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetRelTol(self, rtol):
        r"""SetRelTol(IterativeSolver self, double rtol)"""
        return _solvers.IterativeSolver_SetRelTol(self, rtol)

    def SetAbsTol(self, atol):
        r"""SetAbsTol(IterativeSolver self, double atol)"""
        return _solvers.IterativeSolver_SetAbsTol(self, atol)

    def SetMaxIter(self, max_it):
        r"""SetMaxIter(IterativeSolver self, int max_it)"""
        return _solvers.IterativeSolver_SetMaxIter(self, max_it)

    def SetPrintLevel(self, print_lvl):
        r"""SetPrintLevel(IterativeSolver self, int print_lvl)"""
        return _solvers.IterativeSolver_SetPrintLevel(self, print_lvl)

    def GetNumIterations(self):
        r"""GetNumIterations(IterativeSolver self) -> int"""
        return _solvers.IterativeSolver_GetNumIterations(self)

    def GetConverged(self):
        r"""GetConverged(IterativeSolver self) -> int"""
        return _solvers.IterativeSolver_GetConverged(self)

    def GetFinalNorm(self):
        r"""GetFinalNorm(IterativeSolver self) -> double"""
        return _solvers.IterativeSolver_GetFinalNorm(self)

    def SetPreconditioner(self, pr):
        r"""SetPreconditioner(IterativeSolver self, Solver pr)"""
        return _solvers.IterativeSolver_SetPreconditioner(self, pr)

    def SetOperator(self, op):
        r"""SetOperator(IterativeSolver self, Operator op)"""
        return _solvers.IterativeSolver_SetOperator(self, op)
    __swig_destroy__ = _solvers.delete_IterativeSolver

# Register IterativeSolver in _solvers:
_solvers.IterativeSolver_swigregister(IterativeSolver)

class SLISolver(IterativeSolver):
    r"""Proxy of C++ mfem::SLISolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(SLISolver self) -> SLISolver"""
        _solvers.SLISolver_swiginit(self, _solvers.new_SLISolver())

    def SetOperator(self, op):
        r"""SetOperator(SLISolver self, Operator op)"""
        return _solvers.SLISolver_SetOperator(self, op)

    def Mult(self, b, x):
        r"""Mult(SLISolver self, Vector b, Vector x)"""
        return _solvers.SLISolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_SLISolver

# Register SLISolver in _solvers:
_solvers.SLISolver_swigregister(SLISolver)


def SLI(*args):
    r"""
    SLI(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)
    SLI(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)
    """
    return _solvers.SLI(*args)
class CGSolver(IterativeSolver):
    r"""Proxy of C++ mfem::CGSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(CGSolver self) -> CGSolver"""
        _solvers.CGSolver_swiginit(self, _solvers.new_CGSolver())

    def SetOperator(self, op):
        r"""SetOperator(CGSolver self, Operator op)"""
        return _solvers.CGSolver_SetOperator(self, op)

    def Mult(self, b, x):
        r"""Mult(CGSolver self, Vector b, Vector x)"""
        return _solvers.CGSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_CGSolver

# Register CGSolver in _solvers:
_solvers.CGSolver_swigregister(CGSolver)


def CG(A, b, x, print_iter=0, max_num_iter=1000, RTOLERANCE=1e-12, ATOLERANCE=1e-24):
    r"""CG(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)"""
    return _solvers.CG(A, b, x, print_iter, max_num_iter, RTOLERANCE, ATOLERANCE)

def PCG(A, B, b, x, print_iter=0, max_num_iter=1000, RTOLERANCE=1e-12, ATOLERANCE=1e-24):
    r"""PCG(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)"""
    return _solvers.PCG(A, B, b, x, print_iter, max_num_iter, RTOLERANCE, ATOLERANCE)
class GMRESSolver(IterativeSolver):
    r"""Proxy of C++ mfem::GMRESSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(GMRESSolver self) -> GMRESSolver"""
        _solvers.GMRESSolver_swiginit(self, _solvers.new_GMRESSolver())

    def SetKDim(self, dim):
        r"""SetKDim(GMRESSolver self, int dim)"""
        return _solvers.GMRESSolver_SetKDim(self, dim)

    def Mult(self, b, x):
        r"""Mult(GMRESSolver self, Vector b, Vector x)"""
        return _solvers.GMRESSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_GMRESSolver

# Register GMRESSolver in _solvers:
_solvers.GMRESSolver_swigregister(GMRESSolver)

class FGMRESSolver(IterativeSolver):
    r"""Proxy of C++ mfem::FGMRESSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(FGMRESSolver self) -> FGMRESSolver"""
        _solvers.FGMRESSolver_swiginit(self, _solvers.new_FGMRESSolver())

    def SetKDim(self, dim):
        r"""SetKDim(FGMRESSolver self, int dim)"""
        return _solvers.FGMRESSolver_SetKDim(self, dim)

    def Mult(self, b, x):
        r"""Mult(FGMRESSolver self, Vector b, Vector x)"""
        return _solvers.FGMRESSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_FGMRESSolver

# Register FGMRESSolver in _solvers:
_solvers.FGMRESSolver_swigregister(FGMRESSolver)


def GMRES(*args):
    r"""
    GMRES(Operator A, Vector x, Vector b, Solver M, int & max_iter, int m, double & tol, double atol, int printit) -> int
    GMRES(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, int m=50, double rtol=1e-12, double atol=1e-24)
    """
    return _solvers.GMRES(*args)
class BiCGSTABSolver(IterativeSolver):
    r"""Proxy of C++ mfem::BiCGSTABSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(BiCGSTABSolver self) -> BiCGSTABSolver"""
        _solvers.BiCGSTABSolver_swiginit(self, _solvers.new_BiCGSTABSolver())

    def SetOperator(self, op):
        r"""SetOperator(BiCGSTABSolver self, Operator op)"""
        return _solvers.BiCGSTABSolver_SetOperator(self, op)

    def Mult(self, b, x):
        r"""Mult(BiCGSTABSolver self, Vector b, Vector x)"""
        return _solvers.BiCGSTABSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_BiCGSTABSolver

# Register BiCGSTABSolver in _solvers:
_solvers.BiCGSTABSolver_swigregister(BiCGSTABSolver)


def BiCGSTAB(*args):
    r"""
    BiCGSTAB(Operator A, Vector x, Vector b, Solver M, int & max_iter, double & tol, double atol, int printit) -> int
    BiCGSTAB(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double rtol=1e-12, double atol=1e-24)
    """
    return _solvers.BiCGSTAB(*args)
class MINRESSolver(IterativeSolver):
    r"""Proxy of C++ mfem::MINRESSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(MINRESSolver self) -> MINRESSolver"""
        _solvers.MINRESSolver_swiginit(self, _solvers.new_MINRESSolver())

    def SetPreconditioner(self, pr):
        r"""SetPreconditioner(MINRESSolver self, Solver pr)"""
        return _solvers.MINRESSolver_SetPreconditioner(self, pr)

    def SetOperator(self, op):
        r"""SetOperator(MINRESSolver self, Operator op)"""
        return _solvers.MINRESSolver_SetOperator(self, op)

    def Mult(self, b, x):
        r"""Mult(MINRESSolver self, Vector b, Vector x)"""
        return _solvers.MINRESSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_MINRESSolver

# Register MINRESSolver in _solvers:
_solvers.MINRESSolver_swigregister(MINRESSolver)


def MINRES(*args):
    r"""
    MINRES(Operator A, Vector b, Vector x, int print_it=0, int max_it=1000, double rtol=1e-12, double atol=1e-24)
    MINRES(Operator A, Solver B, Vector b, Vector x, int print_it=0, int max_it=1000, double rtol=1e-12, double atol=1e-24)
    """
    return _solvers.MINRES(*args)
class NewtonSolver(IterativeSolver):
    r"""Proxy of C++ mfem::NewtonSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(NewtonSolver self) -> NewtonSolver"""
        _solvers.NewtonSolver_swiginit(self, _solvers.new_NewtonSolver())

    def SetOperator(self, op):
        r"""SetOperator(NewtonSolver self, Operator op)"""
        return _solvers.NewtonSolver_SetOperator(self, op)

    def SetSolver(self, solver):
        r"""SetSolver(NewtonSolver self, Solver solver)"""
        return _solvers.NewtonSolver_SetSolver(self, solver)

    def Mult(self, b, x):
        r"""Mult(NewtonSolver self, Vector b, Vector x)"""
        return _solvers.NewtonSolver_Mult(self, b, x)

    def ComputeScalingFactor(self, x, b):
        r"""ComputeScalingFactor(NewtonSolver self, Vector x, Vector b) -> double"""
        return _solvers.NewtonSolver_ComputeScalingFactor(self, x, b)
    __swig_destroy__ = _solvers.delete_NewtonSolver

# Register NewtonSolver in _solvers:
_solvers.NewtonSolver_swigregister(NewtonSolver)


def aGMRES(A, x, b, M, max_iter, m_max, m_min, m_step, cf, tol, atol, printit):
    r"""aGMRES(Operator A, Vector x, Vector b, Operator M, int & max_iter, int m_max, int m_min, int m_step, double cf, double & tol, double & atol, int printit) -> int"""
    return _solvers.aGMRES(A, x, b, M, max_iter, m_max, m_min, m_step, cf, tol, atol, printit)
class SLBQPOptimizer(IterativeSolver):
    r"""Proxy of C++ mfem::SLBQPOptimizer class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(SLBQPOptimizer self) -> SLBQPOptimizer"""
        _solvers.SLBQPOptimizer_swiginit(self, _solvers.new_SLBQPOptimizer())

    def SetBounds(self, _lo, _hi):
        r"""SetBounds(SLBQPOptimizer self, Vector _lo, Vector _hi)"""
        return _solvers.SLBQPOptimizer_SetBounds(self, _lo, _hi)

    def SetLinearConstraint(self, _w, _a):
        r"""SetLinearConstraint(SLBQPOptimizer self, Vector _w, double _a)"""
        return _solvers.SLBQPOptimizer_SetLinearConstraint(self, _w, _a)

    def Mult(self, xt, x):
        r"""Mult(SLBQPOptimizer self, Vector xt, Vector x)"""
        return _solvers.SLBQPOptimizer_Mult(self, xt, x)

    def SetPreconditioner(self, pr):
        r"""SetPreconditioner(SLBQPOptimizer self, Solver pr)"""
        return _solvers.SLBQPOptimizer_SetPreconditioner(self, pr)

    def SetOperator(self, op):
        r"""SetOperator(SLBQPOptimizer self, Operator op)"""
        return _solvers.SLBQPOptimizer_SetOperator(self, op)
    __swig_destroy__ = _solvers.delete_SLBQPOptimizer

# Register SLBQPOptimizer in _solvers:
_solvers.SLBQPOptimizer_swigregister(SLBQPOptimizer)



