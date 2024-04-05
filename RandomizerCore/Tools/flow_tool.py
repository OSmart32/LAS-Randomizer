from RandomizerCore.Tools import event_tools
import yaml

def readFlow(flowchart, flow: dict, placements: dict, settings: dict):
    entries = list(flow.keys())
    
    for entry in entries:
        entry = str(entry)
        if entry.startswith("entry"):
            event_tools.addEntryPoint(flowchart, entry.split(" ")[1])
