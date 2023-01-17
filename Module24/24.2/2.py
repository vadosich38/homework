class Monitor:
    vendor = ""
    matrix = ""
    resolution = ""
    fps = ""


class Headphones:
    vendor = ""
    sens = ""
    microphone = False


monitor1 = Monitor()
monitor1.vendor = 'Samsung'
monitor1.matrix = "VA"
monitor1.resolution = "WOHD"
monitor1.fps = 60

monitor2 = Monitor()
monitor2.vendor = 'Samsung'
monitor2.matrix = "VA"
monitor2.resolution = "WOHD"
monitor2.fps = 144

monitor3 = Monitor()
monitor3.vendor = 'Samsung'
monitor3.matrix = "VA"
monitor3.resolution = "WOHD"
monitor3.fps = 70

monitor4 = Monitor()
monitor4.vendor = 'Samsung'
monitor4.matrix = "VA"
monitor4.resolution = "WOHD"
monitor4.fps = 60

headphone1 = Headphones()
headphone1.vendor = 'Sony'
headphone1.sens = 108
headphone1.microphone = False

headphone2 = Headphones()
headphone2.vendor = 'Sony'
headphone2.sens = 108
headphone2.microphone = True

headphone3 = Headphones()
headphone3.vendor = 'Sony'
headphone3.sens = 108
headphone3.microphone = True

print(monitor4.fps, monitor3.fps, monitor2.fps, monitor1.fps)
print(headphone3.microphone, headphone2.microphone, headphone1.microphone)