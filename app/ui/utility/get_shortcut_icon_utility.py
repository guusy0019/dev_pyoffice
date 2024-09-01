import win32gui
import win32ui
import win32con
import win32api
from PIL import Image


class IconExtractor:
    def __init__(self):
        self.ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
        self.ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    def get_icon(self, icon_path):
        try:
            large, small = win32gui.ExtractIconEx(icon_path, 0)
            if not large:
                raise ValueError(f"アイコンを抽出できませんでした: {icon_path}")

            win32gui.DestroyIcon(small[0])

            hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
            hbmp = win32ui.CreateBitmap()
            hbmp.CreateCompatibleBitmap(hdc, self.ico_x, self.ico_y)
            hdc = hdc.CreateCompatibleDC()

            hdc.SelectObject(hbmp)
            hdc.DrawIcon((0, 0), large[0])

            bmpstr = hbmp.GetBitmapBits(True)
            img = Image.frombuffer(
                "RGBA", (self.ico_x, self.ico_y), bmpstr, "raw", "BGRA", 0, 1
            )

            win32gui.DestroyIcon(large[0])

            return img

        except Exception as e:
            raise RuntimeError(f"アイコンの抽出中にエラーが発生しました: {e}")
