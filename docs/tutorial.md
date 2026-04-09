---
title: Turorial
---

# A tutorial introduction to HDTV

This tutorial explains how to open spectra in HDTV, fit peaks and apply energy
calibrations. It gives an overview over the basic features and a typical
workflow for using HDTV.

## Starting hdtv

Start HDTV using the `hdtv` command:
```sh
$ hdtv
HDTV – Nuclear Spectrum Analysis Tool
hdtv>
```

A new GUI window is opened. This window is used to view spectra and fit peaks.
Except for the two axes, it is empty at the moment, as there is no spectrum
to view yet.

Additionally, your terminal window now features the `hdtv>` prompt, which is
ready to accept your commands. To get an overview over the available commands,
press the ++tab++ key. If you want to leave HDTV, you can do so using `exit`
or `quit`. To get more information about a command, enter the name of the
command followed by `--help`.

## Load a Spectrum

To read and write spectra, HDTV resorts to the libmfile library. It supports
multiple file formats for spectra and matrices, including line compressed
(lc) files and line-separated ASCII (txt) spectra.

Use `cd`, `ls`, and `pwd` to navigate your file system and find the
spectrum you want to load.

The `spectrum *` commands are used to work with spectra. Load a new
spectrum using

```
hdtv> spectrum get <filename>
```

It is possible to abbreviate commands to safe time and type less. The
following commands are all equivalent:

```
hdtv> spectrum get <filename>
hdtv> spe g <filename>
hdtv> s g <filename>
hdtv> spectrum <filename>
hdtv> s <filename>
```

The last two commands are special, as the `spectrum *` command group
will default to its `get` subcommand, if no subcommand is present.
Please note that it is not always possible to abbreviate to a single
letter unambiguously.

The `filename` argument can consist of one or multiple filenames.
Globbing is possible, so patterns such as `*`, `?` or `[0-9]`
can be used for filename completion.

After you press ++Enter++, the spectrum appears in the GUI spectra window.
Several interaction possibilities with this window exist:

++left-button++, ++less++, ++greater++, ++left++, ++right++
: Move left and right in the spectrum.

++shift+left-button++
: Move in all directions in the spectrum.

++ctrl+shift+left-button++
: Move around faster.

Scroll Wheel, ++0++, ++1++
: Zoom in and out.

++l++
: Toggle between linear and log y-scale.

++up++, ++down++
: Move up and down in the spectrum.

++pipe++, ++pipe++, ++x++
: Mark a horizontal range (using `|` and `|`) and zoom to it (`x`).

++h++, ++h++, ++y++
: Mark a vertical range (using `h` and `h`) and zoom to it (`y`).

++shift+z++, ++shift+x++
: Zoom in and out vertically.

++shift+a++
: Toggle Y Auto Scale.

++i++
: Press `i` and input a number to center at a certain position.

For a complete list, see `hdtv`(1)

## Fit Peaks
The GUI window is also used for fitting. To create a fit, several markers
have to be set for fit region, background region and the peaks.

Mark the left and right border of the fit region using the ++r++ key for
each side. Two blue lines will appear. All peaks you want to fit have to
lie within the region between these two lines. Only one fit region can
exist, pressing ++r++ again will delete the old fit region and create a
new one.

Mark regions of the spectrum that contain only background and no peaks
using the ++b++ key for each side. Two yellow lines will appear. They do
not have to lie within the fit region. You can create multiple background
regions.

Finally, mark all the peaks using the ++p++ key. One purple line will appear
for each marked peak.

You can delete marked regions and peaks by pressing ++minus++ followed by
++r++ or ++b++, respectively ++p++. This will delete the corresponding
fit region/background region/peak marker closest to the cursor.

To finally execute the fit, press ++shift+f++. This might cause the peak markers
to move to the fitted position. To only fit the background, press ++shift+b++.
In the spectra window, plots will appear for the fitted background and
peaks. You can display a decomposition of the individual peaks using ++shift+d++.
To delete the fits or hide the decomposition, use ++minus+shift+f++, ++minus+shift+b++ or ++minus+shift+d++.

When creating a fit, a table with information about the fit and individual
peaks will appear in the terminal window, giving you information about
position, width, volume and more.

By default, a linear fit is being used for the background. This might not
be sufficient for your needs, so you may want to switch to a polynomial
with a different degree. To switch to a cubic polynomial, use

```
hdtv> fit parameter background 3
```
When you are satisfied with the fit, you might want to store it for further usage:
```
hdtv> fit store
```

A number will appear at the top of the GUI window above each peak, denoting
the corresponding fitID. Each peak can be identified using a pair of two
numbers separated by a dot. For example, `0.0` corresponds to peak `0`
(the leftmost peak) in fit `0`.

It is now possible, to safely delete the so-called workFit using ++minus+shift+f++.
The peak marker and the graphs of the fitted peaks and the background will
remain in the color of the corresponding spectrum.

To activate and possibly modify the fit again, execute
```
hdtv> fit activate <fitID>
```

The colored region markers and fit graphs will reappear. The original fit
will stay visible with dashed lines until you store the fit again.

You can export fits to XML-files using
```
hdtv> fit write <filename>
```
HDTV includes several peak and background models. The default model is the
so-called `theuerkauf` peak model, which is identical to the classical tv
peak model. An alternate model is the `ee` peak model, which is used to
describe the shape of lines in electron-scattering spectra. To explicitly
activate a peak model, use

