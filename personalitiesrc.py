#!/usr/bin/env python2

# Markov chain nick configuration
# 'Personality name':
#   ('IRC nick regex',
#    'Cemetech forum username regex' or None,
#    'Omnimaga forum username regex' or None),
# ...etc....
#
# Regexes must contain at least one parenthesized group!

personality_regexes = {
    'redstone':
        (r'(redstone|asian).*',
         None,
         None),
    'sircmpwn':
        (r'(sircmpwn).*',
         r'(sircmpwn).*',
         r'(sircmpwn).*',),
    'ashbad':
        (r'(ashbad|obongo|aalewis).*',
         r'(ashbad).*',
         r'(ashbad).*',),
    'jonimus':
        (r'(jonimus|thestorm).*',
         r'(TheStorm)',
         r'(TheStorm|JonimusPrime)'),
    'joeyoung':
        (r'(jy|joeyoung|mtgrss111).*',
         r'(JoeYoung)',
         None),
    'comic':
        (r'(comic).*',
         r'(comicIDIOT)',
         None),
    'juju':
        (r'(juju).*',
         r'(juju).*',
         r'(juju).*'),
    'debrouxl':
        (r'(debrouxl|ldebrouxl).*',
         r'(Lionel Debroux)',
         r'(Lionel Debroux)'),
    'bb010g':
        (r'(bb010g).*',
         None,
         None),
    'cvsoftd':
        (r'(CV|notipa).*',
         r'(CVSoft)',
         None),
    'calebh':
        (r'(CalebH|Parse34).*',
         r'(CalebHansberry)',
         None),
    'netham45':
        (r'(netham45|netbot45).*',
         r'(netham45)',
         r'(netham45)'),
    'kevino':
        (r'(.*?kevin_o.*?|dj_omni.*?|dj_o.*?|`-`|celtic3.*?|celticiii.*?|xlibman.*?|omnom|nom|ragol666.*?)',
         r'(dj.omnimaga|dj.o)',
         r'(dj.omnimaga|dj.o)'),
    'brandonw':
        (r'(brandonw)',
         r'(brandonw)',
         r'(brandonw)'),
    'tev':
        (r'(tev).*?',
         r'(travis)',
         r'(travise|travis e|travis e\.)'),
    'merth':
        (r'(merth|merthsoft|shaun).*?',
         r'(merth|merthsoft|shaun).*?',
         r'(merth|merthsoft|shaun).*?'),
    'randomist':
        (r'(randomist|korinidos|.*arch|metalrand|randeimos|damakaru).*?',
         None,
         None),
    'sirlewk':
        (r'(sir_lewk|sirlewk).*?',
         None,
         None),
    'chronomex':
        (r'(chronomex|chronome1|.*?slythe|xmc|cmx|exmic).*?',
         r'(chronomex)',
         r'(chronomex)'),
    'michaelv':
        (r'(michael_v|michaelv).*?',
         None,
         None),
    'ej':
        (r'(e-j|e-jl|el-j).*?',
        None,
        None),
    'cricketb':
        (r'(cricket_b|cricketb|chirp_b|truepika).*?',
         None,
         None),
    'glk':
        (r'(glk).*?',
         None,
         None),
    'kerm':
        (r'(kerm).*?',
         r'(KermMartian)',
         r'(KermMartian)'),
    'nikky':
        (r'(nikky|allyn)(?!(?:bot|test)).*',
         r'(allynfolksjr)',
         None),
}
