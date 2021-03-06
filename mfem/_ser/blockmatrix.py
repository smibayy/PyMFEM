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
    from . import _blockmatrix
else:
    import _blockmatrix

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

import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.sparsemat
import mfem._ser.densemat
class BlockMatrix(mfem._ser.matrix.AbstractSparseMatrix):
    r"""Proxy of C++ mfem::BlockMatrix class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(BlockMatrix self, intArray offsets) -> BlockMatrix
        __init__(BlockMatrix self, intArray row_offsets, intArray col_offsets) -> BlockMatrix
        """
        _blockmatrix.BlockMatrix_swiginit(self, _blockmatrix.new_BlockMatrix(*args))

        from mfem.ser import intArray  
        if len(args) == 1:
           if isinstance(args[0], intArray):
               self._offsets = args[0]
        if len(args) == 2:
           if (isinstance(args[0], intArray) and
               isinstance(args[1], intArray)):
               self._offsets = (args[0], args[1])




    def SetBlock(self, i, j, mat):
        r"""SetBlock(BlockMatrix self, int i, int j, SparseMatrix mat)"""
        val = _blockmatrix.BlockMatrix_SetBlock(self, i, j, mat)

        if not hasattr(self, '_linked_mat'):
           self._linked_mat = {}
        self._linked_mat[i, j] = mat


        return val


    def NumRowBlocks(self):
        r"""NumRowBlocks(BlockMatrix self) -> int"""
        return _blockmatrix.BlockMatrix_NumRowBlocks(self)

    def NumColBlocks(self):
        r"""NumColBlocks(BlockMatrix self) -> int"""
        return _blockmatrix.BlockMatrix_NumColBlocks(self)

    def GetBlock(self, *args):
        r"""
        GetBlock(BlockMatrix self, int i, int j) -> SparseMatrix
        GetBlock(BlockMatrix self, int i, int j) -> SparseMatrix
        """
        return _blockmatrix.BlockMatrix_GetBlock(self, *args)

    def IsZeroBlock(self, i, j):
        r"""IsZeroBlock(BlockMatrix self, int i, int j) -> int"""
        return _blockmatrix.BlockMatrix_IsZeroBlock(self, i, j)

    def RowOffsets(self, *args):
        r"""
        RowOffsets(BlockMatrix self) -> intArray
        RowOffsets(BlockMatrix self) -> intArray
        """
        return _blockmatrix.BlockMatrix_RowOffsets(self, *args)

    def ColOffsets(self, *args):
        r"""
        ColOffsets(BlockMatrix self) -> intArray
        ColOffsets(BlockMatrix self) -> intArray
        """
        return _blockmatrix.BlockMatrix_ColOffsets(self, *args)

    def RowSize(self, i):
        r"""RowSize(BlockMatrix self, int const i) -> int"""
        return _blockmatrix.BlockMatrix_RowSize(self, i)

    def EliminateRowCol(self, *args):
        r"""
        EliminateRowCol(BlockMatrix self, int rc, mfem::Matrix::DiagonalPolicy dpolicy=DIAG_ONE)
        EliminateRowCol(BlockMatrix self, intArray ess_bc_dofs, Vector sol, Vector rhs)
        """
        return _blockmatrix.BlockMatrix_EliminateRowCol(self, *args)

    def Finalize(self, *args):
        r"""
        Finalize(BlockMatrix self, int skip_zeros=1)
        Finalize(BlockMatrix self, int skip_zeros, bool fix_empty_rows)
        """
        return _blockmatrix.BlockMatrix_Finalize(self, *args)

    def CreateMonolithic(self):
        r"""CreateMonolithic(BlockMatrix self) -> SparseMatrix"""
        return _blockmatrix.BlockMatrix_CreateMonolithic(self)

    def Elem(self, *args):
        r"""
        Elem(BlockMatrix self, int i, int j) -> double
        Elem(BlockMatrix self, int i, int j) -> double const &
        """
        return _blockmatrix.BlockMatrix_Elem(self, *args)

    def Inverse(self):
        r"""Inverse(BlockMatrix self) -> MatrixInverse"""
        return _blockmatrix.BlockMatrix_Inverse(self)

    def NumNonZeroElems(self):
        r"""NumNonZeroElems(BlockMatrix self) -> int"""
        return _blockmatrix.BlockMatrix_NumNonZeroElems(self)

    def GetRow(self, row, cols, srow):
        r"""GetRow(BlockMatrix self, int const row, intArray cols, Vector srow) -> int"""
        return _blockmatrix.BlockMatrix_GetRow(self, row, cols, srow)

    def EliminateZeroRows(self, threshold=1e-12):
        r"""EliminateZeroRows(BlockMatrix self, double const threshold=1e-12)"""
        return _blockmatrix.BlockMatrix_EliminateZeroRows(self, threshold)

    def Mult(self, x, y):
        r"""Mult(BlockMatrix self, Vector x, Vector y)"""
        return _blockmatrix.BlockMatrix_Mult(self, x, y)

    def AddMult(self, x, y, val=1.):
        r"""AddMult(BlockMatrix self, Vector x, Vector y, double const val=1.)"""
        return _blockmatrix.BlockMatrix_AddMult(self, x, y, val)

    def MultTranspose(self, x, y):
        r"""MultTranspose(BlockMatrix self, Vector x, Vector y)"""
        return _blockmatrix.BlockMatrix_MultTranspose(self, x, y)

    def AddMultTranspose(self, x, y, val=1.):
        r"""AddMultTranspose(BlockMatrix self, Vector x, Vector y, double const val=1.)"""
        return _blockmatrix.BlockMatrix_AddMultTranspose(self, x, y, val)
    __swig_destroy__ = _blockmatrix.delete_BlockMatrix
    owns_blocks = property(_blockmatrix.BlockMatrix_owns_blocks_get, _blockmatrix.BlockMatrix_owns_blocks_set, doc=r"""owns_blocks : int""")

    def PrintMatlab(self, *args):
        r"""
        PrintMatlab(BlockMatrix self, std::ostream & os=mfem::out)
        PrintMatlab(BlockMatrix self, char const * file, int precision=8)
        """
        return _blockmatrix.BlockMatrix_PrintMatlab(self, *args)

# Register BlockMatrix in _blockmatrix:
_blockmatrix.BlockMatrix_swigregister(BlockMatrix)



