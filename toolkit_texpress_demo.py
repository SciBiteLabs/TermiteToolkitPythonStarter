"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Example script to call TExpress and extract entities from the hits

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '1.0'
__copyright__ = '(c) 2018, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from pprint import pprint
from termite_toolkit import texpress

input_file = "./resources/medline_sample.zip"
username = '' #we will give you this on the hackathon day
password = '' #we will give you this on the hackathon day
termite_home = "https://ugm.scibite.com/termite"
pattern = ':(INDICATION):{0,5}:(GENE)'

# build the request
t = texpress.TexpressRequestBuilder()
t.set_url(termite_home)
t.set_binary_content(input_file)
t.set_input_format('medline.xml')
t.set_subsume(True)
t.set_pattern(pattern)
t.set_basic_auth(username, password, verification=False)

result = t.execute(display_request=True)
entity_hits = texpress.get_entity_hits_from_json(result, score_cutoff=2)

pprint(entity_hits)
