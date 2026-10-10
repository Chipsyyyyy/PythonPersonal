import pyperclip
import winsound

try:
    pyperclip.copy("")
    print("Clipboard cleared")
    winsound.MessageBeep(winsound.MB_OK)
except Exception as e:
    winsound.MessageBeep(winsound.MB_ICONHAND)