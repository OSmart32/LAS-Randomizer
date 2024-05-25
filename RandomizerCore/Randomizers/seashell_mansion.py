import RandomizerCore.Tools.event_tools as event_tools
from RandomizerCore.Randomizers import data


def makeEventChanges(flowchart, placements):
    # 40 shells, doesn't use a present box
    event_tools.findEvent(flowchart, 'Event65').data.forks.pop(0)

    event_tools.insertEventAfter(flowchart, 'Event64', 'Event65')

    # Remove the thing to show Link's sword because it will show L1 sword if he has none. 
    sword_check1 = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag', {'symbol': data.SWORD_FOUND_FLAG}, {0: 'Event65', 1: 'Event64'})
    event_tools.insertEventAfter(flowchart, 'Event80', sword_check1)

    # However, leave it the 2nd time if he's going to get one here.
    if placements['40-seashell-reward'] != 'sword':
        sword_check2 = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag', {'symbol': data.SWORD_FOUND_FLAG}, {0: 'Event48', 1: 'Event47'})
        event_tools.insertEventAfter(flowchart, 'Event54', sword_check2)
    
    # Special case, if there is a sword here, then actually give them item before the end of the animation so it looks like the vanilla cutscene :)
    if placements['40-seashell-reward'] == 'sword':
        early_give_sword1 = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey', {'itemKey': 'SwordLv1', 'count': 1, 'index': -1, 'autoEquip': False}, 'Event19')
        early_give_sword2 = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey', {'itemKey': 'SwordLv2', 'count': 1, 'index': -1, 'autoEquip': False}, 'Event19')
        sword_check3 = event_tools.createSwitchEvent(flowchart, 'EventFlags', 'CheckFlag', {'symbol': data.SWORD_FOUND_FLAG}, {0: early_give_sword1, 1: early_give_sword2})
        event_tools.insertEventAfter(flowchart, 'Event74', sword_check3)
    else:
        event_tools.insertEventAfter(flowchart, 'Event74', 'Event19')

