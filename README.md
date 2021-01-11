# ConvexPolygons

This project consists of a chatbot in Telegram that allows the creation of convex polygons and make different computations with the polygons.
To access the bot via Telegram just search @Anasbot and send him /start.

## Getting Started

Before starting to execute the project 

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

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

