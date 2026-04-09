---
title: Manpage
---

# hdtv(1) -- Nuclear Spectrum Analysis Tool


## SYNOPSIS
$`hdtv [-h] [-b _batchfile_] [-e _commands_] [-v]`

## DESCRIPTION
HDTV tries to provide functionality similar to the old TV program on top
of the `ROOT` data analysis toolkit developed at CERN. The use of Python
gives HDTV much better scripting capabilities than TV. Also, since HDTV
consists of a number of modules that can in principle be used independently
of each other, HDTV is much easier to extend and customize. HDTV is written
in a mixture of C++ and Python, glued together using PyROOT.

## OPTIONS
`--help`, `-h`
: Show help message and exit

`--batch _batchfile_`, `-b _batchfile_`
: Open and execute hdtv batchfile

`--execute _commands_`, `-e _commands_`
: Execute hdtv command(s)

`--version`, `-v`
: Show HDTV Version

## HDTV COMMAND LINE
HDTV features an extensive command line interface. Besides a wide set of
HDTV commands, it is possible to use special prefixes:

`:`
: Execute a single Python command.

`@`
: Execute an HDTV batch file (or use the `exec` command).

`!`
: Execute a single shell command.

The command line is implemented using `prompt_toolkit`. Common features,
such as tab-completion, history and history-search (using ++ctrl+r++) are
available.

## KEY BINDINGS
Note: Key bindings are case sensitive.

### Window
++u++
: Update Viewport

++l++
: Toggle Log Scale

++shift+a++
: Toggle Y Auto Scale

++exclam++
: Toggle Use Norm


#### x directions
++space++
: Set X Zoom Marker

++x++
: Expand X

++arrow-right++, ++greater++
: Shift X Offset Right

++arrow-left++, ++less++
: Shift X Offset Left

++enter++
: Update

++pipe++
: Set X Center at Cursor

++1++
: X Zoom In Around Cursor

++0++
: X Zoom Out Around Cursor

#### y direction
++h++
: Set Y Zoom Marker

++y++
: Expand Y

++arrow-up++
: Shift Y Offset Up

++arrow-down++
: Shift Y Offset Down

++shift+z++
: Y Zoom In Around Cursor

++shift+x++
: Y Zoom Out Around Cursor


#### all directions
++e++
: Expand

++i++
: Enter Edit Mode: Go To Position


### Spec Interface
++page-up++, ++shift+n+p++
: Show Prev

++page-down++, ++shift+n+n++
: Show Next

++equal++
: Refresh All

++t++
: Refresh Visible

++n++
: Enter Edit Mode: Show spectrum

++a++
: Enter Edit Mode: Activate spectrum


### Fit Interface
++b++
: Set Marker bg

++minus+b++
: Remove Marker bg

++r++
: Set Marker region

++minus+r++
: Remove Marker region

++p++
: Set Marker peak

++minus+p++
: Remove Marker peak

++shift+b++
: Execute Fit (Background only)

++shift+f++
: Execute Fit

++shift+b++
: QuickFit

++minus+b++
: Clear Fit (Background only)

++minus+shift+f++
: Clear Fit

++plus+shift+f++
: Store Fit

++shift+d++
: Show Decomposition

++minus+shift+d++
: Hide Decomposition

++f+s++
: Enter Edit Mode: Show Fit

++f+a++
: Enter Edit Mode: Activate Fit

++f+p++
: Show Prev

++f+n++
: Show Next

++shift+i++
: Execute Integral


### Matrix Interface
++g++
: Set Marker cut

++c+g++
: Set Marker cutregion

++c+b++
: Set Marker cutbg

++minus+c+g++
: Remove Marker cutregion

++minus+c+b++
: Remove Marker cutbg

++minus+shift+c++
: Clear Cut

++plus+shift+c++
: Store Cut

++shift+c++
: Execute Cut

++c+s++
: Enter Edit Mode: Show Cut

++c+a++
: Enter Edit Mode: Activate Cut

++c+p++
: Show Prev

++c+n++
: Show Next

++tab++
: Switch

## FILES
=====

`$HOME/.config/hdtv/startup.py`
: Python script that gets executed during startup.

`$HOME/.config/hdtv/startup.hdtv, $HOME/.config/hdtv/startup.hdtv.d/\*.hdtv`
: Files containing HDTV commands that get executed during startup.

`$HOME/.config/hdtv/plugins/`
: Put plugins here.

`$HOME/.local/share/hdtv/hdtv_history`
: History of commands executed in HDTV.

HDTV supports the XDG Base Directory Specification, with the default paths
listed above. If the legacy directory `$HOME/.hdtv` exists, it is used
instead. It is also possible to manually set the directory using the
`$HDTV_USER_PATH` environment variable.

## BUGS
See <https://github.com/hdtv-tool/hdtv/issues> for a list of all
currently open bugs and feature requests.

## AUTHORS
Jan Mayer (jan.mayer@ikp.uni-koeln.de), <br>
Elena Hoemann (ehoemann@ikp.uni-koeln.de), <br>
Oliver Papst (opapst@ikp.tu-darmstadt.de), <br>
Nigel Warr (warr@ikp.uni-koeln.de), <br>
Norbert Braun (n.braun@ikp.uni-koeln.de), <br>
Tanja Kotthaus (t.kotthaus@ikp.uni-koeln.de), <br>
Ralf Schulze (r.schulze@ikp.uni-koeln.de) <br>
