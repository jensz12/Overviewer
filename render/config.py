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
            
def annFilter(poi):
    if poi['id'] == 'Ann':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def sebFilter(poi):
    if poi['id'] == 'Seb':
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
                    'name':'Kjaspers starter hus',
                    'description':'Kjaspers starter hus. Anders bor også her'},
					{'id':'Jens',
                    'x':111,
                    'y':64,
                    'z':21,
                    'name':'Jens starter base',
                    'description':'Jens starter base. Ann bor også her'},
					{'id':'Bisse',
                    'x':172,
                    'y':64,
                    'z':168,
                    'name':'Bisses starter base',
                    'description':'Bisses starter base'},
					{'id':'LeQuest',
                    'x':5,
                    'y':64,
                    'z':-85,
                    'name':'Fyrtårne',
                    'description':'De 4 fyrtårne markere serverens spawn chunks. Tårnene er bygget af Jens'},
					{'id':'Mathias',
                    'x':-203,
                    'y':64,
                    'z':-479,
                    'name':'Mathias base',
                    'description':'Mathias base'},
					{'id':'Jancx',
                    'x':218,
                    'y':64,
                    'z':189,
                    'name':'Jancx base',
                    'description':'Jancx base'},
					{'id':'Jancx',
                    'x':70,
                    'y':64,
                    'z':-40,
                    'name':'S.S Randers',
                    'description':'S.S Randers'},
					{'id':'LeQuest',
                    'x':90,
                    'y':64,
                    'z':0,
                    'name':'LeQuest Træet',
                    'description':'LeQuest Træet. Bygget af TheFred & Kjasper'},
					{'id':'LeQuest',
                    'x':112,
                    'y':64,
                    'z':33,
                    'name':'Nether portalen',
                    'description':'Nether portalen. Bygget af TheFred med meget lidt hjælp fra Jens'},
					{'id':'Astrid',
                    'x':76,
                    'y':64,
                    'z':-6,
                    'name':'Astrids base & kul lager',
                    'description':'Astrids base & kul lager'},
					{'id':'LeQuest',
                    'x':227,
                    'y':64,
                    'z':-678,
                    'name':'Witchfarmen',
                    'description':'Witchfarmen. Bygget af TheFred'},
					{'id':'Kjasper',
                    'x':83,
                    'y':64,
                    'z':-577,
                    'name':'Pers subscribers',
                    'description':'Pers subscribers'},
					{'id':'LeQuest',
                    'x':3217,
                    'y':64,
                    'z':3191,
                    'name':'Mesaen',
                    'description':'Mesaen. Portal øen er bygget af Fred'},
					{'id':'Mathias',
                    'x':526,
                    'y':64,
                    'z':552,
                    'name':'Mathias mob farm',
                    'description':'Mathias mob farm'},
					{'id':'LeQuest',
                    'x':470,
                    'y':64,
                    'z':391,
                    'name':'End portalen',
                    'description':'End portalen'},
					{'id':'LeQuest',
                    'x':260,
                    'y':64,
                    'z':278,
                    'name':'Bomberman spillet',
                    'description':'Bomberman spillet. Bygget af Kjasper'},
					{'id':'Fred',
                    'x':4,
                    'y':64,
                    'z':95,
                    'name':'Freds villager breeder',
                    'description':'Freds villager breeder'},
					{'id':'LeQuest',
                    'x':143,
                    'y':64,
                    'z':226,
                    'name':'Ko breederen',
                    'description':'Ko breederen. Bygget af Kjasper & Jancx'},
					{'id':'LeQuest',
                    'x':721,
                    'y':64,
                    'z':-57,
                    'name':'Horse Island',
                    'description':'Horse Island. Hjemstedet for heste på LeQuest'},
					{'id':'Jancx',
                    'x':79,
                    'y':64,
                    'z':-18,
                    'name':'Jancx start base',
                    'description':'Jancx start base'},
					{'id':'LeQuest',
                    'x':3,
                    'y':64,
                    'z':8,
                    'name':'Kæmpe kiste',
                    'description':'En kæmpe kiste. Bygget af Kjasper'},
					{'id':'Mathias',
                    'x':80,
                    'y':64,
                    'z':0,
                    'name':'Mathias Starter Base',
                    'description':'Mathias starter base.'},
					{'id':'LeQuest',
                    'x':72,
                    'y':64,
                    'z':-29,
                    'name':'Death games / LeQuest games',
                    'description':'Death Games/LeQuest Games. Bygget af Kjasper'},
					{'id':'Spirit',
                    'x':143,
                    'y':64,
                    'z':-71,
                    'name':'Anders hus',
                    'description':'Kjaspers starter hus. Anders bor også her'},
                    {'id':'LeQuest',
                    'x':139,
                    'y':64,
                    'z':0,
                    'name':'Auto fiske farm',
                    'description':'Auto fiske farm. Bygget af Kjasper'},
                    {'id':'LeQuest',
                    'x':83,
                    'y':64,
                    'z':28,
                    'name':'Chicken cooker',
                    'description':'Chicken cookeren'},
                    {'id':'LeQuest',
                    'x':137,
                    'y':64,
                    'z':10,
                    'name':'Snemanden',
                    'description':'LeQuest snefarmen'},
                    {'id':'Ann',
                    'x':288,
                    'y':64,
                    'z':212,
                    'name':'Anns hule',
                    'description':'Anns hule. Her bor hun når hun er sur på Jens'},
                    {'id':'Kjasper',
                    'x':260,
                    'y':64,
                    'z':264,
                    'name':'Kjaspers Villagers',
                    'description':'Kjaspers villager trading'},
                    {'id':'LeQuest',
                    'x':17,
                    'y':64,
                    'z':-864,
                    'name':'End portal',
                    'description':'End portal'},
                    {'id':'Seb',
                    'x':259,
                    'y':64,
                    'z':131,
                    'name':'Sebs base',
                    'description':'Sebs base'},
                    {'id':'LeQuest',
                    'x':4434,
                    'y':64,
                    'z':3201,
                    'name':'Guldminen',
                    'description':'Guldminen. Bygget af Kjasper, Seb & Jens'},
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
				dict(name="LeQuest", filterFunction=lequestFilter, icon="icons/marker_lequest.png"),
                dict(name="Ann", filterFunction=annFilter, icon="icons/marker_ann.png"),
                dict(name="Seb", filterFunction=sebFilter, icon="icons/marker_seb.png")],
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
				dict(name="LeQuest", filterFunction=lequestFilter, icon="icons/marker_lequest.png"),
                dict(name="Ann", filterFunction=annFilter, icon="icons/marker_ann.png"),
                dict(name="Seb", filterFunction=sebFilter, icon="icons/marker_seb.png")],
}
# Overworld nat
renders["lequestnight"] = {
    "world": "LeQuest",
    "title": "Night",
    "rendermode": smooth_night,
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
				dict(name="LeQuest", filterFunction=lequestFilter, icon="icons/marker_lequest.png"),
                dict(name="Ann", filterFunction=annFilter, icon="icons/marker_ann.png"),
                dict(name="Seb", filterFunction=sebFilter, icon="icons/marker_seb.png")],
}
# Nether med Smooth Lightning
renders["lequestnether"] = {
    "world": "LeQuest",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
    'manualpois':[
                   {'id':'LeQuest',
                    'x':571,
                    'y':64,
                    'z':378,
                    'name':'Guldminen',
                    'description':'Portalen til guldminen'},
                    {'id':'LeQuest',
                    'x':339,
                    'y':64,
                    'z':360,
                    'name':'Mesa',
                    'description':'Portalen til mesaen'},
                    {'id':'LeQuest',
                    'x':100,
                    'y':64,
                    'z':8,
                    'name':'End',
                    'description':'Portalen til End'},
                    {'id':'LeQuest',
                    'x':58,
                    'y':64,
                    'z':-40,
                    'name':'Spawn',
                    'description':'Portalen til spawn'},
                    {'id':'LeQuest',
                    'x':99,
                    'y':64,
                    'z':38,
                    'name':'Mob farm',
                    'description':'Portalen til mob farmen'},
                    {'id':'LeQuest',
                    'x':-205,
                    'y':64,
                    'z':24,
                    'name':'Desert',
                    'description':'Portalen til desert'},
                    {'id':'LeQuest',
                    'x':42,
                    'y':64,
                    'z':-24,
                    'name':'Breeder',
                    'description':'Portalen til villager breederen'},
                    {'id':'LeQuest',
                    'x':66,
                    'y':64,
                    'z':-108,
                    'name':'Swamp',
                    'description':'Portalen til swampen'},
                    {'id':'LeQuest',
                    'x':127,
                    'y':64,
                    'z':-45,
                    'name':'Horse Island',
                    'description':'Portalen til Horse Island'},
					],
	'markers':[ dict(name="LeQuest", filterFunction=lequestFilter, icon="icons/marker_lequest.png")],
}
