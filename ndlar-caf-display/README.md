# DUNE ndlar-caf-display

This package provides an interactive 2D/3D event display for interactions within the **DUNE Near Detector Liquid Argon (ND-LAr)** using Common Analysis Format (CAF) flat trees as input. It draws straight lines between the start and end positions of particle hypotheses, color-coded by particle type and overlaid with truth-level information for validation.

The package can be installed with pip:
```
pip install ndlar-caf-display
```

The primary way to generate an event display is with the `ndlar-caf-display` command which is a CLI that is included in the pip installation. Alternatively, you can import the `ndlar_caf_display.helpers` module in Python. 

## The `ndlar-caf-display` command

The basic usage of this command is:
```
ndlar-caf-display /path/to/CAF.flat.root
```
which brings up an interactive window for the event display, and saves a png of the event display to the default `--save-dir` which is `plots/`. The full usage can be seen with `ndlar-caf-display --help`:
```
[chknight@dunegpvm02 test]$ ndlar-caf-display --help
usage: ndlar-caf-display [-h] [--spill SPILL] [--ixn IXN [IXN ...]] [--reco {dlp,pandora}] [--save-dir SAVE_DIR]
                         [--skip-truth] [--apply-fv-cut] [--batch]
                         caf_file

Display interactions from a CAF file.

positional arguments:
  caf_file              Path to the CAF file to display.

optional arguments:
  -h, --help            show this help message and exit
  --spill SPILL         Spill number to display (default: 0th spill).
  --ixn IXN [IXN ...]   Interaction number(s) within the spill to display (default: 0th interaction).
  --reco {dlp,pandora}  Reconstruction type to display: 'dlp' (spine) or 'pandora' (default: 'dlp').
  --save-dir SAVE_DIR   Directory to save plots (default: 'plots').
  --skip-truth          Whether to skip plotting truth information (default: False).
  --apply-fv-cut        Whether to apply the fiducial volume cut (default: False).
  --batch, -b           Whether to run in batch mode where the plots are not displayed interactively (default:
                        False).
```

If you are running `ndlar-caf-display` on a machine with `/pnfs/dune/persistent` available, e.g. the DUNE gpvm's, you can get started quickly with:
```
ndlar-caf-display -b /pnfs/dune/persistent/physicsgroups/dunendsim/abooth/nd-production/MicroProdN4p1/run-cafmaker/MicroProdN4p1_NDComplex_FHC.caf.full.spineonly/CAF.flat/0002000/0002400/MicroProdN4p1_NDComplex_FHC.caf.full.spineonly.0002459.CAF.flat.root
```

## Usage via `ndlar_caf_display.helpers`

You may want to interact directly with functions written in the `ndlar_caf_display.helpers` module, for example if you wanted to write script that produced a bunch of event display for later viewing. 

You can see examples of this in the `ndlar-caf-display` CLI source [code](https://github.com/DUNE/dune-nd-ana/blob/develop/ndlar-caf-display/src/ndlar_caf_display/cli.py), and in this [notebook](https://github.com/DUNE/dune-nd-ana/blob/develop/ndlar-caf-display/ndlar_caf_display-copyMe.ipynb).