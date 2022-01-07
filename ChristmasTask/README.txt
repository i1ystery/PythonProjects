Project name: Shop Database Application
Author: Maksym Kuzma
Instructions before running application:
1. Open database_export.sql file with Microsoft SQL Server Management Studio
2. In login popup window choose SQL Server Authentication
3. Login with username: sa and password: student
#IMPORTANT remember server name. 
You will need to set it in config file
4. When logged in, application will open database_export.sql file
5. In editor find text USERNAME_HERE and replace it with your username
6. Then find text PASSWORD_HERE and replace it with your password
#IMPORTANT remember username and password that you put there.
7. Finally, execute opened this .sql file by pressing F5 on keyboard then close application
8. Next step is config setup
9. Using notepad open config.json that is located in cfg folder.
10. Change SERVERNAME_HERE to server name that you remembered in Management Studio
11. Change USERNAME_HERE and PASSWORD_HERE to username and password that you input in Management Studio
12. Close and save config.json file.

Instructions for launchings application:
There are 2 ways to launch application:
1) OS Windows
2) OS Linux, MacOS

1. If you're using OS Windows - run Shop.exe that is located in /bin folder


2. If you're using other OS (Linux, MacOS) make sure you have at least Python version 3.9 version installed.
   Now open terminal and run these commands:
      pip install pyodbc
      pip install pandas
   Finally change you terminal directory to Shop/src folder using this command
      cd Shop/src  The
      
