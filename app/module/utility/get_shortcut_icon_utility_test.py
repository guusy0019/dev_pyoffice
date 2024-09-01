import unittest
from app.module.utility.get_shortcut_icon_utility import IconExtractor


class TestIconExtractor(unittest.TestCase):

    def test_extract_icon(self):
        icon_extractor = IconExtractor(icon_size=(64, 64))
        icon = icon_extractor.get_icon(
            icon_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk"
        )
        self.assertIsNotNone(icon)  # アイコンがNoneでないことを確認
