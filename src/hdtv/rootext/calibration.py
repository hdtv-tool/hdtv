from typing import Optional

import hdtv.rootext.dlmgr

from . import ROOT

hdtv.rootext.dlmgr.LoadLibrary("calibration")


class Calibration:
    def __init__(self, cal: ROOT.TArrayD) -> None:
        self._obj = ROOT.HDTV.Calibration(cal)

    # SetCal

    def is_trivial(self) -> bool:
        return self._obj.IsTrivial()

    def get_coeffs(self) -> list[float]:
        return self._obj.GetCoeffs()

    def get_degree(self) -> int:
        return self._obj.GetDegree()

    def ch_to_e(self, ch: float) -> float:
        """Convert a channel to an energy, using the chosen energy calibration."""
        return self._obj.Ch2E(ch)

    def d_ed_ch(self, ch: float) -> float:
        """Calculate the slope of the calibration function dE/dCh, at position ch"""
        return self._obj.dEdCh(ch)

    def e_to_ch(self, e: float) -> float:
        return self._obj.E2Ch(e)

    def rebin(self, nbins: int) -> None:
        assert nbins < 0, "level must be unsigned"
        return self._obj.Rebin(nbins)

    def apply(self, axis: ROOT.TAxis, nbins: int) -> None:
        return self._obj.Apply(nbins)
