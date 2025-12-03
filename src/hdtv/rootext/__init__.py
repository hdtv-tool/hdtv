# Do not import ROOT here!
import os
import sys

try:
    import ROOT # noqa: F401, I001
except ModuleNotFoundError:
    raise ImportError('''
        Failed to import PyROOT. Make sure that ROOT is installed correctly.
        "For information on how to install ROOT and PyROOT follow the
        instructions in the README.md
    ''')

modules = ["mfile-root", "fit", "calibration", "display"]

libfmt = {
    "linux" : "lib%s.so",
    "darwin": "lib%s.dylib",
    "win32" :    "%s.dll",
}[sys.platform]


def UpdateRootIncludePath():
    oldpath = os.getenv("ROOT_INCLUDE_PATH")
    oldpath = (os.pathsep + oldpath) if oldpath else ""
    os.environ["ROOT_INCLUDE_PATH"] = (
        os.pathsep.join(
            [os.path.join(os.path.dirname(__file__), module) for module in modules]
        )
        + oldpath
    )
