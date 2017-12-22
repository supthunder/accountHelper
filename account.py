import json
from termcolor import cprint
import pyperclip
from pyfiglet import Figlet

# def addToClipBoard(text):
#     command = 'echo ' + text.strip() + '| clip'
#     os.system(command)

def create(account):
	print(account)

def load(account):
	cprint("\nAccount loaded and ready, press enter to keep loading!","green")

	end = False
	count = 0
	while not end:
		try:
			count += 1
			currentAccount = account[str(count)]
			cprint("\nID: {} loaded\n".format(str(count)),"yellow")


			x = input("Press enter to copy name to clipboard")
			cprint("{}\n".format(currentAccount['name']),"green")
			pyperclip.copy(currentAccount['name'])
			spam = pyperclip.paste()


			x = input("Press enter to copy address to clipboard")
			cprint("{}\n".format(currentAccount['address']),"green")
			pyperclip.copy(currentAccount['address'])
			spam = pyperclip.paste()


			x = input("Press enter to copy card to clipboard")
			cprint("{} - {} - {}\n".format(currentAccount['card'],currentAccount['cvv'],currentAccount['date']),"green")
			pyperclip.copy(currentAccount['card'])
			spam = pyperclip.paste()

			x = input("Press enter to copy card to clipboard")
			cprint("{} - {} - {}\n".format(currentAccount['card'],currentAccount['cvv'],currentAccount['date']),"green")
			pyperclip.copy(currentAccount['cvv'])
			spam = pyperclip.paste()

			currentAccount['used'] = True
		except:
			cprint("REACHED END!","red",attrs=['bold'])
			end = True
	return account

def main():
	with open("account.json") as f:
		masterAccount = json.load(f)

	#create copy just incase
	with open("account_original.json","w") as outfile:
		json.dump(masterAccount, outfile, indent=4, sort_keys=True)


	# cprint('''|        /account loader/       |''',"red",'on_yellow',attrs=['bold'])

	f = Figlet()
	cprint(f.renderText('| account loader | '),"red",attrs=['bold'])

	name = input("Enter name: ")
	account = masterAccount[name]
 
	cr = input("1 - create\n2- load\n choose one: ")

	if cr == "1":
		create(account)
	elif cr == "2":
		account = load(account)
	masterAccount[name] = account

	with open("account.json","w") as outfile:
		json.dump(masterAccount, outfile, indent=4, sort_keys=True)


if __name__ == '__main__':
	main()
