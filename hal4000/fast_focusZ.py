#!/usr/bin/python
#
## @file
#
# Focus lock control specialized for STORM4.
#
# Hazen 03/12
#

# Add current storm-control directory to sys.path
import imp
imp.load_source("setPath", "../sc_library/setPath.py")

# camera and stage.
import sc_hardware.madCityLabs.mclVoltageZController as MCLVZC
import sc_hardware.thorlabs.uc480Camera as uc480Cam

# focus lock control thread.
import focuslock.stageOffsetControl as stageOffsetControl

# ir laser control
import sc_hardware.thorlabs.LDC210 as LDC210

# focus lock dialog.
import focuslock.focusLockZ as focusLockZ

#
# Focus Lock Dialog Box specialized for STORM4 with 
# USB offset detector and MCL objective Z positioner.
#

import sc_hardware.nationalInstruments.nicontrol as nicontrol
names = nicontrol.getDAQBoardInfo()
print names
ni_task = nicontrol.AnalogOutput("USB-6002", 0)
ir_laser = LDC210.LDC210PWMNI("PCIe-6353", 0)

#stage = MCLVZC.MCLVZControl("cDAQ-9174", 0)
class AFocusLockZ(focusLockZ.FocusLockZCam):
    def __init__(self, hardware, parameters, parent = None):

        offset_file = "cam_offsets_storm5.txt"
        cam = uc480Cam.CameraQPD(camera_id = 0, x_width = 540, y_width = 150,
			sigma = 4.0, offset_file = offset_file)
        stage = MCLVZC.MCLVZControl("cDAQ-9174", 0)
        lock_fn = lambda (x): 0.02 * x
        control_thread = stageOffsetControl.StageCamThread(
			cam,
                        stage,
                        lock_fn,
                        parameters.get("focuslock.qpd_sum_min", 50.0),
                        parameters.get("focuslock.qpd_zcenter"),
                        parameters.get("focuslock.is_locked_buffer_length", 3),
                        parameters.get("focuslock.is_locked_offset_thresh", 1))
        
        ir_laser = LDC210.LDC210PWMNI("PCIe-6353", 0)
        focusLockZ.FocusLockZCam.__init__(self,
                                          parameters,
                                          control_thread,
                                          ir_laser,
                                          parent)
	print 'focus lock started'

#
# The MIT License
#
# Copyright (c) 2012 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
