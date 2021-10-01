import pyautogui
import pyperclip
import os
import sys


def resourcePath(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(filename)

def write(str):
    pyperclip.copy(str)
    pyautogui.hotkey("ctrl","v")

def main():
    # .env 読み込みの儀式　→ exe化して、.batで呼び出すようにするので、idとpassが変更できるようにする。
    # load_dotenv(verbose=True)
    # dotenv_path = join(dirname(__file__), '.env')
    # load_dotenv(dotenv_path)

    MEETING_ID = os.environ.get("ZOOM_MEETING_ID")
    MEETING_PASSWORD = os.environ.get("ZOOM_MEETING_PASSWORD")

    # desktopのみの表示
    pyautogui.hotkey("win", "d")

    # zoom起動
    pyautogui.press("win")
    write("zoom")
    pyautogui.sleep(1) # 少しだけまつ
    pyautogui.press("enter")

    pyautogui.sleep(15)
    buttonx, buttony = pyautogui.locateCenterOnScreen('./images/zoom-join-buuton.png', confidence=0.6)
    pyautogui.click(buttonx, buttony)
    
    pyautogui.sleep(15)
    write(MEETING_ID)
    pyautogui.press("enter")

    pyautogui.sleep(15)
    write(MEETING_PASSWORD)
    pyautogui.press("enter")

    pyautogui.sleep(15)
    pyautogui.press("enter")



if __name__ == "__main__":
    main()