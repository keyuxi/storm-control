#!/usr/bin/python
#
## @file
#
# This file contains hardware classes that interface 
# National Instruments cards with HAL illumination
# control software.
#
# Hazen 04/14
#

import hashlib
import time

# Debugging
import sc_library.hdebug as hdebug

import sc_hardware.baseClasses.illuminationHardware as illuminationHardware
import sc_hardware.nationalInstruments.nicontrol as nicontrol

## Nidaq
#
# National Instruments DAQ card (modulation).
#
class Nidaq(illuminationHardware.DaqModulation):

    ## __init__
    #
    # @param parameters A XML object containing initial parameters.
    # @param parent The PyQt parent of this object.
    #
    def __init__(self, parameters, parent):
        illuminationHardware.DaqModulation.__init__(self, parameters, parent)

        self.ao_task = False
        self.ct_task = False
        self.do_task = False

        if (hasattr(parameters, "counter_board")):
            self.counter_board = parameters.counter_board
            self.counter_id = parameters.counter_id
            self.counter_trigger = parameters.counter_trigger
        else:
            self.counter_board = False
            self.counter_id = False
            self.counter_trigger = False

        # FIXME:
        #   Need a waveform_clock_board parameter and we need to fix
        #   nicontrol to respect this, otherwise we can only use one
        #   board for waveform output.
        if (hasattr(parameters, "waveform_clock")):
            self.waveform_clock = parameters.waveform_clock
        else:
            self.waveform_clock = False
    
    ## analogOff
    #
    # Sets the analog voltage to the minimum.
    #
    # @param channel_id The channel id.
    #
    def analogOff(self, channel_id):
        if not self.filming:
            nicontrol.setAnalogLine(self.analog_settings[channel_id].board,
                                    self.analog_settings[channel_id].channel,
                                    self.analog_settings[channel_id].min_voltage)

    ## analogOn
    #
    # Sets the analog voltage to the maximum.
    #
    # @param channel_id The channel id.
    #
    def analogOn(self, channel_id):
        if not self.filming:
            nicontrol.setAnalogLine(self.analog_settings[channel_id].board,
                                    self.analog_settings[channel_id].channel,
                                    self.analog_settings[channel_id].max_voltage)

    ## digitalOff
    #
    # Sets the digital line to 0.
    #
    # @param channel_id The channel id.
    #
    def digitalOff(self, channel_id):
        if not self.filming:
            nicontrol.setDigitalLine(self.digital_settings[channel_id].board,
                                     self.digital_settings[channel_id].channel,
                                     False)

    ## digitalOn
    #
    # Sets the digital line to 1.
    #
    # @param channel_id The channel id.
    #
    def digitalOn(self, channel_id):
        if not self.filming:
            nicontrol.setDigitalLine(self.digital_settings[channel_id].board,
                                     self.digital_settings[channel_id].channel,
                                     True)

    ## shutterOff
    #
    # Sets the shutter digital line to 0.
    #
    # @param channel_id The channel id.
    #
    def shutterOff(self, channel_id):
        nicontrol.setDigitalLine(self.shutter_settings[channel_id].board,
                                 self.shutter_settings[channel_id].channel,
                                 False)

    ## digitalOn
    #
    # Sets the shutter digital line to 1.
    #
    # @param channel_id The channel id.
    #
    def shutterOn(self, channel_id):
        nicontrol.setDigitalLine(self.shutter_settings[channel_id].board,
                                 self.shutter_settings[channel_id].channel,
                                 True)

    ## startFilm
    #
    # Called at the start of filming (when shutters are active).
    #
    # @param seconds_per_frame How many seconds it takes to acquire each frame.
    # @param oversampling The number of values in the shutter waveform per frame.
    #
    def startFilm(self, seconds_per_frame, oversampling):
        illuminationHardware.DaqModulation.startFilm(self, seconds_per_frame, oversampling)
        print oversampling

        # Calculate frequency. This is set slightly higher than the camere
        # frequency so that we are ready at the start of the next frame.
        frequency = (1.01 / seconds_per_frame) * float(oversampling)

        # If oversampling is 1 then just trigger the ao_task 
        # and do_task directly off the camera fire pin.
        wv_clock = self.waveform_clock  # wv_clock = DAQ counter port (eg PFI12)
        if (oversampling == 1):
            wv_clock = "PFI" + str(self.counter_trigger)
            
        # Setup the counter.  (counter_board  = DAQ card)
        if self.counter_board and (oversampling > 1):
            
            def startCtTask():
                try:
                    self.ct_task = nicontrol.CounterOutput(self.counter_board, 
                                                           self.counter_id,
                                                           frequency, 
                                                           0.5)
                    self.ct_task.setCounter(oversampling)
                    self.ct_task.setTrigger(self.counter_trigger)
                    self.ct_task.startTask()
                except nicontrol.NIException:
                    return True

                return False

            iters = 0
            while (iters < 5) and startCtTask():
                hdebug.logText("startCtTask failed " + str(iters))
                self.ct_task.clearTask()
                time.sleep(0.5)
                iters += 1

            if iters == 5:
                hdebug.logText("startCtTask critical failure")
                raise nicontrol.NIException("NIException: startCtTask critical failure")

        else:
            self.ct_task = False

        # Setup analog waveforms.
        if (len(self.analog_data) > 0):

            # Sort by board, channel.
            analog_data = sorted(self.analog_data, key = lambda x: (x[0], x[1]))

            # Set waveforms.
            waveform = []
            for i in range(len(analog_data)):
                waveform += analog_data[i][2]

            def startAoTask():
                try:
                    # Create channels.
                    self.ao_task = nicontrol.AnalogWaveformOutput(analog_data[0][0], analog_data[0][1])
                    for i in range(len(analog_data) - 1):
                        self.ao_task.addChannel(analog_data[i+1][0], analog_data[i+1][1])
 
                    # Add waveform
                    self.ao_task.setWaveform(waveform, frequency, clock = wv_clock)

                    # Start task.
                    self.ao_task.startTask()
                except nicontrol.NIException:
                    return True
                    
                return False

            iters = 0
            while (iters < 5) and startAoTask():
                hdebug.logText("startAoTask failed " + str(iters))
                self.ao_task.clearTask()
                time.sleep(0.1)
                iters += 1

            if iters == 5:
                hdebug.logText("startAoTask critical failure")
                raise nicontrol.NIException("NIException: startAoTask critical failure")

        else:
            self.ao_task = False

        # Setup digital waveforms.
        if (len(self.digital_data) > 0):
            print 'starting digital waveform'
            # Sort by board, channel.
            digital_data = sorted(self.digital_data, key = lambda x: (x[0], x[1]))

            # Set waveforms.
            waveform = []
            for i in range(len(digital_data)):
                waveform += digital_data[i][2]

            def startDoTask():

                try:
                    # Create channels.
                    self.do_task = nicontrol.DigitalWaveformOutput(digital_data[0][0], digital_data[0][1])
                    for i in range(len(digital_data) - 1):
                        self.do_task.addChannel(digital_data[i+1][0], digital_data[i+1][1])

                    # Add waveform
                    self.do_task.setWaveform(waveform, frequency, clock = wv_clock)

                    # Start task.
                    self.do_task.startTask()
                except nicontrol.NIException:
                    return True

                return False

            iters = 0
            while (iters < 5) and startDoTask():
                hdebug.logText("startDoTask failed " + str(iters))
                self.do_task.clearTask()
                time.sleep(0.1)
                iters += 1

            if iters == 5:
                hdebug.logText("startDoTask critical failure")
                raise nicontrol.NIException("NIException: startDoTask critical failure")

        else:
            self.do_task = False

        # Start tasks
