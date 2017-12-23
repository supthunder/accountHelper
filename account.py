import json
from termcolor import cprint
import pyperclip
from pyfiglet import Figlet

# def addToClipBoard(text):
#     command = 'echo ' + text.strip() + '| clip'
#     os.system(command)

def create(account):
	try:
		lastId = int(account['lastId']) + 1
		cprint("{} accounts already loaded!\n".format(account['lastId']),"blue")
	except:
		lastId = 1

	end = False
	while not end:
		tempDict = {}
		tempDict['first'] = input("Enter first name (first): ")
		tempDict['last'] = input("Enter last name (last): ")
		tempDict['address'] = input("Enter address (123 main st): ")
		tempDict['city'] = input("Enter city (dc): ")
		tempDict['zip'] = input("Enter zip (12345): ")
		tempDict['phone'] = input("Enter phone (1231231234): ")
		tempDict['email'] = input("Enter address (som@some.com): ")
		tempDict['card'] = input("Enter credit card (1234123412341234): ")
		tempDict['cvv'] = input("Enter cvv (123): ")
		tempDict['date'] = input("Enter exp date (11/11): ")
		tempDict['used'] = False
		tempDict['orderNum'] = ""
		account[str(lastId)] = tempDict
		x = input("Done? (y/n) ")

		if x == "y":
			account['lastId'] = str(lastId)
			end = True
		else:
			lastId += 1
			print("\n")
	return account


def load(account):
	cprint("\nAccount loaded and ready, press enter to keep loading!","green")

	end = False
	count = 0
	while not end:
		try:
			count += 1
			currentAccount = account[str(count)]
			cprint("\nID: {} loaded\n".format(str(count)),"yellow")


			x = input("Press enter to copy first name to clipboard")
			cprint("{}\n".format(currentAccount['first']),"green")
			pyperclip.copy(currentAccount['first'])
			spam = pyperclip.paste()

			x = input("Press enter to copy last name to clipboard")
			cprint("{}\n".format(currentAccount['last']),"green")
			pyperclip.copy(currentAccount['last'])
			spam = pyperclip.paste()

			x = input("Press enter to copy address to clipboard")
			cprint("{}\n".format(currentAccount['address']),"green")
			pyperclip.copy(currentAccount['address'])
			spam = pyperclip.paste()

			x = input("Press enter to copy city to clipboard")
			cprint("{}\n".format(currentAccount['city']),"green")
			pyperclip.copy(currentAccount['city'])
			spam = pyperclip.paste()

			x = input("Press enter to copy zip to clipboard")
			cprint("{}\n".format(currentAccount['zip']),"green")
			pyperclip.copy(currentAccount['zip'])
			spam = pyperclip.paste()

			x = input("Press enter to copy phone to clipboard")
			cprint("{}\n".format(currentAccount['phone']),"green")
			pyperclip.copy(currentAccount['phone'])
			spam = pyperclip.paste()

			x = input("Press enter to copy email to clipboard")
			cprint("{}\n".format(currentAccount['email']),"green")
			pyperclip.copy(currentAccount['email'])
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

			order = input("Enter order num: (or press enter) ")
			currentAccount['orderNum'] = order
		except:
			cprint("REACHED END!","red",attrs=['bold'])
			end = True
	return account

def main():
	with open("account.json") as f:
		masterAccount = json.load(f)

	#create copy of previous state just incase
	with open("account_original.json","w") as outfile:
		json.dump(masterAccount, outfile, indent=4, sort_keys=True)


	# cprint('''|        /account loader/       |''',"red",'on_yellow',attrs=['bold'])

	f = Figlet()
	cprint(f.renderText('| account loader | '),"red",attrs=['bold'])
	# print(f.renderText('| account loader | '))

	cprint("User list: ","blue")
	for names in masterAccount.keys():
		cprint("{}".format(names),"yellow")

	name = input("\nEnter exisiting user or create a new one: ")
	try: 
		account = masterAccount[name]
		cr = input("1 - create\n2 - load\nchoose one: ")
	except:
		cprint("No {} found, creating new user {}".format(name,name),"yellow")
		account = {}
		cr = "1"

	if cr == "1":
		account = create(account)
	elif cr == "2":
		account = load(account)

	masterAccount[name] = account

	cprint("\nUpdated json","green")
	with open("account.json","w") as outfile:
		json.dump(masterAccount, outfile, indent=4, sort_keys=True)


if __name__ == '__main__':
	main()
