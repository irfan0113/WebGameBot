#A web game bot by Muhammed Irfan
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
          COMBO : {RICE : 2, NORI : 1, ROE : 1, SALMON : 1, UNAGI : 1, SHRIMP : 1},
}



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

#TODO: Get coordinates of gamewindow
GAME_REGION = () #L,T,W,H
ORDERING_COMPLETE = {SHRIMP : None, RICE : None,
             NORI : None, ROE : None,
             SALMON : None, UNAGI : None}