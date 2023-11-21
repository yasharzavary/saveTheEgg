
# compition control program

## this project will help you to control one compition

default, this program maded for 'rescue egg' compition! but you can change formulas and shedule to any other compition.
it maded from 4 file, one file for database, one for formulas, one for score show and one file is main that have GUI and some control units that we can use it in our compition.
this project can calulate scores for each player and save it in the data base...it can also show the score board depend on the players score...

* GUI writed by 'tkinter' module of the python.
* I use mysql for database.
* I use function base coding in this project.

## photos of the 'egg rescue' compition

i wanna to show you compiton team and place for this 'rescue egg' compition:
<img src="compPhotos\\compPlace.jpg" alt="compition place" width="1280" height="960">
<img src="compPhotos\\compTeam.jpg" alt="compition team" width="1280" height="960">


## some command for developers

developers must download this modules:
1. mysql connector for python - https://pypi.org/project/mysql-connector-python/
2. tkinter module for GUI.

some hint for files:
1. dataBase file is for data base connect, read, write and other usage...it is writed all in funtction base coding, it added to the main and show score part, you can change this file and use in other files.
2. formulas is for game formulas that have one main function and two support, you can change, add and etc. in this file but notice that don't change calc score function!(last function).
3. showScore file is used for showing scores that you can design it depend one the projector or other conditions...
4. main file is GUI and connector of the files! you must run this file and use this file for control the compition.

Notice: you must run main.py file in the project! all other files is for helping this part.

## some hints for users:
when you use this file in one game you must follow this steps:
1. before starting the game add player info to the database with add it in the new team part!
2. when game start update each player's info with update part, in this part you can see all players and if you click on one of them, you can update it's scores!
NOTICE: program will calc scores when you update one of the player's info.
3. in third part you can see score board that you can use it to see one full-screen score board that show each player's info and scores that gain in the game.


i hope you enjoy the project and it can be heplfull in your game and compitions!
thanks for reading and use it.
