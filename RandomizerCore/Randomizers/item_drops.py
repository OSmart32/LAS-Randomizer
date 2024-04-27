def makeDatasheetChanges(sheet, placements, item_defs, settings):
    """Iterates through all the values in the ItemDrop datasheet and makes changes"""
    
    for value in sheet['values']:
        if value['mKey'].startswith('HeartContainer'):
            value['mLotTable'][0]['mType'] = ''
        
        if value['mKey'] == 'AnglerKey':
            value['mLotTable'][0]['mType'] = ''
        if value['mKey'] == 'FaceKey':
            value['mLotTable'][0]['mType'] = ''
        if value['mKey'] == 'HookShot':
            value['mLotTable'][0]['mType'] = ''
        
        if value['mKey'] == 'Bomb':
            if settings['reduce-farming']:
                value['mLotTable'][0]['mCookie'] = 3
        
        if value['mKey'] == 'MagicPowder':
            if settings['reduce-farming']:
                value['mLotTable'][0]['mCookie'] = 3
        
        if value['mKey'] == 'Arrow' and settings['reduce-farming']:
            value['mLotTable'][0]['mCookie'] = 3
        if value['mKey'] == 'Grass' and settings['reduce-farming']:
            value['mLotTable'][1]['mWeight'] = 18
            value['mLotTable'][2]['mWeight'] = 3
            value['mLotTable'][3]['mWeight'] = 71
        
        if value['mKey'] in SEASHELL_DROPS:
            item_key, item_index = getItemInfo(value['mKey'], placements, item_defs)
            value['mLotTable'][0]['mType'] = item_key
            value['mLotTable'][0]['mCookie'] = item_index


def getItemInfo(key, placements, item_defs):
    check = SEASHELL_DROPS[key]
    item = placements[check]
    item_key = item_defs[item]['item-key']
    item_index = placements['indexes'][check] if check in placements['indexes'] else 1 # mCookie of 1 if not for index

    return item_key, item_index


SEASHELL_DROPS = {
    'Seashell0':    'mabe-bushes',
    'Seashell8':    'plains-rock-maze',
    'Seashell9':    'beside-seashell-mansion',
    'Seashell11':   'southwest-bay-bush',
    'Seashell13':   'tail-cave-bonk-tree',
    'Seashell14':   'ukuku-bonk-tree',
    'Seashell16':   'desert-south',
    'Seashell18':   'pond-island',
    'Seashell19':   'small-coast-island',
    'Seashell20':   'ghost-house-pot',
    'Seashell21':   'taltal-east-bridge',
    'Seashell32':   'north-of-moblin-cave',
    'Seashell33':   'rock-maze',
    'Seashell40':   'taltal-west-rock',
    'Seashell49':   'beach-bonk-tree'
}
