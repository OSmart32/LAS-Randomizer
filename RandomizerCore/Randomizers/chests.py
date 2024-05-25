import RandomizerCore.Tools.event_tools as event_tools


def writeChestEvent(flowchart):
    """Edits chests to subflow to Randomizer.bfevfl for all non enemy/masterstalfosnote items"""

    auto_save = event_tools.createActionEvent(flowchart, 'GameControl', 'RequestAutoSave', {}, None)
    subfl = event_tools.createGetItemEvent(flowchart, 'itemKey', 'itemIndex', None, auto_save)

    # replace normal chest add item events with the Randomizer.bfevfl subflow
    event_tools.setSwitchEventCase(flowchart, 'Event33', 1, subfl)
    event_tools.setSwitchEventCase(flowchart, 'Event39', 0, subfl)

    # attach to TreasureBox_ShockOpen
    event_tools.insertEventAfter(flowchart, 'Event28', subfl)
    
    # make the game still autosave if medicine gets put back in the chest
    event_tools.insertEventAfter(flowchart, 'Event40', auto_save)

    # make the D6 pot chest check if it contains an enemy
    event_tools.insertEventAfter(flowchart, 'TreasureBox_ShockOpen', 'Event27')
    event_tools.insertEventAfter(flowchart, 'Event15', 'Event28')
    check_enemy = event_tools.createSwitchEvent(flowchart, 'TreasureBox', 'ContainsEnemy',
        {}, {0: 'Event15', 1: 'Event42'})
    event_tools.insertEventAfter(flowchart, 'Event27', check_enemy)


def makeChestsFaster(flowchart):
    '''Speeds up the animation and gives control back to the player a bit sooner'''

    # remove the cameraLookAt event and the secret unlocked music
    del event_tools.findEvent(flowchart, 'Event44').data.forks[0]
    event_tools.insertEventAfter(flowchart, 'Event52', None)

    # COMMENTED OUT BECAUSE EVEN JUST KEEPING THE SAME DATA WOULD CAUSE THIS TO BREAK
    # PROBABLY IS JUST SOME PARAM TYPE BEING WRONG OR SOMETHING
    # now edit Link to move 3x faster if he is in the way of the chest
    # event_tools.findEvent(flowchart, 'Event46').data.params.data['speed'] = 3
    # event_tools.findEvent(flowchart, 'Event46').data.params.data = {
    #     'speed': 3,
    #     'distance': 1.5,
    #     'actor': 'TreasureBox',
    #     'timeOut': 1.0 # idk if there is any instance where timeOut: 7.0 actually matters but just in case we set it to 1.0
    # }