from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

#Telegram Token not specidfied
task = []

#List Codes
def download():
    # 'C:\Users\yeshi\Dropbox\Polito\Third Year\Second Semester\Ambient Intelligence\Python Labs\course-materials\Lab2'
    Updater.message.reply_text('Input file name:')
    path = Updater.message.text
    file = open(path, 'r')
    task.extend(file.readlines())
    file.close()

def upload():
    Updater.message.reply_text('Enter the name of the output file:')
    path = Updater.message.text
    file = open(path, 'w')
    if len(task) == 0:
        print('List is empty!')
    else:
        for i in task:
            file.write(i)
    file.close()

def intial():
    Updater.message.reply_text('1. Show all the existing tasks?')
    Updater.message.reply_text('2. Insert a new task:')
    Updater.message.reply_text('3. Which tasks to remove from the existing tasks?')
    Updater.message.reply_text('4. The program eliminates the a substring:')
    Updater.message.reply_text('Please enter a number between:')

def new_task():
    Updater.message.reply_text('Name of task to be added:')
    item = Updater.message.text
    task.append(item)

def remove_task():
    Updater.message.reply_text('Name the substring to be removed:')
    item = Updater.message.text
    task_to_remove = []
    for i in task:
        if item in i:
            task_to_remove.append(i)

    for g in task_to_remove:
        if g in task:
            task.remove(g)

def show():
    if len(task) != 0:
        for g in task:
            Updater.message.reply_text(g)
    else:
        Updater.message.reply_text('The list is empty!')


#Telebot Codes
def start(bot, update):
    Updater.message.reply_text("Processing!")

def reply(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    Updater.message.reply_text('Welcome to Todo Manager:')
    repeat_text = update.message.text
    download()



    #Put the right answer
    #Updater.message.reply_text()

def main():
    updater = Updater("573598791:AAF6kiGBOCp5Pc7cMsc1273bKVtjXT5R8sU")
    pong = updater.dispatcher
    pong.add_handler(CommandHandler("start",start))
    pong.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle


if __name__ == "__main__":
    while True:
        main()
        x = Updater.message.text
        if x == '/showTasks':
            show()
            Updater.message.reply_text('Please enter a number:')
        elif x == '/newTasks':
            new_task()
            Updater.message.reply_text('Please enter a number:')
        elif x == '/removeTasks':
            remove_task()
            Updater.message.reply_text('Please enter a number:')
        elif x == '/removeAllTasks':
            Updater.message.reply_text('The program will terminate now')
            upload()
            break
        else:
            Updater.message.reply_text('Please enter a commend from the list:')
