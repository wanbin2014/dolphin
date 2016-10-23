import pkg_resources
from dolphin.mmseg.simple import build_trier

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'



#trier = build_trier("dict/dict.txt")
