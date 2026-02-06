# HDTV - A ROOT-based spectrum analysis software
#  Copyright (C) 2006-2019  The HDTV development team (see file AUTHORS)
#
# This file is part of HDTV.
#
# HDTV is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# HDTV is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with HDTV; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

"""
Test whether the rootext Matop Transpose operation performs as intended.

At time of writing, there is no interface to generate mfiles with Python.
The test files were generated using create_mtx.c.
Note that the checked-in test files are deliberately small and may not
cover all edge cases of the transpose implementation. Generate larger
files to trigger these cases.

"""
import hashlib
import os
import tempfile

import pytest
import ROOT


@pytest.fixture
def load_rootext(lib="mfile-root"):
    import hdtv.rootext.dlmgr
    hdtv.rootext.dlmgr.LoadLibrary(lib)

@pytest.mark.parametrize(
    "mtx, tmtx",[
        ("simple.mtx", "simple.tmtx"),
        ("simple.tmtx", "simple.mtx"),
        ("complex.mtx", "complex.tmtx"),
        ("complex.tmtx", "complex.mtx"),
    ]
)
def test_matop_transpose(mtx : str, tmtx : str):
    mtx = os.path.join(os.path.dirname(__file__), mtx)
    tmtx = os.path.join(os.path.dirname(__file__), tmtx)

    tmtx_hash = hashlib.md5()
    with open(tmtx, "rb") as _tmtx:
        for block in iter(lambda: _tmtx.read(65536), b''):
            tmtx_hash.update(block)

    calc_hash = hashlib.md5()
    with tempfile.NamedTemporaryFile(mode= "r+b", delete=True) as _tmtx:
        result = ROOT.MatOp.Transpose(mtx, _tmtx.name)
        assert result == 0, \
            f"MatOp.Transpose failed with error code {result}: {ROOT.MatOp.GetErrorString(result)}"
        for block in iter(lambda: _tmtx.read(65536), b''):
            calc_hash.update(block)

    assert calc_hash.digest() == tmtx_hash.digest(), \
        f"Hash mismatch: expected {tmtx_hash.hexdigest()}, got {calc_hash.hexdigest()}"