#        for task in [self.ao_task, self.do_task]:
#            #for task in [self.ct_task, self.ao_task, self.do_task]:
#            if task:
#                task.startTask()

    ## stopFilm
    #
    # Called at the end of filming (when shutters are active).
    #
    def stopFilm(self):
        illuminationHardware.DaqModulation.stopFilm(self)
        for task in [self.ct_task, self.ao_task, self.do_task]:
            if task:
                try:
                    task.stopTask()
                    task.clearTask()
                except nicontrol.NIException as e:
                    hdebug.logText("stop / clear failed for task " + str(task) + " with " + str(e))


## NidaqAmp
#
# National Instruments DAQ card analog amplitude modulation.
#
class NidaqAmp(illuminationHardware.AmplitudeModulation):

    ## __init__
    #
    # @param parameters A XML object containing initial parameters.
    # @param parent The PyQt parent of this object.
    #
    def __init__(self, parameters, parent):
        illuminationHardware.AmplitudeModulation.__init__(self, parameters, parent)

    ## amplitudeOff
    #
    # Called when the module should turn off a channel.
    #
    # @param channel_id The channel id.
    #
    def amplitudeOff(self, channel_id):
        nicontrol.setAnalogLine(self.channel_parameters[channel_id].board,
                                self.channel_parameters[channel_id].channel,
                                self.channel_parameters[channel_id].min_voltage)

    ## amplitudeOn
    #
    # Called when the module should turn on a channel.
    #
    # @param channel_id The channel id.
    # @param amplitude The channel amplitude.
    #
    def amplitudeOn(self, channel_id, amplitude):
        nicontrol.setAnalogLine(self.channel_parameters[channel_id].board,
                                self.channel_parameters[channel_id].channel,
                                0.001 * amplitude)

    ## getMaxAmplitude
    #
    # @param channel_id The channel id.
    #
    # @return The maximum amplitude for this channel.
    #
    def getMaxAmplitude(self, channel_id):
        return self.channel_parameters[channel_id].maximum

    ## getMinAmplitude
    #
    # @param channel_id The channel id.
    #
    # @return The minimum amplitude for this channel.
    #
    def getMinAmplitude(self, channel_id):
        params = self.channel_parameters[channel_id]
        if (hasattr(params, "minimum")):
            return params.minimum
        else:
            return 0

    ## initialize
    #
    # This is called by each of the channels that wants to use this module.
    #
    # @param interface Interface type (from the perspective of the channel).
    # @param channel_id The channel id.
    # @param parameters A parameters object for this channel.
    #
    def initialize(self, interface, channel_id, parameters):
        self.channel_parameters[channel_id] = parameters
        self.channel_parameters[channel_id].maximum = int(1000.0 * parameters.max_voltage)
        self.channel_parameters[channel_id].minimum = int(1000.0 * parameters.min_voltage)

    ## setAmplitude
    #
    # @param channel_id The channel id.
    # @param amplitude The channel amplitude.
    #
    def setAmplitude(self, channel_id, amplitude):
        self.amplitudeOn(channel_id, amplitude)

