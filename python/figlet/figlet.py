from pyfiglet import Figlet
import sys

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) != 3:
    sys.exit("Invalid Usage 1")
elif sys.argv[1].strip() != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid Usage 2")

f = sys.argv[2]
if f not in list:
    sys.exit("Invalid Usage 3")
else:
    figlet.setFont(font=f)

x = input("Input: ")
print(figlet.renderText(x))