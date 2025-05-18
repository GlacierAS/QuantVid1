from manim import ImageMobject
from enumcfg import *


class MRSF():
    @staticmethod
    def _get_sf_char(size, link) -> ImageMobject:
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
    def get_sfbook(size = SSize.S) -> ImageMobject:
        return MRSF._get_sf_char(size, "mrstarfruit/neutral_ready.png")
    @staticmethod
    def get_sfidea(size = SSize.S) -> ImageMobject:
        return MRSF._get_sf_char(size, "mrstarfruit/idea_ready.png")
    @staticmethod
    def get_sflevi(size = SSize.S) -> ImageMobject:
        return MRSF._get_sf_char(size, "mrstarfruit/levi_ready.png")
    @staticmethod
    def get_sfconfused(size = SSize.S) -> ImageMobject:
        return MRSF._get_sf_char(size, "mrstarfruit/confused_ready.png")
    @staticmethod
    def get_sfshoked(size = SSize.S) -> ImageMobject:
        return MRSF._get_sf_char(size, "mrstarfruit/shoked_ready.png")