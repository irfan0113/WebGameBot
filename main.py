#A web game bot by Muhammed Irfan https://www.github.com/Irfan0113
#Game - Sushi Go Round

import pyautogui
import time
import os
import logging
import sys
import random
import copy

#For Debugging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d:%(message)s', datefmt='%H:%M:%S')
# TODO: Remove this comment after Debugging
#logging.disable(logging.DEBUG)

#FOOD

ONIGIRI = 'onigiri'
GUNKAN_MAKI = 'gunkan_maki'
CALIFORNIA_ROLL = 'california_roll'
SALMON_ROLL = 'salmon_roll'
SHRIMP_SUSHI = 'shrimp_sushi'
UNAGI_ROLL = 'unagi_roll'
DRAGON_ROLL = 'dragon_roll'
COMBO = 'combo'
ALL_ORDER_TYPE = (ONIGIRI, GUNKAN_MAKI, CALIFORNIA_ROLL, SALMON_ROLL, SHRIMP_SUSHI, UNAGI_ROLL, DRAGON_ROLL, COMBO)

#INGREDIENTS

SHRIMP = 'shrimp'
RICE = 'rice'
NORI = 'nori'
ROE = 'roe'
SALMON  = 'salmon'
UNAGI = 'unagi'

RECIPE = {ONIGIRI: {RICE : 2, NORI : 1},
          CALIFORNIA_ROLL: {RICE : 1, NORI : 1, ROE : 1},
          GUNKAN_MAKI : {RICE : 1, NORI : 1, ROE : 2},
          SALMON_ROLL : {RICE : 1, NORI : 1, SALMON : 2},
          SHRIMP_SUSHI : {RICE : 1, NORI : 1, SHRIMP : 2},
          UNAGI_ROLL : {RICE : 1, NORI : 1, UNAGI : 2},
          DRAGON_ROLL : {RICE : 2, NORI : 1, ROE : 1, UNAGI : 2},
          COMBO : {RICE : 2, NORI : 1, ROE : 1, SALMON : 1, UNAGI : 1, SHRIMP : 1},}



#TODO: Better Message
LEVEL_WIN_MESSAGE = 'win'

#SETTINGS

MIN_INGREDIENTS = 4
PLATE_CLEARING_FREQ = 8
NORMAL_RESTOCK_TIME = 7
TIME_TO_REMAKE = 30

LEVEL = 1
INVENTORY = {SHRIMP : 5, RICE : 10,
             NORI : 10, ROE : 10,
             SALMON : 5, UNAGI : 5}

ORDERING_COMPLETE = {SHRIMP : None, RICE : None,
             NORI : None, ROE : None,
             SALMON : None, UNAGI : None}

GAME_REGION = ()
ROLLING_COMPLETE = 0
LAST_PLATE_CLEARING = 0
LAST_GAME_OVER_CHECK = 0
INGRED_COORDS = None
PHONE_COORDS = None
TOPPING_COORDS = None
ORDER_BUTTON_COORDS = None
RICE1_COORDS = None
RICE2_COORDS = None
NORMAL_DELIVERY_BUTTON_COORDS = None
MAT_COORDS = None


def main():
    logging.debug('Program Started.')
    # loggin.debug('To interrupt mouse movement, move mouse to upper left corner')
    getGameRegion()
    navigateStartGameMenu()
    setupCoordinates()
    startServing()
    
def imPath(filename):
    return os.path.join('images', filename)

def getGameRegion():
    
    global GAME_REGION
    logging.debug('Capturing Screen Size.....')
    region = pyautogui.locateOnScreen(imPath('top_right_corner.png'))
    
    if region is None:
        raise Exception('Failed to capture screen.. Make sure the game is open..')
    
    topRightX = region[0] + region[2]
    topRightY = region[1]
    GAME_REGION = (topRightX - 640, topRightY, 640, 480) #Screen Size is always 640x480
    logging.debug('-----Game region FOUND Successfully : %s ----' &(GAME_REGION,))
    
