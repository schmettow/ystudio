"""
Dual toggle
"""


import time
from yui import LED, RGB, Onpress, this_moment

def main():
    State = "Init" # "setRGB", "setLed"
    print(State)
    sign_1 = RGB()
    sign_2 = LED()
    btn_mode = Onpress()
    btn_value = Onpress()

    for btn in (btn_mode, btn_value, sign_1, sign_2):
        btn.connect()

    sign_1.on()
    sign_2.off()

    State = "setRGB"

    while True:
        if btn_mode.update():
            if State == "setRGB":
                State = "setLED"
            else:
                State = "setRGB"
            print(State)

        if btn_value.update():
            if State == "setRGB":
                if sign_1.value:
                    sign_1.off()
                else:
                    sign_1.on()
            elif State == "setLED":
                if sign_2.value:
                    sign_2.off()
                else:
                    sign_2.on()
    return False

main()