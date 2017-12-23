import json
from termcolor import cprint
import pyperclip
from pyfiglet import Figlet

# def addToClipBoard(text):
#     command = 'echo ' + text.strip() + '| clip'
#     os.system(command)

def create(account):
	x = input("Add to existing accounts? (y/n) ")
	if x == "y":
		try:
			lastId = int(account['lastId']) + 1
			cprint("{} accounts already loaded!\n".format(account['lastId']),"blue")
		except:
			cprint("No accounts in json","red")
			lastId = 1
	else:
		lastId = 1

	end = False
	while not end:
		tempDict = {}
		tempDict['name'] = input("Enter name (first last): ")
		tempDict['address'] = input("Enter address (123 main st): ")
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
	except:
		cprint("No {} found, creating new user {}".format(name,name),"yellow")
		account = {}
 
	cr = input("1 - create\n2 - load\nchoose one: ")

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
