import pygame

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION and event.axis == 0:
                print("steer")
            elif event.type == pygame.JOYAXISMOTION and event.axis == 2:
                print("throttle")
            elif event.type == pygame.JOYAXISMOTION and event.axis == 3:
                print("break")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 2:
                print("O")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                print("+")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 5:
                print("-")

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