## NidaqTR
#
# National Instruments DAQ card (modulation) with task recycling.
# Waveforms are considered different if they have different md5
# hashs. Hopefully hash collisions will be very rare..
#
class NidaqTR(Nidaq):

    ## __init__
    #
    # @param parameters A XML object containing initial parameters.
    # @param parent The PyQt parent of this object.
    #
    def __init__(self, parameters, parent):
        Nidaq.__init__(self, parameters, parent)

        self.ao_tasks = {}
        self.ct_tasks = {}
        self.do_tasks = {}

    ## startFilm
    #
    # Called at the start of filming (when shutters are active).
    #
    # @param seconds_per_frame How many seconds it takes to acquire each frame.
    # @param oversampling The number of values in the shutter waveform per frame.
    #
    def startFilm(self, seconds_per_frame, oversampling):
        illuminationHardware.DaqModulation.startFilm(self, seconds_per_frame, oversampling)

        # Calculate frequency. This is set slightly higher than the camere
        # frequency so that we are ready at the start of the next frame.
        frequency = (1.01 / seconds_per_frame) * float(oversampling)

        # Setup analog waveforms.
        print "analog"
        if (len(self.analog_data) > 0):

            # Sort by board, channel.
            analog_data = sorted(self.analog_data, key = lambda x: (x[0], x[1]))

            # Set waveforms.
            waveform = []
            for i in range(len(analog_data)):
                waveform += analog_data[i][2]

            # Check if we already have a task for this waveform.
            waveform_hash = hashlib.md5("".join(str(elt) for elt in waveform)).hexdigest()
            if waveform_hash in self.ao_tasks:
                self.ao_task = self.ao_tasks[waveform_hash]
                self.ao_task.reserveTask()
                print "using recycled ao_task", waveform_hash

            else:
                def initAoTask():

                    # Create channels.
                    self.ao_task = nicontrol.AnalogWaveformOutput(analog_data[0][0], analog_data[0][1])
                    for i in range(len(analog_data) - 1):
                        self.ao_task.addChannel(analog_data[i+1][0], analog_data[i+1][1])

                    # Add waveform
                    return self.ao_task.setWaveform(waveform, frequency, clock = self.waveform_clock)

                iters = 0
                valid = initAoTask()
                while (iters < 5) and (not valid):
                    hdebug.logText("initAoTask failed " + str(iters))
                    self.ao_task.clearTask()
                    time.sleep(0.1)
                    valid = initAoTask()                    
                    iters += 1

                if valid:
                    self.ao_tasks[waveform_hash] = self.ao_task

        else:
            self.ao_task = False

        # Setup digital waveforms
        print "digital"
        if (len(self.digital_data) > 0):

            # Sort by board, channel.
            digital_data = sorted(self.digital_data, key = lambda x: (x[0], x[1]))

            # Set waveforms.
            waveform = []
            for i in range(len(digital_data)):
                waveform += digital_data[i][2]

            # Check if we already have a task for this waveform.
            waveform_hash = hashlib.md5("".join(str(elt) for elt in waveform)).hexdigest()
            if waveform_hash in self.do_tasks:
                self.do_task = self.do_tasks[waveform_hash]
                self.do_task.reserveTask()
                print "using recycled do_task", waveform_hash

            else:
                def initDoTask():

                    # Create channels.
                    self.do_task = nicontrol.DigitalWaveformOutput(digital_data[0][0], digital_data[0][1])
                    for i in range(len(digital_data) - 1):
                        self.do_task.addChannel(digital_data[i+1][0], digital_data[i+1][1])

                    # Add waveform
                    return self.do_task.setWaveform(waveform, frequency, clock = self.waveform_clock)

                iters = 0
                valid = initDoTask()
                while (iters < 5) and (not valid):
                    hdebug.logText("initDoTask failed " + str(iters))
                    self.do_task.clearTask()
                    time.sleep(0.1)
                    valid = initDoTask()
                    iters += 1

                if valid:
                    self.do_tasks[waveform_hash] = self.do_task

        else:
            self.do_task = False

        # Setup the counter.
        print "counter"
        if self.counter_board:

            ct_hash = str(frequency) + str(oversampling)
            if ct_hash in self.ct_tasks:
                self.ct_task = self.ct_tasks[ct_hash]
                self.ct_task.reserveTask()
                print "using recycled ct_task", ct_hash

            else:
                def initCtTask():
                    self.ct_task = nicontrol.CounterOutput(self.counter_board, 
                                                           self.counter_id,
                                                           frequency, 
                                                           0.5)
                    self.ct_task.setCounter(oversampling)
                    self.ct_task.setTrigger(self.counter_trigger)
                    print self.ct_task.verifyTask()
                    return self.ct_task

                iters = 0
                valid = initCtTask()
                while (iters < 5) and (not valid):
                    hdebug.logText("initCtTask failed " + str(iters))
                    self.ct_task.clearTask()
                    time.sleep(0.1)
                    valid = initCtTask()
                    iters += 1

                if valid:
                    self.ct_tasks[ct_hash] = self.ct_task

        else:
            self.ct_task = False

        # Start tasks
        for task in [self.ct_task, self.ao_task, self.do_task]:
            if task:
                task.startTask()

    ## stopFilm
    #
    # Called at the end of filming (when shutters are active).
    #
    def stopFilm(self):
        illuminationHardware.DaqModulation.stopFilm(self)
        for task in [self.ct_task, self.ao_task, self.do_task]:
            if task:
                task.stopTask()
                task.unreserveTask()


#
# The MIT License
#
# Copyright (c) 2014 Zhuang Lab, Harvard University
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
