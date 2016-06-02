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
                    'description':'Freds starter base'},
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
					{'id':'LeQuest',
                    'x':5,
                    'y':64,
                    'z':-85,
                    'name':'Fyr',
                    'description':'De 4 fyrtårne markere serverens spawn chunks. Tårnene er bygget af Jens'},
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
                    'description':'LeQuest Træet. Bygget af TheFred & Kjasper'},
					{'id':'LeQuest',
                    'x':112,
                    'y':64,
                    'z':33,
                    'name':'nether',
                    'description':'Nether portalen. Bygget af TheFred med meget lidt hjælp fra Jens'},
					{'id':'Astrid',
                    'x':76,
                    'y':64,
                    'z':-6,
                    'name':'coalstore',
                    'description':'Astrids kul lager'},
					{'id':'LeQuest',
                    'x':227,
                    'y':64,
                    'z':-678,
                    'name':'witchfarm',
                    'description':'Witchfarmen. Bygget af TheFred'},
					{'id':'Kjasper',
                    'x':83,
                    'y':64,
                    'z':-577,
                    'name':'kjasperpizza',
                    'description':'Pizza'},
					{'id':'LeQuest',
                    'x':3217,
                    'y':64,
                    'z':3191,
                    'name':'mesa',
                    'description':'Mesaen. Portal øen er bygget af Fred'},
					{'id':'Mathias',
                    'x':526,
                    'y':64,
                    'z':552,
                    'name':'mathiasmob',
                    'description':'Mathias mob farm'},
					{'id':'LeQuest',
                    'x':470,
                    'y':64,
                    'z':391,
                    'name':'end',
                    'description':'End portalen'},
					{'id':'LeQuest',
                    'x':260,
                    'y':64,
                    'z':278,
                    'name':'bomberman',
                    'description':'Bomberman spillet. Bygget af Kjasper'},
					{'id':'Fred',
                    'x':4,
                    'y':64,
                    'z':95,
                    'name':'fredvillager',
                    'description':'Freds villager breeder'},
					{'id':'LeQuest',
                    'x':143,
                    'y':64,
                    'z':226,
                    'name':'cows',
                    'description':'Ko breederen. Bygget af ?'},
					{'id':'LeQuest',
                    'x':721,
                    'y':64,
                    'z':-57,
                    'name':'horse',
                    'description':'Horse Island. Hjemstedet for heste på LeQuest'},
					{'id':'Jancx',
                    'x':79,
                    'y':64,
                    'z':-18,
                    'name':'jancxstar',
                    'description':'Jancx start base'},
					{'id':'LeQuest',
                    'x':3,
                    'y':64,
                    'z':8,
                    'name':'kiste',
                    'description':'En kæmpe kiste. Bygget af ?'},
					{'id':'Mathias',
                    'x':80,
                    'y':64,
                    'z':0,
                    'name':'mathiasstart',
                    'description':'Mathias starter base.'},
					{'id':'LeQuest',
                    'x':72,
                    'y':64,
                    'z':-29,
                    'name':'deathgames',
                    'description':'Death Games/LeQuest Games. Bygget af Kjasper'},
					{'id':'Spirit',
                    'x':143,
                    'y':64,
                    'z':-71,
                    'name':'andershus',
                    'description':'Kjaspers starter hus. Anders bor også her'},
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
# Nether med Smooth Lightning
renders["lequestnether"] = {
    "world": "LeQuest",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
