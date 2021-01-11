from telegram.ext import Updater, CommandHandler
from cl.EvalVisitor import EvalVisitor
from cl.script import execute_script

# Guardamos el visitor como parámetro global para no perder la información.
visitor = EvalVisitor()


# Comportamiento del comando /start.
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Who woke up the Hulk ?")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Execute /help so that the Hulk can walk you through the operations")
    context.bot.sendAnimation(chat_id=update.effective_chat.id,
                              animation="https://media.giphy.com/media/prhZjwRxxt5Ys/giphy.gif", duration=None)


# Comportamiento del comando /help.
def Help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="This bot is designed to execute different operations with polygons using these commands:"
                                  "\n/start used to start the bot.\n/create used to create and assign a polygon to a variable."
                                  "\nExample: /create p1 := [0 0  0 1  1 1  0.2 0.8]"
                                  "\n/color used to assign a color to a polygon.\nExample: /color p1, {1 0 0}"
                                  "\n/print used to print the vertices of a polygon.\nExample: /print p1"
                                  "\n/area used to compute the area of a polygon.\nExample: /area p1"
                                  "\n/perimeter used to compute the perimeter of a polygon.\nExample: /perimeter p1"
                                  "\n/vertices used to compute the number of vertices of a polygon.\nExample: /vertices p1"
                                  "\n/centroid used to compute the centroid of a polygon.\nExample: /centroid p1"
                                  "\n/equal used to check whether two polygons are equal or not.\nExample: /equal p1, p2"
                                  "\n/inside used to check if a polygons is inside another polygon.\nExample: /inside p1, p2"
                                  "\n/draw used to draw polygons.\nExample /draw \"image.png\", p1, p2"
                                  "\n/formatPolygon used to see different formats of a polygon.\nExample: /formatPolygon")


# Comportamiento del comando /create.
def assignPolygon(update, context):
    try:
        polygon = update.message.text[8:]
        execute_script(polygon, visitor)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        assignFormat(context, update)
        print(e)


# Comportamiento del comando /color.
def color(update, context):
    try:
        entry = update.message.text[1:]
        execute_script(entry, visitor)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Color assigned successfully")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        colorFormat(context, update)
        print(e)


# Comportamiento del comando /print.
def polygon_print(update, context):
    try:
        entry = update.message.text[1:]
        command = execute_script(entry, visitor)
        if len(command) == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="∅")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=execute_script(entry, visitor))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        printFormat(context, update)
        print(e)


# Comportamiento del comando /area.
def area(update, context):
    try:
        entry = update.message.text[1:]
        command = execute_script(entry, visitor)
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(command))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        areaFormat(context, update)
        print(e)


# Comportamiento del comando /perimeter.
def perimeter(update, context):
    try:
        entry = update.message.text[1:]
        command = execute_script(entry, visitor)
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(command))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        perimeterFormat(context, update)
        print(e)


# Comportamiento del comando /vertices.
def vertices(update, context):
    try:
        entry = update.message.text[1:]
        command = execute_script(entry, visitor)
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(command))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        verticesFormat(context, update)
        print(e)


# Comportamiento del comando /centroid.
def centroid(update, context):
    try:
        entry = update.message.text[1:]
        command = execute_script(entry, visitor)
        if command == ():
            context.bot.send_message(chat_id=update.effective_chat.id, text="∅")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=str(command[0]) + ' ' + str(command[1]))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        centroidFormat(context, update)
        print(e)


# Comportamiento del comando /equal.
def equal(update, context):
    try:
        entry = update.message.text[1:]
        command = execute_script(entry, visitor)
        context.bot.send_message(chat_id=update.effective_chat.id, text=command)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        equalFormat(context, update)
        print(e)


# Comportamiento del comando /inside.
def inside(update, context):
    try:
        entry = update.message.text[1:]
        command = execute_script(entry, visitor)
        context.bot.send_message(chat_id=update.effective_chat.id, text=command)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error in grammar, please try again")
        insideFormat(context, update)
        print(e)


