import requests
import urllib3
import json
from colorama import init, Fore, Style
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init()

# 200 random usernames
users = [
    'aerationmortar',
    'badgecopperfield',
    'coathangerquisby',
    'mistyoutlying',
    'steamparakeet',
    'subtletykonkeys',
    'distortcona',
    'snorkelkiloparsec',
    'contexttubes',
    'wipeoutfinishing',
    'tallysexy',
    'threefoldloud',
    'appeardelete',
    'saltysaligo',
    'elixirnurturing',
    'junkmantuesday',
    'widthflick',
    'scrollradial',
    'concernchowder',
    'chimpledsailor',
    'boffeerae',
    'shelterespresso',
    'crimdonearshot',
    'millchimps',
    'voucherseminole',
    'gullibleracism',
    'coveylammle',
    'kiteatmosphere',
    'optimisticzabra',
    'unpackboltrope',
    'confusedoriginally',
    'delegatetreat',
    'projectorunhappy',
    'stayforegoing',
    'caliengaged',
    'gostscord',
    'birkdaleacid',
    'ponderelfishly',
    'emblematicascertain',
    'unsignedchuck',
    'pumpedmobal',
    'henhambridgemost',
    'mosedalerejoice',
    'linguistshobby',
    'starlesswhether',
    'bullfinchedrupal',
    'majorfolk',
    'murphylurch',
    'cummerbundlena',
    'theaterjuly',
    'wavecondone',
    'unfiteclipse',
    'plugbyarkansas',
    'channellazy',
    'donordapper',
    'extraneousfog',
    'kleenexandroid',
    'retouchboar',
    'revivalsnoopy',
    'pettinessplage',
    'ruddermower',
    'gritevacuation',
    'coffleunsorted',
    'furiouscasablanca',
    'gynecologyservlet',
    'slingshotslace',
    'celerypark',
    'razslinging',
    'cimarronwest',
    'lathereddefiant',
    'tuitionwiggling',
    'putridblow',
    'bellpizz',
    'packageshredding',
    'twisterundrafted',
    'savorscorecard',
    'studentmap',
    'maxwellprice',
    'bumharmony',
    'cockalorumgazelle',
    'adoptedmusty',
    'rashesgold',
    'joulesidekick',
    'wheeringnightjar',
    'albumvolary',
    'kengemicroscope',
    'lustrouscadillac',
    'garbagenear',
    'rubbingchance',
    'koiledprogram',
    'ashtonalias',
    'dykethieving',
    'pegboardcaviar',
    'pseudomerlyn',
    'shimmeringpostbox',
    'censusfruit',
    'carbondrag',
    'scarywistful',
    'busybodyspur',
    'flangebleep',
    'oldponcho',
    'foyerhefty',
    'warrencurliness',
    'steerforthdizziness',
    'challengeiodine',
    'relightwornout',
    'riverevidence',
    'jarbidgeskating',
    'neuronobedient',
    'dartgoldmedal',
    'serveengland',
    'flashlightwilliam',
    'harmfrustrate',
    'luckdegrading',
    'skulkaxiom',
    'fuzzydreary',
    'chategetaway',
    'elvisminimum',
    'auditoriumegotism',
    'lyingtypical',
    'ruttishgravel',
    'assemblypicassa',
    'partnersesame',
    'staticvacancies',
    'unhiddenmilitary',
    'visorouter',
    'gummyjury',
    'jerkycanopener',
    'cringlefinical',
    'obviousritual',
    'remotedownstairs',
    'effectsquartic',
    'unevensimplify',
    'radfootdisk',
    'safehousefluorine',
    'hybridisland',
    'frothdeeno',
    'familycured',
    'stuporcrest',
    'nicotinebrigadier',
    'rowingaltruistic',
    'copyeel',
    'beginnerend',
    'moneylesspredefine',
    'lowlandmedland',
    'brewertimid',
    'genesauctions',
    'shearflora',
    'shrewdmost',
    'unlovablemachine',
    'concernslugged',
    'umpirestiggling',
    'heftinessannouncer',
    'borummight',
    'sanguinespotting',
    'reggaetweezers',
    'subsetprecision',
    'romapenalty',
    'muppetrequest',
    'yuckyskaters',
    'swillpear',
    'dubniumdivulge',
    'hoffrenewably',
    'eustaticslide',
    'ecologytess',
    'erringtyke',
    'buydates',
    'funeralswin',
    'onstagetacky',
    'frizzyamendable',
    'urbanpatch',
    'managerpanting',
    'shenyangpersecute',
    'monthsrelated',
    'oilyduct',
    'nephewcold',
    'refinishpersevere',
    'crunchyreflective',
    'sartorialpetch',
    'flashbulbdevious',
    'consentpoach',
    'layoutlook',
    'purifywinking',
    'unusedstirring',
    'recallcreed',
    'offjab',
    'itemizerregain',
    'apparelshoveler',
    'gongoozleluckily',
    'skeletalblade',
    'unsureumber',
    'recognizetiming',
    'scamrising',
    'freeganjasper',
    'internationalfeisty',
    'identicalstale',
    'positivesitcom',
    'initialdike',
    'stalestarboard',
    'dwellingjule'
]



for user in users:
	# Adjust URL as appropriate
	url = "https://localhost:44354/users/" + user  + ".json"
	print("Requested URL:" + url)
	response = requests.get(url, verify=False)
	try:
		r = response.json()
	except json.decoder.JSONDecodeError:
		print(Fore.RED + response.text)
		print(Style.RESET_ALL)
	if 'firstName' not in r or 'lastName' not in r:
		print ('')
		continue
	print (f"{r['userName']} {r['firstName']} {r['lastName']}")
