import RandomizerCore.Tools.event_tools as event_tools
from RandomizerCore.Randomizers import data


# blue_tunic_get = item_get.insertItemGetAnimation(flowchart, 'ClothesBlue', -1, None, auto_save)
# blue_tunic_check = event_tools.createSwitchEvent(flowchart, 'FlowControl', 'CompareString',
#     {'value1': 'itemKey', 'value2': 'ClothesBlue'},
#     {0: blue_tunic_get, 1: red_tunic_check})

# cello_get = item_get.insertItemGetAnimation(flowchart, 'FullMoonCello', -1, None, auto_save)
# cello_check = event_tools.createSwitchEvent(flowchart, 'FlowControl', 'CompareString',
#     {'value1': 'itemKey', 'value2': 'FullMoonCello'},
#     {0: cello_get, 1: blue_tunic_check})

def createItemComparison(flowchart, items):
    event_tools.addEntryPoint(flowchart, 'itemKey')
    last_item = None

    for item in items:
        if item.startswith('$'):
            continue

        get_item = event_tools.createGetItemEvent(flowchart, item, 'itemIndex')
        check_item = event_tools.createSwitchEvent(flowchart, 'FlowControl', 'CompareString',
            {'value1': 'itemKey', 'value2': item},
            {0: get_item, 1: last_item})
        last_item = check_item
    
    event_tools.insertEventAfter(flowchart, 'itemKey', last_item)


