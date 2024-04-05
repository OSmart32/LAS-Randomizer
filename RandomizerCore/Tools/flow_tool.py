from RandomizerCore.Tools import event_tools


def readFlow(flowchart, flow: dict, placements: dict, settings: dict):
    entries = list(flow.keys())
    entries = [str(e) for e in entries]

    for entry in entries:
        if isinstance(flow[entry], list):
            createEvents(flowchart, entry, flow[entry], placements, settings)
        else:
            if entry == "Actors":
                addActors()
                continue
            if entry == "Connect":
                for k,v in flow[entry].items():
                    connectEvents(flowchart, v, settings)
            editEvent()


def addActors():
    pass


def createEvents(flowchart, entry: str, events: list, placements: dict, settings: dict):
    if entry.startswith("entry"):
        event_tools.addEntryPoint(flowchart, entry.split(" ")[1])


def connectEvents(flowchart, events: list, settings: dict):
    first = events.pop(0)
    for ev in events:
        # parse any conditionals here
        event_tools.insertEventAfter(flowchart, first, ev)
        first = ev
    


def editEvent(flowchart, event, edits: dict):
    event = event_tools.findEvent(event)
