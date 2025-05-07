from manim import ImageMobject
from enumcfg import *


class MRSF():
    @staticmethod
    def _get_sf_char(size, mirror, link) -> ImageMobject:
        if mirror:
            link = link[:-4] + "_F.png"
            
            for i in range(100):
                print(link)
        o = ImageMobject(link)
        match size:
            case SSize.S:
                o.scale(0.12)
            case SSize.M:
                o.scale(0.3)
            case SSize.L:
                o.scale(0.5)
            case SSize.XL:
                o.scale(0.75)
        return o

    @staticmethod
    def get_sfbook(size = SSize.S, mirror = False) -> ImageMobject:
        return MRSF._get_sf_char(size, mirror, "mrstarfruit/neutral_ready.png")
    @staticmethod
    def get_sfidea(size = SSize.S, mirror = False) -> ImageMobject:
        return MRSF._get_sf_char(size, mirror, "mrstarfruit/idea_ready.png")