# Comportamiento del comando /draw.
def draw(update, context):
    try:
        entry = update.message.text[1:]
        fileName = execute_script(entry, visitor)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fileName, 'rb'))
    except Exception as e:
        if str(e) is not None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))
            drawFormat(context, update)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Error in grammar, please try again" + str(e))
            drawFormat(context, update)
        print(e)


# Comportamiento del comando /formatPolygon.
def formatPolygon(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="A polygon can be defined in a different ways:\n"
                                                                    "With an ID Example: p1\nWith points Example: [1 1  0 2]\n"
                                                                    "Empty Example: p1 := []\n"
                                                                    "With operations Example: p1 * p2 or #p1 or !12 or p1 + p2 or\n"
                                                                    "[1 1] * p1 or[1 1] + p2 or [1 2  2 1] * [1 1]...\n")


# Método que lanza un mensaje que explica el formato de asignar un polígono a una variable.
def assignFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/create p1 := [0 0  0 1  0.2 0.8] or\n"
                                  "/create p1 := p2 operation p3 or\n/create p1 := p2 operation [0 0  1 0] or\n"
                                  "/create p1 := []\n"
                                  "/create p1 := [1 1  2 2] operation [1 1] or\n/create p1 := #p2 or\n/create p1 := !10\nwhere operations can be +, *, !, #")


# Método que lanza un mensaje que explica el formato de asignar un color a un polígono.
def colorFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id, text="The correct format is:\n/color p1, {1,0,0}")


# Método que lanza un mensaje que explica el formato del print de un polígono o un texto.
def printFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/print p1 or\n/print [1 0  0 0] or\n"
                                  "/print \"text\"")


# Método que lanza un mensaje que explica el formato para calcular el área de un polígono.
def areaFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/area polygon\nRemember to execute /formatPolygon to check the format of a polygon")


# Método que lanza un mensaje que explica el formato para calcular el perímetro de un polígono.
def perimeterFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/perimeter polygon\nRemember to execute /formatPolygon to check the format of a polygon")


# Método que lanza un mensaje que explica el formato para calcular el número de vértices de un polígono.
def verticesFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/vertices polygon\nRemember to execute /formatPolygon to check the format of a polygon")


# Método que lanza un mensaje que explica el formato para calcular el centroid de un polígono.
def centroidFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/centroid polygon\nRemember to execute /formatPolygon to check the format of a polygon")


# Método que lanza un mensaje que explica el formato de como comprobar si dos polígonos son iguales o no.
def equalFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/equal polygon1, polygon2\nRemember to execute /formatPolygon to check the format of a polygon")


# Método que lanza un mensaje que explica el formato de como comprobar si un polígono está dentro de otro polígono.
def insideFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\n/inside polygon1, polygon2\nRemember to execute /formatPolygon to check the format of a polygon")


# Método que lanza un mensaje que explica el formato de como dibujar los polígonos.
def drawFormat(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="The correct format is:\ndraw \"image.png\", polygon1, polygon2, ...\nRemember to execute /formatPolygon to check the format of a polygon")


#  declara una constante con el access token que lee de token.txt
TOKEN = open('token.txt').read().strip()

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(CommandHandler('help', Help))

dispatcher.add_handler(CommandHandler('print', polygon_print))

dispatcher.add_handler(CommandHandler('color', color))

dispatcher.add_handler(CommandHandler('area', area))

dispatcher.add_handler(CommandHandler('perimeter', perimeter))

dispatcher.add_handler(CommandHandler('vertices', vertices))

dispatcher.add_handler(CommandHandler('centroid', centroid))

dispatcher.add_handler(CommandHandler('equal', equal))

dispatcher.add_handler(CommandHandler('inside', inside))

dispatcher.add_handler(CommandHandler('create', assignPolygon))

dispatcher.add_handler(CommandHandler('formatPolygon', formatPolygon))

dispatcher.add_handler(CommandHandler('draw', draw))

# Iniciar el  bot
updater.start_polling()
