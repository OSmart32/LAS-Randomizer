from RandomizerCore.Tools import event_tools


def readFlow(flowchart, flow: dict, placements: dict, settings: dict):
    entries = list(flow.keys())
    entries = [str(e) for e in entries]

    for entry in entries:
        if isinstance(flow[entry], list):
            createEvents(flowchart, entry, flow[entry], placements, settings)
        else:
            if entry == "Actors":
                for k,v in flow[entry].items():
                    addActor(flowchart, k, v)
            if entry == "Connect":
                for k,v in flow[entry].items():
                    connectEvents(flowchart, v, settings)
            editEvent()


def addActor(flowchart, actor, actor_data):
    pass


def createEvents(flowchart, entry: str, events: list, placements: dict, settings: dict):
    first = None
    if entry.startswith("entry"):
        first = entry.split(" ")[1]
        event_tools.addEntryPoint(flowchart, first)
    
    if not first:
        first = events.pop(0)
    
    for ev in events:
        # parse any conditionals here - should be separate function
        pass


def connectEvents(flowchart, events: list, settings: dict):
    first = None
    for ev in events:
        if isinstance(ev, dict): # must be checking settings
            set_key = ev.split("[")[1].split("]")[0]
            false_evs = ev["0"]
            true_evs = ev["1"]
            if settings[set_key]:
                connectEvents(flowchart, true_evs, settings)
            else:
                connectEvents(flowchart, false_evs, settings)
        else:
            if first is not None:
                event_tools.insertEventAfter(flowchart, first, ev)
        first = ev
    


def editEvent(flowchart, event, edits: dict):
    event = event_tools.findEvent(event)
