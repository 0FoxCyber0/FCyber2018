import os, sys


print ("\033[31;1mmSilahkan Login Dahulu:)")

print ("\033[37;1mGak Tau User Ama Passnya PM 085848812535 Atau 0895335217099 ")

username = 'FOX' 

password = 'CYBER'


def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)


def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")


		if pwd == password:

			print "\n\033[1;34mLogin Succed . Page Akan Dialihkan 1 Second", 

			sys.exit()


		else:

			print "\n\033[1;36mSorry Invalid Password !!!\033[00m"

			print "Back Login\n"

			restart()


	else:

		print "\n\033[1;36mSorry Invalid Username !!!\033[00m"

		print "Back Login\n"

		restart()


try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

