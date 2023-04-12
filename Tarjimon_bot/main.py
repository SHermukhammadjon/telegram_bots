from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from database import Bot_database
from media import Message_media, CONTEXT
"""
v.3.0.0
"""
def add_user(user_id, lang):
	if RAM_dic.get(user_id):
		RAM_dic[user_id]['lang'] = lang
		RAM_dic[user_id]['edit_count'] += 1
	else:
		RAM_dic[user_id] = {'lang' : lang, 'edit_count' : 0, 'send_name' : 0, 'user_name' : "0"}
API_TOKEN = '6082856375:AAH8nuCVOpIRRnVkaHyXdaSM9TzLiwjlKh0'

RAM_lis = []
RAM_dic = {}

def capital_letter(word):
	word = word.capitalize()
	if len(word) > 3:
		if word[1] == 'h':
			return word[0] + 'H' + word[2:]
	return word


commands = [
	BotCommand(command = "start", description = "Botni ishga tushurish."),
	BotCommand(command = "restart", description = "Botni qayat ishga tushurish."),
	BotCommand(command = "info", description = "Bot statistikasni olish"),
	BotCommand(command = "help", description = "Botni ishlatish bo'ycha yordam")
	]


registir_inbutton = [InlineKeyboardButton(text = "📝 ro'yxatdan o'tish", callback_data = "add_user")]

database = Bot_database("test.db")
database.creat_tables(user_table_name = "users_data", chat_listb_name = "chat", cheet_tb_name = "cheet")

message_media = Message_media()

defolt_lang = "en"


def star(update, context):
	user_id = update.message.chat.id
	print(user_id)
	if database.available_user(user_id):
		pass 
	else:
		if RAM_dic.get(user_id):
			lang = RAM_dic[user_id]['lang']
			update.message.reply_photo(
				photo = open('photos/chose_lang.png', 'rb'),
				caption = CONTEXT['which_lang'][lang],
				reply_markup = InlineKeyboardMarkup([message_media.get_inline_lang(lang = lang)]))

		else:
			RAM_lis.append(user_id)
			update.message.reply_photo(
				photo = open('photos/chose_lang.png', 'rb'),
				caption = f"🇺🇿 Sizga qaysi til qulay?\n🇬🇧 Which language is the best for you?\n🇷🇺 Какой язык вам удобен?",
				reply_markup = InlineKeyboardMarkup([message_media.get_inline_lang(lang = 'en')]))




def lang_mode_hendler(update): 
	message = update.message.text
	if message == "uzn-en mode 🇺🇿-🇬🇧":
		# print("england")
		data_base.set_lang(update, 'en')
		update.message.reply_text("O'zbekcha Inglizcha tartibi yoqildi")
		return True
	elif message == "uzb-ru mode 🇺🇿-🇷🇺":
		# print("russia")
		data_base.set_lang(update, 'ru')
		update.message.reply_text("O'zbekcha Ruscha tartibi yoqildi")
		return True
	return False


def core_function(update, context):
	user_id = update.message.chat.id
	message = update.message.text
	# print(RAM_lis)
	buttons = ["uzb-en mode 🇺🇿🔄🇬🇧", "uzb-ru mode 🇺🇿🔄🇷🇺", "🛡 Oxford Definition", "Aloqa 📲", "⚙️ Sozlamalar"]
	if database.available_user(user_id):
		pass
		
	else:
		#Registir user
		if message in ["📝 Ro'yxatdan o'tish", '📝 Зарегистрироваться', "📝 Sign up"] and RAM_dic.get(user_id):
			user_name = RAM_dic[user_id]['user_name']
			lang = RAM_dic[user_id]['lang']
			buttons = message_media.get_uh_menu(lang = lang)

			database.add_user(int(user_id), user_name, lang)
			head_menu = CONTEXT['head_menu'][lang]
			update.message.reply_text(text = head_menu, 
				reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

		#Ask user name
		elif user_id in RAM_lis:
			if RAM_dic.get(user_id):
				# If user fir send your name
				lang = RAM_dic[user_id]['lang']

				if RAM_dic[user_id]['send_name'] == 0: 
					RAM_dic[user_id]['send_name'] =+ 1
					RAM_dic[user_id]['user_name'] = message
					buttons = message_media.get_regist_button(lang = lang)

					caption = f"{CONTEXT['well_name'][lang][0]} {message} {CONTEXT['well_name'][lang][1]}" # Well name ...
					
					update.message.reply_photo(photo = open('photos/happy_bot.png', 'rb'), 
						caption = caption,
						reply_markup = ReplyKeyboardMarkup([buttons], resize_keyboard = True, one_time_keyboard = True))
					
				
				else:
					# buttons = message_media.get_regist_button(lang = lang)
					RAM_dic[user_id]['user_name'] = message
					reply = CONTEXT['your_name'][lang][0] + message + CONTEXT['your_name'][lang][1] # Your name change ... 
					update.message.reply_text(reply)
				
			else:
				update.message.reply_photo(
				photo = open('photos/chose_lang.png', 'rb'),
				caption = f"🇺🇿 Sizga qaysi til qulay?\n🇬🇧 Which language is the best for you?\n🇷🇺 Какой язык вам удобен?",
				reply_markup = InlineKeyboardMarkup([message_media.get_inline_lang(lang = 'en')]))



def core_inline(update, context):
	user_id = update.callback_query.message.chat.id
	query = update.callback_query
	if user_id in RAM_lis:
		# print(query.data)
		if query.data in ["set_uz", "set_ru", "set_en"]:
			lang = query.data[-2:] #get lang
			add_user(user_id, lang)
			# RAM_dic[user_id] = {'lang' : lang}

			# context.bot.send_message(chat_id = user_id, text = CONTEXT['you_chose_lang'][lang])
			query.message.edit_media(media = InputMediaPhoto(media = open('photos/hello_bot.png', 'rb')))
			query.message.edit_caption(CONTEXT['you_chose_lang'][lang])
			buttons = message_media.get_change_lang_inline(lang = lang)
			query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup([buttons])) 

			if RAM_dic[user_id]['edit_count'] == 0:
				RAM_dic[user_id]['edit_count'] += 1
				query.message.reply_photo(
					photo = open('photos/upset_bot.png', 'rb'),
					caption = CONTEXT['need_sign_up'][lang])
		
		elif query.data == "nouser_change_lang":
			lang = RAM_dic[user_id]['lang']

			buttons = message_media.get_inline_lang(lang = lang)
			query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup([buttons]))

	elif database.available_user(user_id):
		pass

def main():
	updater = Updater(token = API_TOKEN)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', star))
	dispatcher.add_handler(MessageHandler(Filters.text, core_function))
	dispatcher.add_handler(CallbackQueryHandler(core_inline))

	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	main()