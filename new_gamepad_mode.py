import pygame

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN and event.button == 6:
                print("L2")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 7:
                print("R2")


except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
