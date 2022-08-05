import Tools.event_tools as event_tools
from Randomizers import item_get
from Randomizers import data



def changeInstrument(flowchart, item_key, item_index, model_path, model_name, room, room_data):
    """Applies changes to both the Instrument actor and the event flowchart"""
    
    if room == 'D6-instrument':
        act = room_data.actors[1]
    else:
        act = room_data.actors[0]

    # store the level and location for the leveljump event since we will overwrite these parameters
    level = str(act.parameters[0], 'utf-8')
    location = str(act.parameters[1], 'utf-8')

    act.type = 0x8E # yoshi doll, will disappear once you have yoshi, but the player never actually obtains it :)
    act.parameters[0] = bytes(model_path, 'utf-8')
    act.parameters[1] = bytes(model_name, 'utf-8')
    act.parameters[2] = bytes(room, 'utf-8') # entry point that we write to flow
    act.parameters[3] = bytes(data.INSTRUMENT_FLAGS[room], 'utf-8') # flag for if item appears

    fade_event = insertInstrumentFadeEvent(flowchart, level, location)
    instrument_get = item_get.insertItemGetAnimation(flowchart, item_key, item_index, None, fade_event)

    event_tools.addEntryPoint(flowchart, room)
    event_tools.createActionChain(flowchart, room, [
        ('SinkingSword', 'Destroy', {}),
        ('EventFlags', 'SetFlag', {'symbol': data.INSTRUMENT_FLAGS[room], 'value': True})
    ], instrument_get)



def insertInstrumentFadeEvent(flowchart, level, location):
    shine_effect = event_tools.createActionChain(flowchart, None, [
        ('Audio', 'StopAllBGM', {'duration': 1.0}),
        ('Link', 'PlayInstrumentShineEffect', {}),
        ('Timer', 'Wait', {'time': 2})
        # ('Audio', 'StopOtherThanSystemSE', {'duration': 3.0}),
        # ('Audio', 'PlayOneshotSystemSE', {'label': 'SE_ENV_GET_INST_WHITEOUT2', 'pitch': 1.0, 'volume': 1.0}),
        # ('Fade', 'StartPreset', {'preset': 3}),
        # ('Fade', 'StartParam', {'colorB': 0.9, 'colorG': 0.9, 'colorR': 0.9, 'mode': 2, 'time': 0.75}),
    ], None)

    level_jump = event_tools.createActionChain(flowchart, None, [
        ('Timer', 'Wait', {'time': 2}),
        ('GameControl', 'RequestLevelJump', {'level': level, 'locator': location, 'offsetX': 0.0, 'offsetZ': 0.0}),
        ('GameControl', 'RequestAutoSave', {})
    ], None)

    return event_tools.createForkEvent(flowchart, shine_effect, [
        event_tools.createActionEvent(flowchart, 'Audio', 'StopOtherThanSystemSE', {'duration': 3.0}),
        event_tools.createActionEvent(flowchart, 'Audio', 'PlayOneshotSystemSE', {'label': 'SE_ENV_GET_INST_WHITEOUT2', 'pitch': 1.0, 'volume': 1.0}),
        event_tools.createActionChain(flowchart, None, [
            ('Fade', 'StartPreset', {'preset': 3}),
            ('Fade', 'StartParam', {'colorB': 0.9, 'colorG': 0.9, 'colorR': 0.9, 'mode': 2, 'time': 0.75})
        ])
    ], level_jump)[0]