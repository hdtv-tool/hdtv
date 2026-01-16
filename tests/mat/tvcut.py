import os
import random
import time

# Cut using TV


class Cut:
    def __init__(self):
        self.fBgRegions = []

    def Cut(self, matfile, r1, r2):
        tempdir = "/home/braun/Diplom/temp"
        fname = f"{random.randint(0, 2 ** 128):032X}.asc"

        tvcmds = "cut activate 0; "
        tvcmds += "cut attach matrix 1; "
        tvcmds += "cut attach dir 2; "

        tvcmds += f"cut dir open 2 {tempdir}; "
        tvcmds += f"cut matrix open 1 {matfile}; "

        # Sub-channel resolution is really useless here,
        # because TV cuts only with channel resolution anyway

        tvcmds += f"cut marker cut enter {r1:.1f}; "
        tvcmds += f"cut marker cut enter {r2:.1f}; "

        for bg in self.fBgRegions:
            tvcmds += f"cut marker bg-gate enter {bg:.1f};"

        tvcmds += "cut create cut; "

        tvcmds += f"spec write {tempdir + '/' + fname}'txt active; "

        tvcmds += "exit; "

        os.spawnl(
            os.P_WAIT,
            "/usr/bin/xvfb-run",
            "/usr/bin/xvfb-run",
            "-w",
            "0",
            "/ikp/bin/tv",
            "-src",
            "-rc",
            "-e",
            tvcmds,
        )

        time.sleep(0.5)

        return tempdir + "/" + fname
