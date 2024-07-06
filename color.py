import ctypes

# 必要な定数や関数の定義
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# モニターのデバイスコンテキスト取得
hdc = user32.GetDC(0)

# モニターの解像度取得
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# 画面全体を反転させる
gdi32.BitBlt(hdc, 0, 0, width, height, hdc, 0, 0, 0x00550009)

# 後処理
user32.ReleaseDC(0, hdc)
import ctypes
import time

def main():
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32

    while True:
        # モニターのデバイスコンテキスト取得
        hdc = user32.GetDC(0)

        # モニターの解像度取得
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)

        # 画面全体を反転させる
        gdi32.BitBlt(hdc, 0, 0, width, height, hdc, 0, 0, 0x00550009)

        # 後処理
        user32.ReleaseDC(0, hdc)

        # 一定時間待機（例えば10秒）
        time.sleep(10)

if __name__ == "__main__":
    main()


