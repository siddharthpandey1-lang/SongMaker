import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SongMaker")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

# Fonts
title_font = pygame.font.SysFont("Georgia", 48, bold=True)
body_font = pygame.font.SysFont("Segoe UI", 28)
desc_font = pygame.font.SysFont("Segoe UI", 24, italic=True)
welcome_font = pygame.font.SysFont("Segoe UI", 32, bold=True)

# Song data
name = "I Love the Nights"
description = "A haunting ballad of heartbreak, fury, and longing."
lyrics = [
    "Shadows fall, your memory burns,",
    "Every page, my heart still turns.",
    "I scream your name into the cold,",
    "But no one listens, no one holds.",
    "",
    "Pre-Chorus",
    "Anger rises where love once lived,",
    "Bitter lessons that life won’t forgive.",
    "I’m tangled in the web of what we were,",
    "Every word from you, still a blur.",
    "",
    "Chorus",
    "I love the nights, though they tear me apart,",
    "Sadness and fury still live in my heart.",
    "Through the silence, through the cries,",
    "I love the nights, where love never dies.",
    "",
    "Verse 2",
    "Your laughter haunts the empty hall,",
    "I chase your shadow, I hit the wall.",
    "I burn bridges I once called home,",
    "And drown in memories I can’t disown.",
    "",
    "Pre-Chorus 2",
    "I hate the truth, I hate the lies,",
    "But I can’t escape your hollow eyes.",
    "Love’s a curse I can’t erase,",
    "A twisted beauty I can’t replace.",
    "",
    "Chorus",
    "I love the nights, though they tear me apart,",
    "Sadness and fury still live in my heart.",
    "Through the silence, through the cries,",
    "I love the nights, where love never dies.",
    "",
    "Bridge / Twist",
    "Was it love or just a game?",
    "I burn in anger, whisper your name.",
    "Every ending is a start,",
    "Every shadow a piece of my heart.",
    "I’m lost in fury, lost in desire,",
    "But even in fire, I feel you inspire.",
    "",
    "Final Chorus",
    "I love the nights, where the darkness sings,",
    "Of broken promises and shattered wings.",
    "Through the rage, through the pain,",
    "I love the nights, I love the rain.",
    "Even if love is cruel and unkind,",
    "I love the nights where you’re still mine."
]

# Fade-in effect
def fade_in(surface, duration=2):
    fade = pygame.Surface((WIDTH, HEIGHT))
    for alpha in range(0, 255, 5):
        fade.set_alpha(alpha)
        fade.fill(BLACK)
        screen.blit(surface, (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(int(duration * 1000 / 51))

# Fade-out effect
def fade_out(duration=2):
    fade = pygame.Surface((WIDTH, HEIGHT))
    for alpha in range(255, 0, -5):
        fade.set_alpha(alpha)
        fade.fill(BLACK)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(int(duration * 1000 / 51))

# Welcome screen
def show_welcome():
    screen.fill(BLACK)
    lines = [
        "Welcome to SongMaker!",
        "This is a simple music creation tool.",
        "You can create, edit, and play your own songs.",
        "Let's get started!",
        "Type 'help' to see a list of commands.",
        "Type 'alt+F4' to quit the program.",
        "Enjoy making music!",
        "Remember to save your work frequently!"
    ]
    y = 80
    for line in lines:
        text = welcome_font.render(line, True, CYAN)
        screen.blit(text, (50, y))
        y += 50
    pygame.display.update()
    time.sleep(4)
    fade_out()

# Song display
def render_song():
    screen.fill(BLACK)
    y = 40
    screen.blit(title_font.render(name, True, WHITE), (50, y))
    y += 60
    screen.blit(desc_font.render(description, True, WHITE), (50, y))
    y += 40

    for line in lyrics:
        if y > HEIGHT - 40:
            break
        text = body_font.render(line, True, WHITE)
        screen.blit(text, (50, y))
        y += 35

    pygame.display.update()

# Main loop
show_welcome()
render_song()
fade_in(screen)

running = True
start_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fade_out()
            running = False
    if time.time() - start_time > 25:
        fade_out()
        running = False

pygame.quit()
sys.exit()