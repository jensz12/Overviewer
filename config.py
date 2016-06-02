# Define the path to your world here. 'LeQuest' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['LeQuest'] = "C:/Users/Jens/Downloads/overviewer/LeQuest"

# Define where to put the output.
outputdir = "C:/world"

# Overworld med Smooth Lightning!
renders["lequestoverworld"] = {
    "world": "LeQuest",
    "title": "Overworld",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}
# Overworld caves
renders["lequestcave"] = {
    "world": "LeQuest",
    "title": "Cave",
    "rendermode": cave,
    "dimension": "overworld",
}
# Nether med Smooth Lightning
renders["lequestnether"] = {
    "world": "LeQuest",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
