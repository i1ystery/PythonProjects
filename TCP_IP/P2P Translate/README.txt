IN ORDER TO INSTALL MY TRANSLATOR U HAVE TO:
1. Install python3 on your Linux machine
2. Download my .deb file and install it
3. Configure translator
4. Run translator daemon

1st step
 1) Make sure you're connected to the internet
 2) In terminal write the following lines:
 	sudo apt install python3
 3) Now you have python3 installed on your Linux OS
2nd step
 1) To download .deb file to your Linux OS write thise line into terminal
 	wget https://www.dropbox.com/s/s85tx01lkv0tqwb/Translate.deb
 2) Now you'll have Translate.deb in your current working directory
 3) To install Translate.deb file you'll have to write this line in terminal
 	sudo dpkg -i Translate.deb
 4) Don't forget to reload daemons. Write this in terminal
 	sudo systemctl daemon-reload
3rd step
 1) In order to change Translate configuration navigate to /usr/local/etc and open cfg.json using this command
  	nano /usr/local/etc/cfg.json
 2) Now you can change configuration
 	{
 	 "IP": "127.0.0.1",		# Server IP
 	 "Port": 65525,		# Port that the server will listen on
 	 "IP_RANGE": "127.0.0.0/24",	# Range of ips, where the other servers will be
 	 "PORT_RANGE": "65525-65535"	# Range of ports, where the other servers will listen on
 	}
 3) Change configuration and save file
4th step
 1) In order to start daemon write this in terminal
 	sudo systemctl start translate
 2) Check if daemon is running
 	sudo systemctl status translate
 3) Congratulations now you have successfully installed and run my Translator.
    Now you can connect to running daemon using Putty or your self-programmed client

# Note
SERVER LOGS ARE SAVED IN:
	/tmp/server_log.txt
TRANSLATABLE WORDS:
	range -> expected translation: rozsah
	car -> expected translation: auto
	hideout -> expected translation: úkryt
	loadout -> expected translation: výbava
	stash -> expected translation: skrýš
AVAILABLE COMMANDS:
	TRANSLATELOC
	TRANSLATEREM
	TRANSLATEANY 
