# -*- coding: utf-8 -*-
def astridFilter(poi):
    if poi['id'] == 'Astrid':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def bisseFilter(poi):
    if poi['id'] == 'Bisse':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def fredFilter(poi):
    if poi['id'] == 'Fred':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def jancxFilter(poi):
    if poi['id'] == 'Jancx':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def jensFilter(poi):
    if poi['id'] == 'Jens':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def kjasperFilter(poi):
    if poi['id'] == 'Kjasper':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def mathiasFilter(poi):
    if poi['id'] == 'Mathias':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'
			
def spiritFilter(poi):
    if poi['id'] == 'Spirit':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def lequestFilter(poi):
    if poi['id'] == 'LeQuest':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

# Define the path to your world here. 'LeQuest' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['LeQuest'] = "C:/Users/Jens/Downloads/overviewer/LeQuest"

# Define where to put the output.
outputdir = "C:/world"

# Overworld med Smooth Lightning
renders["lequestoverworld"] = {
    "world": "LeQuest",
    "title": "Overworld",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
	'manualpois':[
                   {'id':'Astrid',
                    'x':117,
                    'y':64,
                    'z':60,
                    'name':'Luftballonen',
                    'description':'Astrids luftballon'},
                   {'id':'Fred',
                    'x':145,
                    'y':64,
                    'z':56,
                    'name':'Freds base',
                    'description':'Freds base'},
					{'id':'Kjasper',
                    'x':148,
                    'y':64,
                    'z':-64,
                    'name':'StarterBase',
                    'description':'Kjaspers starter hus. Anders bor også her'},
					{'id':'Jens',
                    'x':111,
                    'y':64,
                    'z':21,
                    'name':'StarterBase',
                    'description':'Jens starter base'},
					{'id':'Bisse',
                    'x':172,
                    'y':64,
                    'z':168,
                    'name':'StarterBase',
                    'description':'Bisses starter base'},
					{'id':'Jens',
                    'x':5,
                    'y':64,
                    'z':-85,
                    'name':'Fyr',
                    'description':'De 4 fyrtårne markere serverens spawn chunks'},
					{'id':'Mathias',
                    'x':-203,
                    'y':64,
                    'z':-479,
                    'name':'mathiasbase',
                    'description':'Mathias base'},
					{'id':'Jancx',
                    'x':218,
                    'y':64,
                    'z':189,
                    'name':'jancxbase',
                    'description':'Jancx base'},
					{'id':'Jancx',
                    'x':70,
                    'y':64,
                    'z':-40,
                    'name':'jancxranders',
                    'description':'S.S Randers'},
					{'id':'LeQuest',
                    'x':90,
                    'y':64,
                    'z':0,
                    'name':'questree',
                    'description':'LeQuest Træet'},
					],
	'markers':[ 
				dict(name="Astrid", filterFunction=astridFilter, icon="icons/marker_astrid.png"),
				dict(name="Bisse", filterFunction=bisseFilter, icon="icons/marker_bisse.png"),
				dict(name="Fred", filterFunction=fredFilter, icon="icons/marker_fred.png"),
				dict(name="Jancx", filterFunction=jancxFilter, icon="icons/marker_jancx.png"),
				dict(name="Jens", filterFunction=jensFilter, icon="icons/marker_jens.png"),
				dict(name="Kjasper", filterFunction=kjasperFilter, icon="icons/marker_kjasper.png"),
				dict(name="Mathias", filterFunction=mathiasFilter, icon="icons/marker_mathias.png"),
				dict(name="Spirit", filterFunction=spiritFilter, icon="icons/marker_spirit.png"),
				dict(name="LeQuest", filterFunction=lequestFilter, icon="icons/marker_lequest.png")],
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
