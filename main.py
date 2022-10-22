import random
import pygame
import pygame_textinput
from eeveeClass import eeveePet
from musicManager import playMusic
from textManager import textManager
from imgManager import imgManager
from barManager import barManager
from feedingManager import feedingManager
from statsManager import stats

clock = pygame.time.Clock()

# Game status
Game_screen = 0

# Setting up game window
w, h = 600, 440
screen = pygame.display.set_mode((w, h))
backgroundColor = 255, 255, 255

# Creating a eevee
playerEevee = eeveePet('null', 0, 0)

# Setting up the name imput
nameInput = pygame_textinput.TextInputVisualizer()

# Setting up the text used in the game
font = pygame.font.Font('assets/fonts/pokemon_pixel_font.ttf', 32)
textNameRequest = font.render('Please name your eevee', True, (0, 0, 0), (255, 255, 255))

# text surface object
textRectNameRequest = textNameRequest.get_rect()

# set the center of the rectangular object.
textRectNameRequest.center = (w // 2, h // 2)

# Timer for events
can_suffer, is_suffering, gettingDirty, is_gettingDirty = False, False, False, False
aging = pygame.USEREVENT + 1
hunger = pygame.USEREVENT + 2
dirt = pygame.USEREVENT + 3
health = pygame.USEREVENT + 4

# Stats for evolution
numberofWash, numberofFeed = 0, 0
has_evolved = False

# Health, hunger, dirt status
health_status, hunger_status, dirt_status = 4, 4, 4

# Feed minigame data
feedEeveeX = w / 2
is_moving = False
direction = 'left'
EeveeFlip = False
fruit_generated = False
fruit_score = 0

# Wash minigame data
dirtyEeveeX = w / 2
dirtyEeveeY = h / 2
dirtyTimer = pygame.USEREVENT + 5
dirtyScore = 0

window_rect = screen.get_rect()
loop = True

is_playing_minigame, is_playing_main = False, False
miniGameSong = None
mainScreenSong = None

while loop:

    if health_status == 0:
        Game_screen = 4
        can_suffer = False

    screen.fill(backgroundColor)
    events = pygame.event.get()

    if can_suffer and not is_suffering:
        # Aging
        pygame.time.set_timer(aging, 900)
        # Hunger
        pygame.time.set_timer(hunger, 250)
        # Dirty
        pygame.time.set_timer(dirt, 200)
        # HealthCheck
        pygame.time.set_timer(health, 100)

        is_suffering = True

    elif not can_suffer and is_suffering:
        # Aging
        pygame.time.set_timer(aging, 0)
        # Hunger
        pygame.time.set_timer(hunger, 0)
        # Dirty
        pygame.time.set_timer(dirt, 0)
        # HealthCheck
        pygame.time.set_timer(health, 0)

        is_suffering = False
        can_suffer = False

    if gettingDirty and not is_gettingDirty:
        pygame.time.set_timer(dirtyTimer, 5000)
        is_gettingDirty = True
    elif not gettingDirty and is_gettingDirty:
        pygame.time.set_timer(dirtyTimer, 0)
        gettingDirty = False
        is_gettingDirty = False

    if Game_screen == 1:
        pygame.display.set_caption('Take care of ' + str(playerEevee.name))
        if is_playing_minigame and not is_playing_main:
            miniGameSong.stop()
            mainScreenSong = playMusic('assets/music/mainTheme.wav', 0.2, False)
            is_playing_main = True
            is_playing_minigame = False

        if not is_playing_minigame and not is_playing_main:
            mainScreenSong = playMusic('assets/music/mainTheme.wav', 0.2, False)
            is_playing_main = True

        can_suffer = True
        # Main screen
        eeveeimg = imgManager(screen, 80, h // 2, True, str(playerEevee.img), 60 * 2, 50 * 2)

        feedbtn = imgManager(screen, w / 3 - 95, (h - 40), False, 'assets/UI/feed.png', 30 * 4, 20 * 4)
        washbtn = imgManager(screen, w / 2 - 70, (h - 40), False, 'assets/UI/wash.png', 30 * 4, 20 * 4)

        barManager(screen, w // 2 + 90, h // 2 - 40, 'health', health_status)
        barManager(screen, w // 2 + 90, h // 2, 'hunger', hunger_status)
        barManager(screen, w // 2 + 90, h // 2 + 40, 'dirt', dirt_status)

        # Putting eevee age on screen
        textManager('Age : ' + str(playerEevee.age), font, screen, 80, h // 2 + 70)
        # Putting eevee name on screen
        textManager(str(playerEevee.name), font, screen, 80, h // 3)

    elif Game_screen == 0:
        pygame.display.set_caption('Name your pokemon')
        if not is_playing_minigame:
            miniGameSong = playMusic('assets/music/name_select.wav', 0.2, False)
        is_playing_minigame = True

        # Screen to ask for eevee Name
        screen.blit(textNameRequest, textRectNameRequest)
        nameInput.update(events)
        # Blit its surface onto the screen
        screen.blit(nameInput.surface, (w // 3 + 100, h // 2 + 20))

    elif Game_screen == 2:
        pygame.display.set_caption('Use the arrow keys to move around ! Get all the fruits')
        if is_playing_main == True:
            mainScreenSong.stop()
            miniGameSong = playMusic('assets/music/Mini-Games-feed.wav', 0.2, False)
            is_playing_minigame = True
            is_playing_main = False
        # Screen for feeding minigame
        feedEeveeImg = imgManager(screen, feedEeveeX, (h - 60), EeveeFlip, str(playerEevee.img), 60 * 2, 50 * 2)

        if fruit_generated:
            for fruit in fruits.objs:
                if len(fruits.objs) == 0:
                    fruit_generated = False
                if not window_rect.contains(fruit.rect):
                    fruit_generated = False

                if feedEeveeImg.rect.contains(fruit.rect):
                    if fruit.value == 'assets/fruits/bomb.png':
                        fruit_generated = False
                        is_moving = False
                        fruit_score = 0
                        feedEeveeX = w / 2
                        Game_screen = 1

                    elif fruit.value == 'assets/fruits/oran_berry.png':
                        fruits.objs.remove(fruit)
                        fruit_score += 1

                fruit.rect.y += 10
                screen.blit(fruit.imgDone, fruit.rect)

        if fruit_score >= 5:
            playerEevee.hunger = 0
            is_moving = False
            numberofFeed += 1
            Game_screen = 1
            fruit_score = 0

        if is_moving == True and direction == 'left':
            EeveeFlip = False
            feedEeveeX -= 10
        if is_moving == True and direction == 'right':
            EeveeFlip = True
            feedEeveeX += 10

    elif Game_screen == 3:
        pygame.display.set_caption('Click on your pokemon to clean him !')
        if is_playing_main == True:
            mainScreenSong.stop()
            miniGameSong = playMusic('assets/music/wash_minigame.wav', 0.2, False)
            is_playing_minigame = True
            is_playing_main = False
        flip = random.choice([False, True])
        dirtEeveeImg = imgManager(screen, dirtyEeveeX, dirtyEeveeY, flip, str(playerEevee.img), 60 * 2, 50 * 2)

    elif Game_screen == 4:
        pygame.display.set_caption('Your pokemon as perish...')
        if is_playing_main == True:
            mainScreenSong.stop()
            miniGameSong = playMusic('assets/music/game_over.wav', 0.2, False)
            is_playing_minigame = True
            is_playing_main = False
        grave = imgManager(screen, w / 2, h / 2, False, 'assets/UI/grave.png', 96 * 2, 96 * 2)

    for event in events:
        # Controls for feeding minigame
        if Game_screen == 2:
            if not fruit_generated:
                fruits = feedingManager(screen, w, 0)
                fruit_generated = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                is_moving = True
                direction = 'left'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                is_moving = True
                direction = 'right'
            else:
                is_moving = False

        if event.type == pygame.MOUSEBUTTONDOWN and Game_screen == 3:
            gettingDirty = True
            x, y = event.pos
            if dirtEeveeImg.rect.collidepoint(x, y):
                dirtyScore += 1
                dirtyEeveeX = random.randint(30, w)
                dirtyEeveeY = random.randint(30, h)

        if event.type == dirtyTimer:
            if dirtyScore < 5:
                dirtyScore = 0
                gettingDirty = False
                dirtyEeveeX = w / 2
                dirtyEeveeY = h / 2
                Game_screen = 1

            elif dirtyScore > 5:
                dirtyScore = 0
                playerEevee.dirt = 0
                numberofWash += 1
                gettingDirty = False
                dirtyEeveeX = w / 2
                dirtyEeveeY = h / 2
                Game_screen = 1

        if event.type == pygame.MOUSEBUTTONDOWN and Game_screen == 1:
            if event.button == 1:
                if feedbtn.rect.collidepoint(event.pos):
                    can_suffer = False
                    Game_screen = 2
                elif washbtn.rect.collidepoint(event.pos):
                    can_suffer = False
                    Game_screen = 3

        if event.type == aging:
            playerEevee.age += 1
            # evolution management

            if playerEevee.age >= 25 and not has_evolved:
                if numberofWash > numberofFeed:
                    playerEevee.img = 'assets/forms/vaporeon.png'
                    has_evolved = True
                elif numberofWash < numberofFeed:
                    playerEevee.img = 'assets/forms/flareon.png'
                    has_evolved = True
                elif numberofWash == numberofFeed:
                    playerEevee.img = 'assets/forms/jolteon.png'
                    has_evolved = True

        if event.type == health:
            playerEevee.health = 150 - ((playerEevee.dirt + playerEevee.hunger) // 2)
            healthcheck = stats('health', playerEevee, health_status, 0, 0, playerEevee.health)
            health_status = healthcheck.status

        if event.type == hunger:
            playerEevee.hunger += 1
            hungercheck = stats('hunger', playerEevee, hunger_status, 0, playerEevee.hunger, 0)
            hunger_status = hungercheck.status

        if event.type == dirt:
            playerEevee.dirt += 1
            dirtcheck = stats('dirt', playerEevee, dirt_status, playerEevee.dirt, 0, 0)
            dirt_status = dirtcheck.status

        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and Game_screen == 0:
            if playerEevee.name == "null":
                playerEevee.name = nameInput.value
                Game_screen = 1

    pygame.display.update()
    clock.tick(30)

pygame.quit()
