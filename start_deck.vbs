Set objShell = CreateObject("Wscript.Shell")
' Set the working directory so Flask can find your HTML and CSS
objShell.CurrentDirectory = "C:\Users\YOUR_OWN_USER\Remote-deck"
' Run Python in windowless mode (pythonw.exe)
objShell.Run """C:\Program Files\Python311\pythonw.exe"" app.py", 0, False
