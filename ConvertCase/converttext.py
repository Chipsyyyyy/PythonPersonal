import pyperclip
import winsound
# -- Added button to windows registry

try:
    text = pyperclip.paste().strip()

    if not text:
        winsound.MessageBeep(winsound.MB_ICONHAND)

        raise SystemExit

    if text[0].islower():
        converted = text.upper()
    else:
        converted = text.lower()
        
    pyperclip.copy(converted)
    winsound.MessageBeep(winsound.MB_OK)
except Exception as e:
        winsound.MessageBeep(winsound.MB_ICONHAND)


# def main():
#     text = input("Enter string you want to capitalise: ").strip()
#     for char in text[0]:
#         if char.islower():
#             converttocapital(text)
#         else:
#             converttolowercase(text)
            
# def converttocapital(text):
#     converted = text.upper()
#     copytoclipboard(converted)
    
# def converttolowercase(text):
#     converted = text.lower()
#     copytoclipboard(converted)
    
# def copytoclipboard(converted):
#     pyperclip.copy(converted)
#     print("Text copied to clipboard")

# if __name__ == "__main__":
#     main()
    

