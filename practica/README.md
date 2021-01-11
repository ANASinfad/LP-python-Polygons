# ConvexPolygons

This project consists of a chatbot in Telegram that allows the creation of convex polygons and make different computations with the polygons such as:
* Intersection of convex polygons
* Union of convex polygons
* Bounding Box of convex polygons
* Check if a polygon is inside other
* Check wether two polygons are equal
* Draw polygons
* Compute the centroid of convex polygons
* Compute the number of vertices of a polygon

To access the bot via Telegram just search @Anasbot and send him /start.

## Getting Started

Before starting to execute the project 

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The things you need to install the software and how to install them

* install Python 3:

	* [Python 3](https://www.python.org)

* Other requirements:

pip3 install -r requirements.txt (or pip)

Once the above requirements have been installed, all that remains is to install the ANTLR4 to be used in the compiler part.

* Download the ANTLR4.jar file:

	* [jar file](https://www.antlr.org/download/antlr-4.8-complete.jar)
	* [Getting started](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

* Install Python runtime:

			* pip3 install antlr4-python3-runtime or
			* pip install antlr4-python3-runtime

* Install Telegram Bot :
			* pip3 install python-telegram-bot


# Running
In the main folder you will find the following files:

* polygons.py
* token.txt (a file that stores the token corresponding to the bot)
* requirement.txt (a file that contains the used libraries)
* cl (a folder that contains the compilers part)
	* ConvexPolygons.g(Grammar)
	* script.py (Script to interact with the visitor)
	* EvalVisitor.py (class used to travel the trees generated from the grammar. This class inherits from ConvexPolygonVisitor)
* bot ( a folder that contains the bot part)
	* bot.py ( Code of the Telegram bot)

In the first part of the project, we had to implement the class polygons.py such that it contains all the operations needed so the user can make computations with polygons and manage them.
To compile this class, simply use the command:
python polygons.py

In the second part of the project, the compiler part had to be implemented to interpret the language defined in the statement. A grammar has been created for this language so that a polygons in AST format can be passed to an instance of the polygons class.
In order to compile and execute this. the following command must be writen in the console:
antlr4 -Dlanguage=Python3 -no-listener -visitor ConvexPolygon.g

In the third part of the project, the bot part had to be implemented to manage the communication between the bot and a user.
To run the but execute the command:
python bot.py

# Functioning

The bot is quite simple to use, and it is possible to use all the commands described in the statement of the [project](https://github.com/jordi-petit/lp-polimomis-2020).
You can always use the command /help to see the operations that bot can do.
The bot can interact with different users at the same time, each user with their own polygons thanks to the context.user_data.

# Built With
* [Python](https://docs.python.org/3/) - language used
* [Telegram](https://core.telegram.org/bots) - For the bot
* [pillow](https://lliçons.jutge.org/grafics/) - To draw the polygons
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - IDE used
* [ANTLR4](https://www.antlr.org) - Used for the grammar

# Author
* Anas Infad