def createRandomizerFlowchart(flow, items: set):
    """Creates a new Randomizer flowchart using ItemCommon.bfevfl as a base
    
    Instead of needing to do a massive item check for each individual placement, we only need to make the item events once
    
    Then every event can simply just subflow to Randomizer.bfevfl to entry point {item}"""
    
    flow.name = 'Randomizer'
    flow.flowchart.name = 'Randomizer'
    flowchart = flow.flowchart

    event_tools.insertEventAfter(flowchart, 'get', 'Event0')
    event_tools.insertEventAfter(flowchart, 'Event1', None)

    items.add('ClothesGreen')
    
    for item in items:
        if item.startswith('$'):
            continue
        event_tools.addEntryPoint(flowchart, item)

        if item == 'SwordLv1':
            event_tools.createProgressiveItemSwitch(flowchart, 'SwordLv1', 'SwordLv2',
                data.SWORD_FOUND_FLAG, item, None)
        elif item == 'Shield':
            event_tools.createProgressiveItemSwitch(flowchart, 'Shield', 'MirrorShield',
                data.SHIELD_FOUND_FLAG, item, None)
        elif item == 'PowerBraceletLv1':
            event_tools.createProgressiveItemSwitch(flowchart, 'PowerBraceletLv1', 'PowerBraceletLv2',
                data.BRACELET_FOUND_FLAG, item, None)
        
        elif item == 'MagicPowder_MaxUp':
            give_powder = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
                {'itemKey': 'MagicPowder', 'count': 40, 'index': -1, 'autoEquip': False}, None)
            powder_check = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
                {'symbol': 'GetMagicPowder'}, {0: None, 1: give_powder})
            randomizerGetSubflow(flowchart, item, 1, -1, powder_check)
        elif item == 'Bomb_MaxUp':
            give_bombs = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
                {'itemKey': 'Bomb', 'count': 60, 'index': -1, 'autoEquip': False}, None)
            bombs_check = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
                {'symbol': data.BOMBS_FOUND_FLAG}, {0: None, 1: give_bombs})
            randomizerGetSubflow(flowchart, item, 1, -1, bombs_check)
        elif item == 'Arrow_MaxUp':
            event_tools.createActionChain(flowchart, item, [
                ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False}),
                ('Inventory', 'AddItemByKey', {'itemKey': 'Arrow', 'count': 60, 'index': -1, 'autoEquip': False}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': item})
            ], None)
        
        elif item == 'ZapTrap':
            autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, None)
            stop_event = event_tools.createActionEvent(flowchart, 'Link', 'StopTailorOtherChannel',
                {'channel': 'toolshopkeeper_dmg', 'index': 0}, autosave_event)
            forks = [
                event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'ev_dmg_elec_lp'}),
                event_tools.createActionEvent(flowchart, 'Link', 'PlayTailorOtherChannelEx',
                    {'channel': 'toolshopkeeper_dmg', 'index': 0, 'restart': False, 'time': 1.0}),
                event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
                event_tools.createActionEvent(flowchart, 'Link', 'Damage', {'amount': 6})]
            event_tools.createForkEvent(flowchart, item, forks, stop_event)[0]
        elif item == 'DrownTrap':
            autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, None)
            forks = [
                event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'fall_water'}),
                event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
                event_tools.createActionChain(flowchart, None, [
                    ('Timer', 'Wait', {'time': 1.5}),
                    ('Link', 'Damage', {'amount': 2})])]
            event_tools.createForkEvent(flowchart, item, forks, autosave_event)[0]
        elif item == 'SquishTrap':
            autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, None)
            forks = [
                event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'dmg_press'}),
                event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
                event_tools.createActionEvent(flowchart, 'Timer', 'Wait', {'time': 2.0}),
                event_tools.createActionEvent(flowchart, 'Link', 'Damage', {'amount': 4})]
            event_tools.createForkEvent(flowchart, item, forks, autosave_event)[0]
        elif item == 'DeathballTrap':
            autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, None)
            forks = [
                event_tools.createActionEvent(flowchart, 'Link', 'PlayTailorOtherChannelEx',
                    {'channel': 'GreatFairy_Heal', 'index': 0, 'restart': False, 'time': 0.0}),
                event_tools.createActionChain(flowchart, None, [
                    ('Timer', 'Wait', {'time': 0.1}),
                    ('Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'fall_deathball'})]),
                event_tools.createActionChain(flowchart, None, [
                    ('Hud', 'SetHeartUpdateEnable', {'enable': True}),
                    ('Timer', 'Wait', {'time': 1.5}),
                    ('Link', 'Damage', {'amount': 2})])]
            event_tools.createForkEvent(flowchart, item, forks, autosave_event)[0]
        elif item == 'QuakeTrap':
            autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, None)
            forks = [
                event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'dmg_quake'}),
                event_tools.createActionEvent(flowchart, 'Timer', 'Wait', {'time': 1.5}),
                event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
                event_tools.createActionEvent(flowchart, 'Link', 'Damage', {'amount': 2})]
            event_tools.createForkEvent(flowchart, item, forks, autosave_event)[0]
        
        # if item == 'HydroTrap':
        #     autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, after)
            
        #     forks = [
        #         event_tools.createActionEvent(flowchart, 'Link', 'SetGravityEnable', {'enable': False}),
        #         event_tools.createActionEvent(flowchart, 'Link', 'PlayTailorOtherChannelEx',
        #             {'channel': 'ev_hydrocannon', 'index': 0, 'restart': False, 'time': 0.333}),
        #         event_tools.createActionChain(flowchart, None, [
        #             ('Timer', 'Wait', {'time': 0.333}),
        #             ('Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'ev_hydrocannon'})
        #         ]),
        #         event_tools.createActionChain(flowchart, None, [
        #             ('Timer', 'Wait', {'time': 1.5}),
        #             ('Link', 'StopTailorOtherChannel', {'channel': 'ev_hydrocannon', 'index': 0})
        #         ]),
        #         event_tools.createActionChain(flowchart, None, [
        #             ('Timer', 'Wait', {'time': 2.0}),
        #             ('Link', 'SetGravityEnable', {'enable': True}),
        #             ('Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'fall_from_top'})
        #         ])
        #     ]
        #     return event_tools.createForkEvent(flowchart, before, forks, autosave_event)[0]
        
        elif item == 'FullMoonCello':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'BowWowEvent', 'value': True}),
                ('EventFlags', 'SetFlag', {'symbol': 'DoorOpen_Btl_MoriblinCave_2A', 'value': False}),
                ('EventFlags', 'SetFlag', {'symbol': 'DoorOpen_Btl_MoriblinCave_1A', 'value': False}),
                ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'SurfHarp':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'GhostClear1', 'value': True}),
                ('EventFlags', 'SetFlag', {'symbol': 'Ghost2_Clear', 'value': True}),
                ('EventFlags', 'SetFlag', {'symbol': 'Ghost3_Clear', 'value': True}),
                ('EventFlags', 'SetFlag', {'symbol': 'Ghost4_Clear', 'value': True}),
                ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        

        elif item == 'ClothesRed':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': data.RED_TUNIC_FOUND_FLAG, 'value': True}),
                ('Link', 'PlayTailorOtherChannelEx', {'channel': 'Change_Color_Red_00', 'index': 0, 'restart': False, 'time': 3.58}),
                ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': 'ClothesRed'})
            ], None)
        elif item == 'ClothesBlue':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': data.BLUE_TUNIC_FOUND_FLAG, 'value': True}),
                ('Link', 'PlayTailorOtherChannelEx', {'channel': 'Change_Color_Blue_00', 'index': 0, 'restart': False, 'time': 3.58}),
                ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': 'ClothesBlue'})
            ], None)
        elif item == 'ClothesGreen':
            event_tools.createActionChain(flowchart, item, [
                ('Link', 'PlayTailorOtherChannelEx', {'channel': 'Change_Color_Green_00', 'index': 0, 'restart': False, 'time': 3.58}),
                ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': 'ClothesGreen'})
            ], None)
        
        # ### Medicine
        # if item == 'SecretMedicine':
        #     return event_tools.createActionChain(flowchart, before, [
        #         ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        #         ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''}),
        #         ('Link', 'Heal', {'amount': 99})
        #     ], after)
        
        elif item == 'Bomb':
            flagset = event_tools.createActionEvent(flowchart, 'EventFlags', 'SetFlag',
                {'symbol': data.BOMBS_FOUND_FLAG, 'value': True}, None)
            randomizerGetSubflow(flowchart, item, 60, -1, flagset)
        elif item == 'MagicPowder':
            flagset = event_tools.createActionEvent(flowchart, 'EventFlags', 'SetFlag',
                {'symbol': 'GetMagicPowder', 'value': True}, None)
            randomizerGetSubflow(flowchart, item, 40, -1, flagset)
        
        elif item == 'Bottle':
            bottle_get = event_tools.createActionEvent(flowchart, 'EventFlags', 'SetFlag',
                {'symbol': 'Bottle2Get', 'value': True}, None)
            index_check = event_tools.createSwitchEvent(flowchart, 'FlowControl', 'CompareInt',
                {'value1': 'itemIndex', 'value2': 1},
                {0: None, 1: bottle_get})
            randomizerGetSubflow(flowchart, item, 1, 'itemIndex', index_check)
        
        elif item == 'YoshiDoll':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeYoshiDollGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Ribbon':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeRibbonGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'DogFood':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeDogFoodGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Bananas':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeBananasGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Stick':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeStickGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Honeycomb':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeHoneycombGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Pineapple':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradePineappleGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Hibiscus':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeHibiscusGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Letter':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeLetterGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'Broom':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeBroomGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'FishingHook':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeFishingHookGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'PinkBra':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeNecklaceGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'MermaidsScale':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': 'TradeMermaidsScaleGet', 'value': True}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        elif item == 'MagnifyingLens':
            event_tools.createActionChain(flowchart, item, [
                ('EventFlags', 'SetFlag', {'symbol': data.LENS_FOUND_FLAG, 'value': True}),
                ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False}),
                ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': ''})
            ], None)
        
        else:
            randomizerGetSubflow(flowchart, item, 1, 'itemIndex', None)
            # subfl = event_tools.createSubFlowEvent(flowchart, '', 'get',
            # {'itemKey': item, 'itemCount': 1, 'itemIndex': 'itemIndex'}, None)
            # event_tools.insertEventAfter(flowchart, item, subfl)
            # event_tools.createActionChain(flowchart, item, [
            #     ('Link', 'GenericItemGetSequenceByKey', {'itemKey': item, 'keepCarry': False, 'messageEntry': item}),
            #     ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False})
            # ], None)
    
    createItemComparison(flowchart, items)


