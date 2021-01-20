"""Simple example showing how to get gamepad events."""

from __future__ import print_function


from inputs import get_gamepad


def main():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Sync":
                continue
            if event.code == "ABS_RZ":
                print(event.ev_type, event.code, event.state)
            if event.code == "ABS_Z":
                print("                        ",event.ev_type, event.code, event.state)
            if event.code == "ABS_X":
                print("            ",event.ev_type, event.code, event.state/256.0/127.0)
            
            #print("                        -----       ",event.ev_type, event.code, event.state/256.0/127.0)
            
            if event.code.find("BTN_") == 0:
                return

if __name__ == "__main__":
    main()