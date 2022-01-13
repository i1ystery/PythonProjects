Project name: Shop Database Application
Author: Maksym Kuzma

Instructions before running application:
1. Application uses school Microsoft SQL Server, so there's no need to change config.json
2. If file config.json does not exist in folder cfg, you should create it.
3. Then you'll have to write this lines into file and save file.
{
 "SERVER": "193.85.203.188",
 "DATABASE": "kuzma",
 "UID": "kuzma",
 "PWD": "asdwsx78"
}

Instructions for launching application:
There are 2 ways to launch application:
1) OS Windows
2) OS Linux, macOS

1. If you're using OS Windows - run Shop.exe that is located in /bin folder and press Enter on keyboard

2. If you're using other OS like Linux or macOS, make sure you have at least Python version 3.9 version installed.
   Now open terminal and run these commands:
      pip install pyodbc
      pip install pandas
   Finally change you terminal directory to Shop/src folder using "cd Shop/src" command and launch python file using "python main.py" command
      
