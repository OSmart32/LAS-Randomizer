# This script handles editing everything related to the shop

# We created new item entries for the shop items
# Buying an item gives the real item via EventFlow
# Stealing gives the fake item which sets its gettingFlag for us to check what was stolen

import RandomizerCore.Tools.event_tools as event_tools
from RandomizerCore.Randomizers import item_get, data
import random


def makeDatasheetChanges(sheet, placements, item_defs, rand_state: tuple) -> tuple:
    """Edit the ShopItem datasheet for the new items"""

    random.setstate(rand_state)

    for slot in sheet['values']:
        if slot['mIndex'] == 2:
            item = placements['shop-slot3-1st'] # shovel
            slot['mGoods'][0]['mItem'] = 'ShopShovel'
            path, model = getItemGraphics(item_defs[item])
            slot['mGoods'][0]['mModelPath'] = f"actor/{path}"
            slot['mGoods'][0]['mModelName'] = model
            slot['mGoods'][0]['mIndex'] = -1

            item = placements['shop-slot3-2nd'] # bow
            slot['mGoods'][1]['mItem'] = 'ShopBow'
            path, model = getItemGraphics(item_defs[item])
            slot['mGoods'][1]['mModelPath'] = f"actor/{path}"
            slot['mGoods'][1]['mModelName'] = model
            slot['mGoods'][1]['mIndex'] = -1

        if slot['mIndex'] == 5:
            item = placements['shop-slot6'] # heart piece
            slot['mGoods'][0]['mItem'] = 'ShopHeart'
            path, model = getItemGraphics(item_defs[item])
            slot['mGoods'][0]['mModelPath'] = f"actor/{path}"
            slot['mGoods'][0]['mModelName'] = model
            slot['mGoods'][0]['mIndex'] = -1

    return random.getstate()


def makeBuyingEventChanges(flowchart, placements, item_defs):
    """Edit the ToolShopKeeper EventFlow for the new items"""

    # shovel
    item = placements['shop-slot3-1st']
    item_key = item_defs[item]['item-key']
    item_index = placements['indexes']['shop-slot3-1st'] if 'shop-slot3-1st' in placements['indexes'] else -1
    event_tools.setSwitchEventCase(flowchart, 'Event50', 1, 'Event52')
    event_tools.insertEventAfter(flowchart, 'Event52', 'Event61')
    item_get.insertItemGetAnimation(flowchart, item_key, item_index, 'Event53', 'Event43')
    event_tools.findEvent(flowchart, 'Event43').data.params.data['symbol'] = 'ShopShovelGet'

    # bow
    item = placements['shop-slot3-2nd']
    item_key = item_defs[item]['item-key']
    item_index = placements['indexes']['shop-slot3-2nd'] if 'shop-slot3-2nd' in placements['indexes'] else -1
    event_tools.setSwitchEventCase(flowchart, 'Event12', 1, 'Event14')
    event_tools.insertEventAfter(flowchart, 'Event14', 'Event65')
    item_get.insertItemGetAnimation(flowchart, item_key, item_index, 'Event17', 'Event151')
    event_tools.findEvent(flowchart, 'Event151').data.params.data['symbol'] = 'ShopBowGet'

    # heart piece
    item = placements['shop-slot6']
    item_key = item_defs[item]['item-key']
    item_index = placements['indexes']['shop-slot6'] if 'shop-slot6' in placements['indexes'] else -1
    set_flag = event_tools.createActionEvent(flowchart, 'EventFlags', 'SetFlag',
        {'symbol': 'ShopHeartGet', 'value': True})
    item_get.insertItemGetAnimation(flowchart, item_key, item_index, 'Event122', set_flag)


def makeStealingEventChanges(flowchart, placements, item_defs):
    """Edit the PlayerStart EventFlow to check for stolen item flags when exiting the shop
    
    The real item is then given to the player, and the stolen flag is set to False"""

    remove_heart = event_tools.createActionChain(flowchart, None, [
        ('EventFlags', 'SetFlag', {'symbol': 'ShopHeartGet', 'value': True}),
        ('EventFlags', 'SetFlag', {'symbol': 'ShopHeartSteal', 'value': False}),
    ], 'Event773')
    give_heart = item_get.insertItemGetAnimation(flowchart,
        item_defs[placements['shop-slot6']]['item-key'],
        placements['indexes']['shop-slot6'] if 'shop-slot6' in placements['indexes'] else -1,
        before=None, after=remove_heart
    )
    check_heart = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
        {'symbol': 'ShopHeartSteal'}, {0: 'Event773', 1: give_heart})

    remove_bow = event_tools.createActionChain(flowchart, None, [
        ('EventFlags', 'SetFlag', {'symbol': 'ShopBowGet', 'value': True}),
        ('EventFlags', 'SetFlag', {'symbol': 'ShopBowSteal', 'value': False}),
    ], check_heart)
    give_bow = item_get.insertItemGetAnimation(flowchart,
        item_defs[placements['shop-slot3-2nd']]['item-key'],
        placements['indexes']['shop-slot3-2nd'] if 'shop-slot3-2nd' in placements['indexes'] else -1,
        before=None, after=remove_bow
    )
    check_bow = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
        {'symbol': 'ShopBowSteal'}, {0: check_heart, 1: give_bow})
    
    remove_shovel = event_tools.createActionChain(flowchart, None, [
        ('EventFlags', 'SetFlag', {'symbol': 'ShopShovelGet', 'value': True}),
        ('EventFlags', 'SetFlag', {'symbol': 'ShopShovelSteal', 'value': False}),
    ], check_bow)
    give_shovel = item_get.insertItemGetAnimation(flowchart,
        item_defs[placements['shop-slot3-1st']]['item-key'],
        placements['indexes']['shop-slot3-1st'] if 'shop-slot3-1st' in placements['indexes'] else -1,
        before=None, after=remove_shovel
    )
    check_shovel = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
        {'symbol': 'ShopShovelSteal'}, {0: check_bow, 1: give_shovel})
    
    event_tools.insertEventAfter(flowchart, 'Event771', check_shovel)
    del event_tools.findEvent(flowchart, 'Event773').data.forks[1] # remove stealing text


def getItemGraphics(item_info) -> tuple:
    """Gets the graphics info for the item
    
    This function is temporary until I write a specific script to globally handle graphics"""

    path = item_info['model-path']
    model = item_info['model-name']
    if model == 'ToolShopkeeper':
        model = random.choice(list(data.ITEM_MODELS.keys()))
        path = data.ITEM_MODELS[model]
    return path, model