# This is a sample config file, meant to give you an idea of how to format your
# config file and what's possible.

# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['LeQuest'] = "C:/Users/Jens/Downloads/overviewer/LeQuest"

# Define where to put the output here.
outputdir = "C:/world"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "smooth_lighting"

renders["lequestoverworld"] = {
    "world": "LeQuest",
    "title": "Overworld",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}
renders["lequestcave"] = {
    "world": "LeQuest",
    "title": "Cave",
    "rendermode": cave,
    "dimension": "overworld",
}
renders["lequestnether"] = {
    "world": "LeQuest",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}