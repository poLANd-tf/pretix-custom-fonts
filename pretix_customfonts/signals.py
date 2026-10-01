import functools
import json
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from pretix.plugins.ticketoutputpdf.signals import register_fonts


@receiver(register_fonts, dispatch_uid="fontpack_custom_fonts")
def fontpack_custom(sender, **kwargs):
    basepath = 'pretix_customfonts'
    return {
        "Britanica Black": {
            "pdf_only": false,
            "regular": {
                "truetype": basepath + "/Britanica-Black.ttf",
                "woff": basepath + "/Britanica-Black.woff",
                "woff2": basepath + "/Britanica-Black.woff2",
            },
            "bold": {
                "truetype": basepath + "/Britanica-Black.ttf",
                "woff": basepath + "/Britanica-Black.woff",
                "woff2": basepath + "/Britanica-Black.woff2",
            },
            "italic": {
                "truetype": basepath + "/Britanica-Black.ttf",
                "woff": basepath + "/Britanica-Black.woff",
                "woff2": basepath + "/Britanica-Black.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/Britanica-Black.ttf",
                "woff": basepath + "/Britanica-Black.woff",
                "woff2": basepath + "/Britanica-Black.woff2",
            },
        },
        "Gabarito": {
            "pdf_only": false,
            "regular": {
                "truetype": basepath + "/Gabarito-Regular.ttf",
                "woff": basepath + "/Gabarito-Regular.woff",
                "woff2": basepath + "/Gabarito-Regular.woff2",
            },
            "bold": {
                "truetype": basepath + "/Gabarito-Bold.ttf",
                "woff": basepath + "/Gabarito-Bold.woff",
                "woff2": basepath + "/Gabarito-Bold.woff2",
            },
            "italic": {
                "truetype": basepath + "/Gabarito-Medium.ttf",
                "woff": basepath + "/Gabarito-Medium.woff",
                "woff2": basepath + "/Gabarito-Medium.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/Gabarito-SemiBold.ttf",
                "woff": basepath + "/Gabarito-SemiBold.woff",
                "woff2": basepath + "/Gabarito-SemiBold.woff2",
            },
        },
        "Gabarito Black": {
            "pdf_only": false,
            "regular": {
                "truetype": basepath + "/Gabarito-Black.ttf",
                "woff": basepath + "/Gabarito-Black.woff",
                "woff2": basepath + "/Gabarito-Black.woff2",
            },
            "bold": {
                "truetype": basepath + "/Gabarito-Black.ttf",
                "woff": basepath + "/Gabarito-Black.woff",
                "woff2": basepath + "/Gabarito-Black.woff2",
            },
            "italic": {
                "truetype": basepath + "/Gabarito-ExtraBold.ttf",
                "woff": basepath + "/Gabarito-ExtraBold.woff",
                "woff2": basepath + "/Gabarito-ExtraBold.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/Gabarito-ExtraBold.ttf",
                "woff": basepath + "/Gabarito-ExtraBold.woff",
                "woff2": basepath + "/Gabarito-ExtraBold.woff2",
            },
        },
    }
