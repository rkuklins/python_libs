from EventHandler import EventHandler
import threading
import struct

# Purpose: A class for handling PS4 controller events.
class PS4Controller(EventHandler, threading.Thread):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "PS4 controller"; 
    
    # This is the main loop of handling PS4 controller events. It is run in a separate thread.
    def run(self):
       # Open the Gamepad event file:
        # /dev/input/event3 is for PS3 gamepad
        # /dev/input/event4 is for PS4 gamepad
        # look at contents of /proc/bus/input/devices if either one of them doesn't work.
        # use 'cat /proc/bus/input/devices' and look for the event file.
        infile_path = "/dev/input/event4"

        # open file in binary mode
        in_file = open(infile_path, "rb")

        # Read from the file
        # long int, long int, unsigned short, unsigned short, unsigned int
        FORMAT = 'llHHI'    
        EVENT_SIZE = struct.calcsize(FORMAT)
        event = in_file.read(EVENT_SIZE)
        #ev3 = EV3Brick()

        while event:

            (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)
            """
            # Handle PS4 controller left joystick
            if ev_type == 3 and code == 1:
                left = self.scale(value, (0,255), (-100,100))
                #if(left > 2 and left < -2):
                print("Left X1: " + str(left))
                #forward = scale(value, (0,255), (-100,100))
            if ev_type == 3 and code == 0:
                left = self.scale(value, (0,255), (-100,100))
                if(left > 2 and left < -2):
                    print("Left Y1: " + str(left))


            #  Handle PS4 controller right joystick
            if ev_type == 3 and code == 0:
                right = self.scale(value, (0,255), (-100,100))
                if(right > 2 and right < -2):
                    print("Right X1: " + str(left))
            if ev_type == 3 and code == 0:
                right = self.scale(value, (0,255), (-100,100))

                if(right > 2 and right < -2):
                    print("Right Y1: " + str(left))

                
            """

        
            if ev_type != 3 and ev_type != 0:
                print("Event type %u, code %u, value %u at %d.%d" % \
                    (ev_type, code, value, tv_sec, tv_usec))
                
            # Handle PS4 controller buttons
            if ev_type == 1:
                print("Button: " + str(code) + " Value: " + str(value));
            
                # Handle PS4 controller X button
                if code == 304 and value == 1:
                    self.trigger("cross_button");
                # Handle PS4 controller CIRCLE(305) button
                # Handle PS4 controller SQUARE(308) button
                # Handle PS4 controller TRIANGLE(307) button
                    

                # Handle PS4 controller L1(310) button
                # Handle PS4 controller L2(312) button
                # Handle PS4 controller R1(311) button
                # Handle PS4 controller R2(313) button

                # Handle PS4 controller SHARE(314) button
                # Handle PS4 controller OPTIONS(315) button
                if code == 315 and value == 1:
                    self.trigger("options_button");
                # Handle PS4 controller PS(316) button
                # Handle PS4 controller L3(317) button
                # Handle PS4 controller R3(318) button
                            

            # Finally, read another event
            event = in_file.read(EVENT_SIZE)

        in_file.close()

    def handle_event(self, event):
        # Override this method to handle PS4 controller events
        pass
 

    # A helper function for converting stick values (0 - 255)
    # to more usable numbers (-100 - 100)
    def scale(val, src, dst):
        """
        Scale the given value from the scale of src to the scale of dst.
    
        val: float or int
        src: tuple
        dst: tuple
    
        example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
        """
        return (float(val-src[0]) / (src[1]-src[0])) * (dst[1]-dst[0])+dst[0]

    def onLeftJoystickX(self, callback):
        self.on("left_joystick_x", callback)


    def onCrossButton(self, callback):
        self.on("cross_button", callback)


    def onCircleButton(self, callback):
        self.on("circle_button", callback)


    def onL2Button(self, callback):
        self.on("l2_button", callback)

    def onR2Button(self, callback):
        self.on("r2_button", callback)

    def onOptionsButton(self, callback):
        self.on("options_button", callback)