def setupCoordinates():
    
    global INGRED_COORDS, PHONE_COORDS, TOPPING_COORDS, ORDER_BUTTON_COORDS, RICE1_COORDS, RICE2_COORDS, NORMAL_DELIVERY_BUTTON_COORDS, MAT_COORDS, LEVEL
    
    INGRED_COORDS = {SHRIMP :   (GAME_REGION[0] + 40, GAME_REGION[1] + 335),
                     RICE :     (GAME_REGION[0] + 95, GAME_REGION[1] + 335),
                     NORI :     (GAME_REGION[0] + 40, GAME_REGION[1] + 385),
                     ROE :      (GAME_REGION[0] + 95, GAME_REGION[1] + 385),
                     SALMON :   (GAME_REGION[0] + 40, GAME_REGION[1] + 425),
                     UNAGI :    (GAME_REGION[0] + 95, GAME_REGION[1] + 425),}
    
    PHONE_COORDS = (GAME_REGION[0] + 513, GAME_REGION[1] + 360)
    TOPPING_COORDS = (GAME_REGION[0] + 513, GAME_REGION[1] + 269)
    
    ORDER_BUTTON_COORDS = {SHRIMP: (GAME_REGION[0] + 496, GAME_REGION[1] + 222),
                           UNAGI:  (GAME_REGION[0] + 578, GAME_REGION[1] + 222),
                           NORI:   (GAME_REGION[0] + 496, GAME_REGION[1] + 281),
                           ROE:    (GAME_REGION[0] + 578, GAME_REGION[1] + 281),
                           SALMON: (GAME_REGION[0] + 496, GAME_REGION[1] + 329),}
    
    RICE1_COORDS = (GAME_REGION[0] + 543, GAME_REGION[1] + 294)
    RICE2_COORDS = (GAME_REGION[0] + 545, GAME_REGION[1] + 269)
    
    NORMAL_DELIVERY_BUTTON_COORDS = (GAME_REGION[0] + 495, GAME_REGION[1] + 293)
    MAT_COORDS = (GAME_REGION[0] + 190, GAME_REGION[1] + 375)
    LEVEL = 1
    
def navigateStartGameMenu():
    
    logging.debug('-----Looking for PLAY button----')
    
    while True:
        pos = pyautogui.locateCenterOnScreen(imPath('play_button.png'), region = GAME_REGION)
        
        if pos is not None:
            break
        
    pyautogui.click(pos, duration=0.25)
    logging.debug('PLAY Button Pressed')
    
    logging.debug('-----Looking for CONTINUE Button-----')
    pos = pyautogui.locateCenterOnScreen(imPath('continue_button.png'), region=GAME_REGION)
    pyautogui.click(pos, duration=0.25)
    logging.debug('CONTINUE Button Pressed')
    
    logging.debug('-----Looking for SKIP Button-----')
    
    while True:
        pos = pyautogui.locateCenterOnScreen(imPath('skip_button.png'), region=GAME_REGION)
        
        if pos is not None:
            break
        
    pyautogui.click(pos, duration=0.25)
    logging.debug('SKIP Button Pressed')
    
    logging.debug('-----Looking for CONTINUE Button-----')
    pos = pyautogui.locateCenterOnScreen(imPath('continue_button.png'), region=GAME_REGION)
    pyautogui.click(pos, duration=0.25)
    logging.debug('CONTINUE Button Pressed')
        
def startServing():
    global LAST_GAME_OVER_CHECK, INVENTORY, ORDERING_COMPLETE, LEVEL
    
    oldOrders = {}
    backOrders = {}
    remakeOrders = {}
    remakeTimes = {}
    LAST_GAME_OVER_CHECK = time.time()
    
    ORDERING_COMPLETE = {SHRIMP : None, RICE : None, NORI : None,
                         ROE : None, SALMON : None, UNAGI : None}
    
    while True:
        currentOrders = getOrders()
        added, removed = getOrdersDifference(currentOrders, oldOrders)
        
        if added != {}:
            logging.debug('New orders : %s' %list(added.values()))
            
            for k in added:
                remakeTimes[k] = time.time() + TIME_TO_REMAKE
        
        if removed != {}:
            logging.debug('Removed orders: %s' %list(removed.values()))
            
            for k in removed:
                del remakeTimes[k]

