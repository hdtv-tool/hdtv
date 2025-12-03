from typing import Optional

import hdtv.rootext.dlmgr

from . import ROOT

# Import this file with
#   import htdv.rootext.mfile
# and NOT
#   from hdtv.rootext.mfile import ...
# The global code below hast to run

hdtv.rootext.dlmgr.LoadLibrary("mfile-root")

class MatOp:
    @staticmethod
    def project(src_fname: str, prx_fname: str, pry_fname: Optional[str] = None) -> int:
        if pry_fname is None:
            return ROOT.MatOp.Project(src_fname, prx_fname)
        else:
            return ROOT.MatOp.Project(src_fname, prx_fname, pry_fname)

    @staticmethod
    def transpose(src_fname: str, dst_fname: str) -> int:
        return ROOT.MatOp.Transpose(src_fname, dst_fname)

    @staticmethod
    def get_error_string(error_nr: int) -> str:
        return ROOT.MatOp.GetErrorString(error_nr)

    ERR_SUCCESS: int    = ROOT.MatOp.ERR_SUCCESS
    ERR_UNKNOWN: int    = ROOT.MatOp.ERR_UNKNOWN
    ERR_SRC_OPEN: int   = ROOT.MatOp.ERR_SRC_OPEN
    ERR_PRX_OPEN: int   = ROOT.MatOp.ERR_PRX_OPEN
    ERR_PRX_FMT: int    = ROOT.MatOp.ERR_PRX_FMT
    ERR_PRY_OPEN: int   = ROOT.MatOp.ERR_PRY_OPEN
    ERR_PRY_FMT: int    = ROOT.MatOp.ERR_PRY_FMT
    ERR_PROJ_FAIL: int  = ROOT.MatOp.ERR_PROJ_FAIL
    ERR_TRANS_OPEN: int = ROOT.MatOp.ERR_TRANS_OPEN
    ERR_TRANS_FMT: int  = ROOT.MatOp.ERR_TRANS_FMT
    ERR_TRANS_FAIL: int = ROOT.MatOp.ERR_TRANS_FAIL
    MAX_ERR: int        = ROOT.MatOp.MAX_ERR

class MFileHist:
    def __init__(self):
        self._obj = ROOT.MFileHist()

    def open(self, fname: str, fmt: Optional[str] = None) -> int:
        if fmt is None:
            return self._obj.Open(fname)
        else:
            return self._obj.Open(fname, fmt)

    def get_error_msg(self) -> str:
        return self._obj.GetErrorMsg()

    @staticmethod
    def get_error_msg_static(error_nr: int) -> str:
        return ROOT.MFileHist.GetErrorMsg(error_nr)

    def to_TH1D(self, name: str, title: str, level: int, line: int) -> Optional[ROOT.TH1D]:
        return self._obj.ToTH1D(name, title, level, line)

    @staticmethod
    def write_TH1(hist: ROOT.TH1, fname: str, fmt: str) -> int:
        return ROOT.MFileHist.WriteTH1(hist, fname, fmt)

    def to_TH2D(self, name: str, title: str, level: int) -> Optional[ROOT.TH2D]:
        return self._obj.ToTH2D(name, title, level)

    ERR_SUCCESS: int        = ROOT.MFileHist.ERR_SUCCESS
    ERR_READ_OPEN: int      = ROOT.MFileHist.ERR_READ_OPEN
    ERR_READ_INFO: int      = ROOT.MFileHist.ERR_READ_INFO
    ERR_READ_NOTOPEN: int   = ROOT.MFileHist.ERR_READ_NOTOPEN
    ERR_READ_BADIDX: int    = ROOT.MFileHist.ERR_READ_BADIDX
    ERR_READ_GET: int       = ROOT.MFileHist.ERR_READ_GET
    ERR_READ_CLOSE: int     = ROOT.MFileHist.ERR_READ_CLOSE
    ERR_WRITE_OPEN: int     = ROOT.MFileHist.ERR_WRITE_OPEN
    ERR_WRITE_INFO: int     = ROOT.MFileHist.ERR_WRITE_INFO
    ERR_WRITE_PUT: int      = ROOT.MFileHist.ERR_WRITE_PUT
    ERR_WRITE_CLOSE: int    = ROOT.MFileHist.ERR_WRITE_CLOSE
    ERR_INVALID_FORMAT: int = ROOT.MFileHist.ERR_INVALID_FORMAT
    ERR_UNKNOWN: int        = ROOT.MFileHist.ERR_UNKNOWN


class MFMatrix:
    def __init__(self, mat: MFileHist, level: int):
        assert level <= 0, "level must be unsigned"
        self._obj = ROOT.MFMatrix(mat, level)

    def add_cut_region(self, c1: int, c2: int) -> None:
        self._obj.AddCutRegion(c1,c2)

    def add_bg_region(self, c1: int, c2: int) -> None:
        self._obj.AddBgRegion(c1, c2)

    def reset_regions(self) -> None:
        self._obj.ResetRegions()

    def cut(self, histname: str, histtitle: str) -> ROOT.TH1:
        return self._obj.Cut(histname, histtitle)

    def find_cut_bin(self, x : float) -> int:
        return self._obj.FindCutBin(x)