```
hdtv> fit function peak activate <peakmodel>
```

Likewise, several background models are available: `polynomial` (default),
`exponential` and `interpolation`. They can be activated using

```
hdtv> fit function background activate <backgroundmodel>
```

The order of the polynomial and exponential background and the order of the
interpolation spline of the interpolation background model can be adjusted
using

```
hdtv> fit parameter background <order>
```

The interpolation model works in a different way in comparison to the
polynomial and exponential model: Instead of fitting a model
to the selected background region, a spline is created. It does not
consider every bin of the selected background region. Instead, for each
background region, only the mean value of all bins is considered.

It is possible to choose between `normal` (default) and `poisson` statistics:
```
hdtv> fit parameter likelihood <statistics>
```

Also, the user can choose to integrate the model for each bin, instead
of evaluating it at the bin center:
```
hdtv> fit parameter integrate true  
```

## Energy Calibration
One of the most important tasks is to conduct an energy calibration. It is
very easy to do so using HDTV by assigning the known energy literature value
to fitted peaks in calibration spectra. To assign energies to fitted peaks
in a stored spectrum, use `fit assign`, e.g.:
```
hdtv> calibration position assign 0.1 1173.228(3) 0.3 1332.492(4)
```

This will assign energies to peaks `0.1` and `0.3` and conduct an energy
calibration afterwards. It is also possible to do this in two steps:
```
hdtv> fit position assign 0.1 1173.228(3) 0.3 1332.492(4)
hdtv> calibration position recalibrate
```

As you might have noticed, HDTV is capable of dealing with uncertainties
and will respect them in the calibration. This is especially useful when
using a larger number of peaks for the calibration. After calibrating
the spectrum, the x-axis in the GUI will show the calibrated energies.

Alternatively, it is also possible to manually enter channel-energy pairs:
```
hdtv> calibration position enter 1543 1173.228(3) 1747 1332.492(4)
```

You can also use an external program to determine a fit polynomial and
enter the coefficients manually:
```
hdtv> calibration position set -30.88423486072141 0.780361132236243
```

This corresponds to the fit function
```
Energy(c) = -30.88423486072141 + 0.780361132236243 c
```

Higher order coefficients can be added at the end of the command.

You can permanently store the calibrations in calibration files. The file
format has changed in comparison to the old TV program. While
spectrum-specific calibration files that only contain a single calibration
are still supported using `calibration position read <filename>` and
`calibration position write <filename>`, it is recommended to use
calibration lists instead. A single calibration list file can contain
the calibration for multiple spectra. The file format corresponds to the
output of `calibration position list`:
```
hdtv> calibration position list
osiris_bg.spc: -30.88423486072141   0.780361132236243
```

To load a calibration list file, use
```
hdtv> calibration position list read <filename>
```

To write all existing calibrations into a calibration list file, use
```
hdtv> calibration position list write <filename>
```

Alternatively, the calibration can be done with some known calibration
sources automatically:
```
hdtv> calibration position nuclide Eu-152 -d IAEA -a
```

To calibrate the efficiency also the built-in calibration sources can be used.
```
hdtv> calibration efficiency fit -d IAEA 0,152Eu
```

## Normalize Spectra
Spectra can be normalized with a coefficient with
```
hdtv> spectrum normalize <specID> <coefficient>
```
Afterwards, go to the spectrum and press ++shift+1++ to apply the normalization.
Press the key combination again to unapply it.

## Working with multiple Spectra
From the command line, it is possible to show individual spectra using
```
hdtv> spectrum show <specID>
```
and
```
hdtv> spectrum hide <specID>
```

`spaecID` might be an id of one or multiple spectra.
Possible values include `0`, `2,4`, `1-5`, `all`, `active`, `none`, `next`, `prev`,
`first`, `last`, and `visible`.

The currently active spectrum (that is used for fitting) is set using
```
hdtv> spectrum activate <specID>
```

It is also possible to show and hide spectra from the GUI spectra window:

++n++ + `<specID>`
: ++n++ followed by the IDs of the spectra to show. Confirm with ++enter++.

++a++ + `<specID>`
: ++a++ followed by the ID of the spectrum to activate. Confirm with ++enter++.

The currently visible spectra and their corresponding colors are shown in
the top left corner of the GUI spectra window.

Spectra can be also deleted, or copied:
```
hdtv> spectrum copy <specID>
hdtv> spectrum delete <specID>
```

Add several spectra by first specifying the specID of the resulting summed spectrum:
```
hdtv> spectrum add <specID_sum> <specID1> <specID2> ...
```

## Open ROOT Files

To open a ROOT histogram:
```
hdtv> root get path/to/rootfile.root/histogram
```

To open an asymmetric ROOT matrix:
```
hdtv> root matrix get asym path/to/rootfile.root/matrix
```

For symmetric matrices use `sym` instead of `asym`.
Opening a matrix gives two spectra 0.0 and 0.1 which are the X and Y projections.

## Peak Search
Find peaks automatically between start and end bin:
```
hdtv> fit peakfind startbin endbin  [-a] [-r] [-s] [-t]
```
The option `-a` automatically fits the found peaks. `-r` rejects peaks. 
With `-s` sigma and with `-t` the threshold for the search can be specified.