def randomizerGetSubflow(flowchart, item, count, index, after=None):
    subfl = event_tools.createSubFlowEvent(flowchart, '', 'get',
        {'itemKey': item, 'itemCount': count, 'itemIndex': index}, after)
    event_tools.insertEventAfter(flowchart, item, subfl)


def insertItemWithoutAnimation(item, index):
    """Same as insertItemGetAnimation but without the Generic ItemGet animation"""
    
    if item == 'PowerBraceletLv1':
        return [
            ('EventFlags', 'SetFlag', {'symbol': data.BRACELET_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
        ]
    
    if item == 'SwordLv1':
        return [
            ('EventFlags', 'SetFlag', {'symbol': data.SWORD_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
        ]
    
    if item == 'Shield':
        return [
            ('EventFlags', 'SetFlag', {'symbol': data.SHIELD_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
        ]
    
    ### Capacity upgrades
    if item == 'MagicPowder_MaxUp':
        return [('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})]

    if item == 'Bomb_MaxUp':
        return [('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})]

    if item == 'Arrow_MaxUp':
        return [('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})]
    
    ### Instrument flags
    if item == 'FullMoonCello':
        return [
            ('EventFlags', 'SetFlag', {'symbol': 'BowWowEvent', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'DoorOpen_Btl_MoriblinCave_2A', 'value': False}),
            ('EventFlags', 'SetFlag', {'symbol': 'DoorOpen_Btl_MoriblinCave_1A', 'value': False}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
        ]
    
    if item == 'SurfHarp': # set flags before giving harp, otherwise ghost requirements will be met during the itemget animation
        return [
            ('EventFlags', 'SetFlag', {'symbol': 'GhostClear1', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'Ghost2_Clear', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'Ghost3_Clear', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'Ghost4_Clear', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
        ]
    
    ### tunics
    if item == 'ClothesRed':
        return [('EventFlags', 'SetFlag', {'symbol': data.RED_TUNIC_FOUND_FLAG, 'value': True})]
    
    if item == 'ClothesBlue':
        return [('EventFlags', 'SetFlag', {'symbol': data.BLUE_TUNIC_FOUND_FLAG, 'value': True})]
    
    ### Medicine
    if item == 'SecretMedicine':
        return [
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
            ('Link', 'Heal', {'amount': 99})
        ]

    ### Shuffled Bombs / Shuffled Powder
    if item == 'Bomb':
        return [
            ('EventFlags', 'SetFlag', {'symbol': data.BOMBS_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 60, 'index': index, 'autoEquip': False})
        ]
    if item == 'MagicPowder':
        return [
            ('EventFlags', 'SetFlag', {'symbol': 'GetMagicPowder', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 40, 'index': index, 'autoEquip': False})
        ]
    
    ### Fishing Minigame Bottle fix, since it wont show up if you have the second bottle in your inventory
    if item == 'Bottle' and index == 1:
        return [
            ('EventFlags', 'SetFlag', {'symbol': 'Bottle2Get', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
        ]

    ### Flippers needs a flag to enable water loading zones that were disabled to prevent rooster softlocks
    if item == 'Flippers':
        return [
            ('EventFlags', 'SetFlag', {'symbol': 'FlippersFound', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
        ]

    ### Trade Quest items
    if item == 'YoshiDoll':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeYoshiDollGet', 'value': True})]

    if item == 'Ribbon':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeRibbonGet', 'value': True})]

    if item == 'DogFood':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeDogFoodGet', 'value': True})]

    if item == 'Bananas':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeBananasGet', 'value': True})]

    if item == 'Stick':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeStickGet', 'value': True})]

    if item == 'Honeycomb':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeHoneycombGet', 'value': True})]

    if item == 'Pineapple':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradePineappleGet', 'value': True})]

    if item == 'Hibiscus':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeHibiscusGet', 'value': True})]

    if item == 'Letter':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeLetterGet', 'value': True})]

    if item == 'Broom':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeBroomGet', 'value': True})]

    if item == 'FishingHook':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeFishingHookGet', 'value': True})]

    if item == 'PinkBra':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeNecklaceGet', 'value': True})]

    if item == 'MermaidsScale':
        return [('EventFlags', 'SetFlag', {'symbol': 'TradeMermaidsScaleGet', 'value': True})]
    
    if item == 'MagnifyingLens':
        return [
            ('EventFlags', 'SetFlag', {'symbol': data.LENS_FOUND_FLAG, 'value': True}),
            ('Inventory', 'SetWarashibeItem', {'itemType': 15})
        ]
    
    ### everything else
    return [('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})]



def insertDampeItemGet(flowchart, item, index, after=None):
    # progressive items
    if item == 'PowerBraceletLv1':
        give_bracelet2 = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': 'PowerBraceletLv2', 'count': 1, 'index': -1, 'autoEquip': False}, after)
        give_bracelet1 = event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': data.BRACELET_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False})
        ], after)
        return event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
            {'symbol': data.BRACELET_FOUND_FLAG}, {0: give_bracelet1, 1: give_bracelet2})

    if item == 'SwordLv1':
        give_sword2 = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': 'SwordLv2', 'count': 1, 'index': -1, 'autoEquip': False}, after)
        give_sword1 = event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': data.SWORD_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False})
        ], after)
        return event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
            {'symbol': data.SWORD_FOUND_FLAG}, {0: give_sword1, 1: give_sword2})
    
    if item == 'Shield':
        give_shield2 = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': 'MirrorShield', 'count': 1, 'index': -1, 'autoEquip': False}, after)
        give_shield1 = event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': data.SHIELD_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': -1, 'autoEquip': False})
        ], after)
        return event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
            {'symbol': data.SHIELD_FOUND_FLAG}, {0: give_shield1, 1: give_shield2})
    
    ### Capacity upgrades
    if item == 'MagicPowder_MaxUp':
        give_powder = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': 'MagicPowder', 'count': 40, 'index': -1, 'autoEquip': False}, after)
        powder_check = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
            {'symbol': 'GetMagicPowder'}, {0: after, 1: give_powder})
        return event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}, powder_check)
    
    if item == 'Bomb_MaxUp':
        give_bombs = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': 'Bomb', 'count': 60, 'index': -1, 'autoEquip': False}, after)
        bombs_check = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag',
            {'symbol': data.BOMBS_FOUND_FLAG}, {0: after, 1: give_bombs})
        return event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}, bombs_check)
    
    if item == 'Arrow_MaxUp':
        return event_tools.createActionChain(flowchart, None, [
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
            ('Inventory', 'AddItemByKey', {'itemKey': 'Arrow', 'count': 60, 'index': -1, 'autoEquip': False}),
        ], after)
    

    ### traps
    if item == 'ZapTrap':
        autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, after)
        stop_event = event_tools.createActionEvent(flowchart, 'Link', 'StopTailorOtherChannel',
            {'channel': 'toolshopkeeper_dmg', 'index': 0}, autosave_event)
        forks = [
            event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'ev_dmg_elec_lp'}),
            event_tools.createActionEvent(flowchart, 'Link', 'PlayTailorOtherChannelEx',
                {'channel': 'toolshopkeeper_dmg', 'index': 0, 'restart': False, 'time': 1.0}),
            event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
            event_tools.createActionEvent(flowchart, 'Link', 'Damage', {'amount': 6})
        ]
        return event_tools.createForkEvent(flowchart, None, forks, stop_event)[0]
    
    if item == 'DrownTrap':
        autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, after)
        forks = [
            event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'fall_water'}),
            event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
            event_tools.createActionChain(flowchart, None, [
                ('Timer', 'Wait', {'time': 1.5}),
                ('Link', 'Damage', {'amount': 2})
            ])
        ]
        return event_tools.createForkEvent(flowchart, None, forks, autosave_event)[0]
    
    if item == 'SquishTrap':
        autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, after)
        forks = [
            event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'dmg_press'}),
            event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
            event_tools.createActionEvent(flowchart, 'Timer', 'Wait', {'time': 2.0}),
            event_tools.createActionEvent(flowchart, 'Link', 'Damage', {'amount': 4})
        ]
        return event_tools.createForkEvent(flowchart, None, forks, autosave_event)[0]
    
    if item == 'DeathballTrap':
        autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, after)
        forks = [
            event_tools.createActionEvent(flowchart, 'Link', 'PlayTailorOtherChannelEx',
                {'channel': 'GreatFairy_Heal', 'index': 0, 'restart': False, 'time': 0.0}),
            event_tools.createActionChain(flowchart, None, [
                ('Timer', 'Wait', {'time': 0.1}),
                ('Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'fall_deathball'})
            ]),
            event_tools.createActionChain(flowchart, None, [
                ('Hud', 'SetHeartUpdateEnable', {'enable': True}),
                ('Timer', 'Wait', {'time': 1.5}),
                ('Link', 'Damage', {'amount': 2})
            ])
        ]
        return event_tools.createForkEvent(flowchart, None, forks, autosave_event)[0]
    
    if item == 'QuakeTrap':
        autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, after)
        forks = [
            event_tools.createActionEvent(flowchart, 'Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'dmg_quake'}),
            event_tools.createActionEvent(flowchart, 'Timer', 'Wait', {'time': 1.5}),
            event_tools.createActionEvent(flowchart, 'Hud', 'SetHeartUpdateEnable', {'enable': True}),
            event_tools.createActionEvent(flowchart, 'Link', 'Damage', {'amount': 6})
        ]
        return event_tools.createForkEvent(flowchart, None, forks, autosave_event)[0]
    
    # if item == 'HydroTrap':
    #     autosave_event = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, after)
        
    #     forks = [
    #         event_tools.createActionEvent(flowchart, 'Link', 'SetGravityEnable', {'enable': False}),
    #         event_tools.createActionEvent(flowchart, 'Link', 'PlayTailorOtherChannelEx',
    #             {'channel': 'ev_hydrocannon', 'index': 0, 'restart': False, 'time': 0.333}),
    #         event_tools.createActionChain(flowchart, None, [
    #             ('Timer', 'Wait', {'time': 0.333}),
    #             ('Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'ev_hydrocannon'})
    #         ]),
    #         event_tools.createActionChain(flowchart, None, [
    #             ('Timer', 'Wait', {'time': 1.5}),
    #             ('Link', 'StopTailorOtherChannel', {'channel': 'ev_hydrocannon', 'index': 0})
    #         ]),
    #         event_tools.createActionChain(flowchart, None, [
    #             ('Timer', 'Wait', {'time': 2.0}),
    #             ('Link', 'SetGravityEnable', {'enable': True}),
    #             ('Link', 'PlayAnimation', {'blendTime': 0.1, 'name': 'fall_from_top'})
    #         ])
    #     ]
    #     return event_tools.createForkEvent(flowchart, before, forks, autosave_event)[0]
    
    ### Instrument flags
    if item == 'FullMoonCello':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'BowWowEvent', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'DoorOpen_Btl_MoriblinCave_2A', 'value': False}),
            ('EventFlags', 'SetFlag', {'symbol': 'DoorOpen_Btl_MoriblinCave_1A', 'value': False}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)
    
    if item == 'SurfHarp': # set flags before giving harp, otherwise ghost requirements will be met during the itemget animation
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'GhostClear1', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'Ghost2_Clear', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'Ghost3_Clear', 'value': True}),
            ('EventFlags', 'SetFlag', {'symbol': 'Ghost4_Clear', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)
    

    ### tunics
    if item == 'ClothesRed':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': data.RED_TUNIC_FOUND_FLAG, 'value': True}),
            ('Link', 'PlayTailorOtherChannelEx', {'channel': 'Change_Color_Red_00', 'index': 0, 'restart': False, 'time': 3.58}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)
    
    if item == 'ClothesBlue':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': data.BLUE_TUNIC_FOUND_FLAG, 'value': True}),
            ('Link', 'PlayTailorOtherChannelEx', {'channel': 'Change_Color_Blue_00', 'index': 0, 'restart': False, 'time': 3.58}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)
    
    if item == 'ClothesGreen':
        return event_tools.createActionChain(flowchart, None, [
            ('Link', 'PlayTailorOtherChannelEx', {'channel': 'Change_Color_Green_00', 'index': 0, 'restart': False, 'time': 3.58}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)
    

    ### Medicine
    if item == 'SecretMedicine':
        return event_tools.createActionChain(flowchart, None, [
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
            ('Link', 'Heal', {'amount': 99})
        ], after)
    

    ### Shuffled Bombs and Powder
    if item == 'Bomb':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': data.BOMBS_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 60, 'index': index, 'autoEquip': False}),
        ], after)
    
    if item == 'MagicPowder':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'GetMagicPowder', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 40, 'index': index, 'autoEquip': False}),
        ], after)
    

    ### Fishing Minigame Bottle fix, since it wont show up if you have the second bottle in your inventory
    if item == 'Bottle' and index == 1:
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'Bottle2Get', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)


    ### Flippers needs a flag to enable water loading zones that were disabled to prevent rooster softlocks
    if item == 'Flippers':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'FlippersFound', 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)


    ### Trade Quest items
    if item == 'YoshiDoll':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeYoshiDollGet', 'value': True}),
        ], after)

    if item == 'Ribbon':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeRibbonGet', 'value': True}),
        ], after)

    if item == 'DogFood':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeDogFoodGet', 'value': True}),
        ], after)

    if item == 'Bananas':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeBananasGet', 'value': True}),
        ], after)

    if item == 'Stick':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeStickGet', 'value': True}),
        ], after)

    if item == 'Honeycomb':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeHoneycombGet', 'value': True}),
        ], after)

    if item == 'Pineapple':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradePineappleGet', 'value': True}),
        ], after)

    if item == 'Hibiscus':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeHibiscusGet', 'value': True}),
        ], after)

    if item == 'Letter':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeLetterGet', 'value': True}),
        ], after)

    if item == 'Broom':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeBroomGet', 'value': True}),
        ], after)

    if item == 'FishingHook':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeFishingHookGet', 'value': True}),
        ], after)

    if item == 'PinkBra':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeNecklaceGet', 'value': True}),
        ], after)

    if item == 'MermaidsScale':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': 'TradeMermaidsScaleGet', 'value': True}),
        ], after)
    
    if item == 'MagnifyingLens':
        return event_tools.createActionChain(flowchart, None, [
            ('EventFlags', 'SetFlag', {'symbol': data.LENS_FOUND_FLAG, 'value': True}),
            ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False}),
        ], after)
    
    ### everything else
    return event_tools.createActionChain(flowchart, None, [
        ('Inventory', 'AddItemByKey', {'itemKey': item, 'count': 1, 'index': index, 'autoEquip': False})
    ], after)
