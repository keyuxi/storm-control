#!/usr/bin/python
#
## @file
#
# Focus lock control specialized for Scope1.
#
# Hazen 03/12
# Alistair 08/16
#
import sc_library.parameters as params

# camera and stage.
import sc_hardware.madCityLabs.mclVoltageZController as MCLVZC
import sc_hardware.thorlabs.uc480Camera as uc480Cam

# focus lock control thread.
import focuslock.stageOffsetControl as stageOffsetControl

# ir laser control
import sc_hardware.thorlabs.LDC210 as LDC210

# focus lock dialog.
import focuslock.focusLockZ as focusLockZ

# # none widgets
# import focuslock.noneWidgets as noneWidgets

#
# Focus Lock Dialog Box specialized for Scope1 with 
# USB offset detector and Ludl Z piezo-Z stage 
#
class AFocusLockZ(focusLockZ.FocusLockZCam):
    def __init__(self, hardware, parameters, parent = None):
        # Scope1 specific focus lock parameters
        lock_params = parameters.addSubSection("focuslock")
        lock_params.add("qpd_zcenter", params.ParameterRangeFloat("Piezo center position in microns",
                                                                  "qpd_zcenter",
                                                                  150.0, 0.0, 300.0))  # range of z-piezo
        lock_params.add("qpd_scale", params.ParameterRangeFloat("Offset to nm calibration value",
                                                                "qpd_scale",
                                                                1.0, 0.1, 1000.0)) # 50, 0.1 to 1000
        lock_params.add("qpd_sum_min", 50.0)
        lock_params.add("qpd_sum_max", 256.0)
        lock_params.add("is_locked_buffer_length", 3)
        lock_params.add("is_locked_offset_thresh", 1)
        lock_params.add("ir_power", params.ParameterInt("", "ir_power", 6, is_mutable = False))
        
        offset_file = "cam_offsets_scope1.txt"
        cam = uc480Cam.CameraQPD(camera_id = 0, x_width = 680, y_width = 200,  # x_width = 540, y_width = 150   / 1280 x 1040
			sigma = 4.0, offset_file = offset_file)  # sigma = 4.0
        stage = MCLVZC.MCLVZControl("USB-6002", 0)
        # stage = noneWidgets.NanoP()  # use this to bypass the stage 
        lock_fn = lambda (x): -0.02 * x
        
        control_thread = stageOffsetControl.StageCamThread(cam,
                        stage,
                        lock_fn,
                        parameters.get("focuslock.qpd_sum_min", 50.0),
                        parameters.get("focuslock.qpd_zcenter"),#add a 0
                        parameters.get("focuslock.is_locked_buffer_length", 3),
                        parameters.get("focuslock.is_locked_offset_thresh", 1))
        
        ir_laser = LDC210.LDC210PWMNI("PCIe-6353", 1)  # Inputs here are (DAQ-card name, counter number). (was 0, switched to 1 and changed wiring 8/11/16)
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
