## storm-control ##
This is a fork of the storm-control repository of code developed in the [Zhuang Lab](http://zhuang.harvard.edu) for the acquisition of STORM movies. We use this software for a variety of single-molecule imaging and fluorescent microscopy approaches, including STORM experiments. Most of the underlying code was written by Hazen Babcock, Harvard University. 

## Installation ##
You will need Python and PyQt as well as a number of other libraries. Please see the Install.txt file in the hal4000 folder.

## Directory Layout ##
dave - This folder contains software (dave.py) that is used to control hal for automated acquisition of multiple images and/or STORM movies. Dave controls Hal and Kilroy via TCP/IP.

fluidics - This folder contains software (kilroy.py) to control a series of pumps and valves so that fluid control can be integrated with imaging. 

hal4000 - This folder contains the hal-4000 microscope control and image acquisition software (hal-4000.py).

sc_hardware - This folder contains classes for interfacing with various bits of hardware. Folders are (usually) the manufacturers name.

sc_library - This folder contains the modules that are used in multiple different programs.

steve - This folder contains software (steve.py) that is used to take and assemble image mosaics. This is useful for array tomography experiments, among other things. Steve also controls Hal via TCP/IP.

zee-calibrator - This folder contains software (main.py) that is used to generate calibration curves for astigmatism based 3D STORM imaging. Calibration data acquired using Hal needs to be analyzed by STORM image analysis software like Insight3 (available by request from the Zhuang Lab) or 3D-DAOSTORM before it can be processed using zee-calibrator.

## General notes ##
1. This software is written primarily in Python with a few C helper libraries.

2. Doxygen documentation is available (for Dave, HAL and Steve), but you'll have to run doxygen to create it.

3. The software is provided "as is" in the hope that others might find it useful. While it is fairly stable and has been developed and used since 2009 in the Zhuang lab, we provide no guarantee that any future changes that are made will maintain backwards compatibility with older versions.

4. We can only provide fairly limited support. You will probably have the most success adapting this software for your purposes if you are reasonably familiar with the Python programming language.

5. This software can also control an NSTORM setup, with some limitations, the biggest of which is probably that shutter sequences don't work.

6. The Fluidics project has been moved from storm-control to a stand-alone [repository](https://github.com/BoettigerLab/fluidics-control).

7. Questions about this fork may be addressed to Alistair Boettiger, (boettiger _at_ stanford.edu). For the original repository, please see [github.com/ZhuangLab/storm-control](https://github.com/ZhuangLab/storm-control).  Note, this fork of the ZhuangLab storm-control is not maintained in backwards compatibility with the source.