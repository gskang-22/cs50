from pyfiglet import Figlet
import sys

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) != 3:
    sys.exit("Invalid Usage")
elif sys.argv[1] != "-f" or sys.argv[1] != "--font":
    sys.exit("Invalid Usage")

x = input("Input: ")
print(figlet.renderText(x))