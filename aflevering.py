import pygame
import time
import math


# Først initierer den pygame og derefter bliver en overflade/vindue lavet 
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Analog Ur")


running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ryder skærmen efter hvert loop
    screen.fill((255, 255, 255))
    
    # Urramme
    clock_radius = 200
    clock_center = (300, 300)
    
    pygame.draw.circle(screen, (0, 0, 0), center=clock_center, radius=clock_radius+25, width=15)
    #minut linjer pr 1 min
    for minute in range(0, 60, 1):
        minute_angle_5 = math.radians(90 - minute * 360 / 60)
        pygame.draw.line(screen, (0, 0, 0), clock_center, (clock_center[0] + clock_radius * math.cos(minute_angle_5),
                                                           clock_center[1] - clock_radius * math.sin(minute_angle_5)), 2)
    #minut linjer pr 5
    for minute in range(0, 60, 5):
        minute_angle_5 = math.radians(90 - minute * 360 / 60)
        pygame.draw.line(screen, (0, 0, 0), clock_center, (clock_center[0] + clock_radius * math.cos(minute_angle_5),
                                                           clock_center[1] - clock_radius * math.sin(minute_angle_5)), 6)   
        pygame.draw.circle(screen, (255, 255, 255), center=(300, 300), radius=180, width=0)
        
    # henter den nuværende tid
    current_time = time.localtime()
    hour_angle = math.radians(90 - (current_time.tm_hour % 12) * 360 / 12)
    minute_angle = math.radians(90 - current_time.tm_min * 360 / 60)
    second_angle = math.radians(90 - current_time.tm_sec * 360 / 60)

    #Viserne tegnes
    pygame.draw.line(screen, (0, 0, 0), clock_center, (clock_center[0] + (clock_radius-60) * math.cos(hour_angle),
                                                       clock_center[1] - (clock_radius-60) * math.sin(hour_angle)), 6)
    pygame.draw.line(screen, (0, 0, 0), clock_center, (clock_center[0] + (clock_radius-35) * math.cos(minute_angle),
                                                       clock_center[1] - (clock_radius-35) * math.sin(minute_angle)), 4)
    pygame.draw.line(screen, (255, 0, 0), clock_center, (clock_center[0] + (clock_radius-25) * math.cos(second_angle),
                                                       clock_center[1] - (clock_radius-25) * math.sin(second_angle)), 2)  # Red second hand

    #opdaterer skærmen
    pygame.display.flip()
pygame.quit()