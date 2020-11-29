import winreg as wreg

def create_reg(name, path, message):
    key = wreg.CreateKey(wreg.HKEY_CLASSES_ROOT, "*\\shell\\" + name)
    wreg.SetValue(key, 'command', wreg.REG_SZ, ("\"{}\", \"%1\"".format(path)))
    wreg.SetValueEx(key, '', 0, wreg.REG_SZ, message)
    wreg.SetValueEx(key, 'Icon', 0, wreg.REG_SZ, "\"{}\"".format(path))
    key.Close()
    
if __name__ == '__main__':
    name = input("Name for reg folder: ")
    path = input("path: ")
    message = input("What message should appear? ")
    
    create_reg(name, path, message)
    
    print("Created; You should see the changes when you restart your pc.")
    input("\nEnter to exit")

