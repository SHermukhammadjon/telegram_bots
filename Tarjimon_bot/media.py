from telegram import KeyboardButton, BotCommand, InlineKeyboardButton

CONTEXT = {'you_chose_lang': 
			{
			'uz' : 'Siz o\'zbek tilini tanladingiz !',
			'en' : 'You have selected English !',
			'ru' : 'Вы выбрали русский язык !'
			},

		'hello_my_name' : 
			{
			'uz' : 'Assalomu alykum Men TarjimonRobotman!',
			'ru' : 'Здравствуйте, я TarjimonRobot!',
			'en' : "Hello, I'm TranslatorRobot!"
			},

		'which_lang' : 
			{
			'uz' : 'Qaysi til sizga qulay?',
			'en' : 'Which language is the best for you?',
			'ru' : 'Какой язык вам удобен?'
			},
		'need_sign_up' : 
			{
				'uz' : "Afsus siz ro'yxatdan o'tmagansiz! Iltimos, ro'yxatdan o'tish uchun ismigizni Jo'nating",
				'en' : "Sorry you are not registered! Please, Send your name to register",
				'ru' : "Извините, вы не зарегистрированы! Пожалуйста, укажите свое имя, чтобы зарегистрироваться"
			},
		'well_name' : 
			{
				'uz' : ["Yaxshi ", "! Agar ismingizni xato kiritgan bo'lsangiz qaytadan ismingizni jo'natishingiz mumkun!"],
				'en' : ["Good ", "! If you entered your name incorrectly, you may send your name again!"],
				'ru' : ["Добрый",  " ! Если вы ввели свое имя неправильно, вы можете отправить свое имя еще раз!"]
			},
		'your_name' : 
			{
				'uz' : ["Sizning ismingiz ", "ga o'zgartirildi!"],
				'en' : ["Your name has been changed to ", "!"],
				'ru' : ["Ваше имя изменено на ", "!"]
			},
		'head_menu' : 
      		{
            'uz' : 'Bosh menu', 
            'ru' : 'Главное меню', 
            'en' : 'Head menu'
            },
		'you_have_registred' : 
    		{
        	'uz' : "Siz muvaffaqiyatli ro'yxatdan o'tdingiz!",
            'ru' : "Вы успешно зарегистрировались!",
            'en' : "You have successfully registered!"
            },
		"you_touch_start" : 
			# Name
    		{
				'uz' : ["Assalomu alykum  ","! Sizi ko'rib turganimdan xursandman."],
				'ru' : ["Привет ", "! Я рад тебя видеть."],
				'en' : ["Hi ", "! I'm glad to see you."]
			},
		"uzen-mode" :
			{
				'uz' : "O'zbekcha Inglizcha tartibi yoqildi.",
				'en' : "Uzbek English mode is enabled.",
				'ru' : "Режим узбекского английского включен."
			},
		"enuz-mode":
			{
				'uz' : "Inglizcha O'zbekcha tartibi yoqildi.",
				'en' : "English Uzbek mode is enabled.",
				'ru' : "Режим английского узбекского включен."
			},
		"uz-en_menu":
			{
				'uz' : "Siz inglizcha o'zbekcha tarjimon menyusidasiz!",
				'en' : "You are in the English-Uzbek translator menu!",
				'ru' : "Вы находитесь в меню англо-узбекского переводчика!"
			},
		"uz-ru_menu":
			{
				'uz' : "Siz Ruscha o'zbekcha tarjimon menyusidasiz!",
				'en' : "You are in the Russian-Uzbek translator menu!",
				'ru' : "Вы в меню русско-узбекского переводчика!"
			},
		"uzru-mode":
			{
				'uz' : "O'zbekchadan Ruschaga tartibi yoqildi.",
				'en' : "The order from Uzbek to Russian is enabled.",
				'ru' : "Порядок с узбекского на русский включен."
			},
		"ruuz-mode":
			{
				'uz' : "Ruschadan O'zbekchaga tartibi yoqildi.",
				'en' : "You are in the Russian to Uzbek translator menu!",
				'ru' : "Порядок с русского на узбекский включен."
			},
		"statistka" : 
    		{
          	'uz' : "📈 statistika", 
       		'ru' : "📈 статистика", 
         	'en' : "📈 statistics"
          	},
		"info" : 
		{
			'uz' : "🤖📂 malumot", 
			'en' : "🤖📂 info", 
			'ru' : "🤖📂 информация"
		},

		'contact_menu' : 
			{'uz' : "📡 Aloqa menyusi:",
			'ru' : "📡 Меню контактов:",
			'en' : "📡 Contact menu:"},

		"admin_contact" : 
			{
				'uz' : "admin bilan aloqa menyusi:",
				'en' : "admin contact menu:",
				'ru' : "меню контактов администратора:"
			},
        "contact_with_admin" :
        	{
        		'uz' : " Adminga shikoyat va takliflaringizni yozishingiz mumkun. Admin sizga tez orada javob beradi",
        		'ru' : ", вы можете писать свои жалобы и предложения Админу. Админ ответит вам в ближайшее время",
        		'en' : ", you can write your complaints and suggestions to the Admin. The Admin will answer you soon"
        	},
        "settings" : 
        	{
        		'uz' : "⚙️Sozlamalar menyusi:",
        		'ru' : "⚙️Меню настроек:",
        		'en' : "⚙️Settings menu:"
        	},
        'change_lang_inbut' : 
        	{
				'uz' : "♻️ Tilni o'zgartirish",
				'en' : "♻️ Change the language",
				'ru' : "♻️ Изменить язык"
			},
		"used_lang" :
			{
				'uz' : "🇺🇿 O'zbek tili qo'lanildi!",
				'ru' : "🇷🇺 Используется русский язык!",
				'en' : "🇬🇧 English is used!"
			},

		'shell_sen_name' : 
			{
				'uz' : "Ismingizni yuborishingiz mumkun",
				'ru' : "Вы можете отправить свое имя",
				'en' : "You can send your name"
			},

		'your_name_changed' : 
			{
				'uz' : ["Siznig ismingiz ", " sifatida saqlandi!"],
				'ru' : ["Ваше имя сохранено как ","!"],
				'en' : ["Your name has been saved as ", "!"]
			},

		"bot_version" : 
			{
				'uz' : "Bot versiyasi 3.0.0 (Beta)\n@tarjima_qilaman_robot",
				'ru' : "Версия бота 3.0.0 (бета-версия)\n@tarjima_qilaman_robot",
				'en' : "Bot Version 3.0.0 (Beta)\n@tarjima_qilaman_robot"
			},
		"oxfor_menu" :
			{
				'en' : "Menu Oxfor:",
				'uz' : "Oxford menusi:",
				"ru" : "Оксфорд меню:"
			}
		}

class Message_media:
	def __init__(self):
		pass

	def get_inline_lang(self, lang = 'uz'):
		settings = {
			'uz' : {
				"🇺🇿 o'zbekcha" : "set_uz", 
				"🇷🇺 Ruscha" : 'set_ru', 
				"🇬🇧 Inglizcha" : 'set_en'},
			'ru' : {
				"🇺🇿 узбекский" : "set_uz", 
				"🇷🇺 Русский" : 'set_ru', 
				"🇬🇧 Английский" : 'set_en'},
			'en' : {
				"🇺🇿 Uzbek" : "set_uz", 
				"🇷🇺 Russian" : 'set_ru', 
				"🇬🇧 English" : 'set_en'}
			}

		inline_buttons = []
		for message, data in settings[lang].items():
			inline_buttons.append(InlineKeyboardButton(text = message, callback_data = data))

		return inline_buttons

	def get_regist_button(self, lang = 'uz'):
		params = {
			'uz' : [KeyboardButton(text = "📝 Ro'yxatdan o'tish")],
			'ru' : [KeyboardButton(text = '📝 Зарегистрироваться')],
			'en' : [KeyboardButton(text = "📝 Sign up")]
			}
		return params[lang]

	def get_change_lang_inline(self, lang = 'uz'):
		params = {
			'uz' : "♻️ Tilni o'zgartirish",
			'en' : "♻️ Change the language",
			'ru' : "♻️ Изменить язык"
			}
		return [InlineKeyboardButton(text = params[lang], callback_data = "nouser_change_lang")]

	def get_uh_menu(self, lang = 'uz'):
		"""
			User head menu buttons
		"""
		params = {
			'uz' : [
				[KeyboardButton(text = "uzb-en mode 🇺🇿🔄🇬🇧"), KeyboardButton(text = "uzb-ru mode 🇺🇿🔄🇷🇺"), KeyboardButton(text = "🛡 Oxford Definition")],
				[KeyboardButton(text = "Aloqa 📲"), KeyboardButton(text = "⚙️ Sozlamalar")],
    			[KeyboardButton(text = "📈 statistika"), KeyboardButton(text = "🤖📂 malumot")]],
			'ru' : [
				[KeyboardButton(text = "узб-анг мод 🇺🇿🔄🇬🇧"), KeyboardButton(text = "узб-ру мод 🇺🇿🔄🇷🇺"), KeyboardButton(text = "🛡 Оксфорд дефинитион")],
				[KeyboardButton(text = "контакт 📲"), KeyboardButton(text = "⚙️ настройки")],
    			[KeyboardButton(text = "📈 статистика"), KeyboardButton(text = "🤖📂 информация")]],
			'en' : [
				[KeyboardButton(text = "uzb-en mode 🇺🇿🔄🇬🇧"), KeyboardButton(text = "uzb-ru mode 🇺🇿🔄🇷🇺"), KeyboardButton(text = "🛡 Oxford Definition")],
				[KeyboardButton(text = "Contact 📲"), KeyboardButton(text = "⚙️ Settings")],
    			[KeyboardButton(text = "📈 statistics"), KeyboardButton(text = "🤖📂 info")]]}

		return params[lang]
	
	def get_translater_buttons(self, lang = "uz", mode = "uz-ru/ru-uz"):
		if mode == "uz-ru/ru-uz":
			home = {'uz' : "🏠 Bosh sahifaga", 'en' : "🏠 Back to Home", 'ru' : "🏠 На главную"}
			uzru_buttons = {'uz' : "🇺🇿 O'zbekchadan ➡️ 🇷🇺 Ruschaga", 'ru' : "Из 🇺🇿 узбекского в ➡️ 🇷🇺 русского", 'en' : "From 🇺🇿 Uzbek to ➡️ 🇷🇺 Russian"}
			ruuz_buttons = {'uz' : "🇷🇺 Ruschadan ➡️ 🇺🇿 O'zbekchaga", 'ru' : "С 🇷🇺 русского на ➡️ 🇺🇿 узбекский", 'en' : "From 🇷🇺 Russian to ➡️ 🇺🇿 Uzbek"}
			manual = {'uz' : "📑 qo'lanma", 'ru' : "📑 руководство", 'en' : "📑  manual"}
			return [[KeyboardButton(text = uzru_buttons[lang]), KeyboardButton(text = ruuz_buttons[lang])], [KeyboardButton(text = manual[lang])], [KeyboardButton(text = home[lang])]]
		
		elif mode == "uz-en/en-uz":
			home = {'uz' : "🏠 Bosh sahifaga", 'en' : "🏠 Back to Home", 'ru' : "🏠 На главную"}
			uzen_buttons = {'uz' : "🇺🇿 O'zbekchadan ➡️ 🇬🇧 Inglizchaga", 'ru' : "🇺🇿 from Uzbek to ➡️ 🇬🇧 English", 'en' : "🇺🇿 from Uzbek to ➡️ 🇬🇧 English"}
			enuz_buttons = {'uz' : "🇬🇧 Inglizchadan ➡️ 🇺🇿 O'zbekchaga", 'ru' : "🇬🇧 английского на ➡️ 🇺🇿 узбекский", 'en' : "🇬🇧 From English to ➡️ 🇺🇿 Uzbek"}
			manual = {'uz' : "📑 qo'lanma", 'ru' : "📑 руководство", 'en' : "📑  manual"}
			return [[KeyboardButton(text = uzen_buttons[lang]), KeyboardButton(text = enuz_buttons[lang])], [KeyboardButton(text = manual[lang])], [KeyboardButton(text = home[lang])]]
	
	def get_contact_menu(self, lang = "uz"):
		admin = {'uz' : "👮🏻‍♂️ Admin bilan aloqa", 'en' : "👮🏻‍♂️ Contact Admin", 'ru' : "👮🏻‍♂️Связаться с Админом"}
		coder = {'uz' : "👨🏻‍💻 dasturchi", 'ru' : "👨🏻‍💻 Программист", 'en' : "👨🏻‍💻 Programmer"}
		head_menu = {'uz' : "🏠 Bosh sahifaga", 'en' : "🏠 Back to Home", 'ru' : "🏠 На главную"}

		return [[KeyboardButton(text = admin[lang]), KeyboardButton(text = coder[lang])], [KeyboardButton(text = head_menu[lang])]]

	def admin_chatm(self, lang = "uz"):
		send = {'uz' : "🚀 xabarlarni yuborish", 'en' : "🚀 send messages",'ru' : "🚀 отправлять сообщения"}
		back = {'uz' : "⬅️ orqaga", 'ru' : "⬅️ назад", 'en' : "⬅️ back"}
		head_menu = {'uz' : "🏠 Bosh sahifaga", 'en' : "🏠 Back to Home", 'ru' : "🏠 На главную"}

		return [[KeyboardButton(text = send[lang])], [KeyboardButton(text = back[lang]), KeyboardButton(text = head_menu[lang])]]

	def delet_message(self, lang = "uz"):
		delet = {'uz' : "❌ O'chrish", 'ru' : "❌ Выключать", 'en' : "❌ Turn off"}
		# send = {'uz' : "✅ Tayyor", 'en' : "✅ Ready", 'ru' : "✅ Готовый"}

		return [[InlineKeyboardButton(text = delet[lang], callback_data = "remove")]]

	def get_setingm(self, lang = 'uz'):
		change_lang = {'uz' : "♻️ Tilni o'zgartirish", 'en' : "♻️ Change the language", 'ru' : "♻️ Изменить язык"}
		change_name = {'uz' : "👤 Ismni O'zgartirish", 'ru' : "👤 Изменить имя", 'en' : "👤 Change Name"}
		version = {'uz' : "🆚 Bo't versiyasi", 'ru' : "🆚 Бот версия", 'en' : "🆚 Bot version"}
		head_menu = {'uz' : "🏠 Bosh sahifaga", 'en' : "🏠 Back to Home", 'ru' : "🏠 На главную"}

		return [[KeyboardButton(text = change_lang[lang]), KeyboardButton(text = change_name[lang])], [KeyboardButton(text = version[lang])], [KeyboardButton(text = head_menu[lang])]]


	def get_inlang(self, lang = 'uz'):
		buttons = {'uz' : ["🇺🇿 o'zbekcha", "🇷🇺 Ruscha", "🇬🇧 Inglizcha"], 'ru' : ["🇺🇿 узбекский", "🇷🇺 Русский", "🇬🇧 Английский"], 'en' : ["🇺🇿 Uzbek", "🇷🇺 Russian", "🇬🇧 English"]}
		data = ["set_uz", 'set_ru', 'set_en']
		
		return [[InlineKeyboardButton(text = buttons[lang][0], callback_data = data[0]), InlineKeyboardButton(text = buttons[lang][1], callback_data = data[1]), InlineKeyboardButton(text = buttons[lang][2], callback_data = data[2])]] 

	def get_change_lang(self, lang = 'uz'):
		change_lang = {'uz' : "♻️ Tilni o'zgartirish", 'en' : "♻️ Change the language",'ru' : "♻️ Изменить язык"}
		use = {'uz' : "✅ Qo'lash", 'ru' : "✅ применять", 'en' : '✅ Apply'}

		return [[InlineKeyboardButton(text = change_lang[lang], callback_data = 'rechose'), InlineKeyboardButton(text = use[lang], callback_data = 'aply')]]

	def get_change_name_buttons(self, lang = 'uz'):
		appl = {'uz' : "✅ Qo'lash", 'ru' : "✅ применять", 'en' : '✅ Apply'}
		nont = {'uz' : "❌ Bekor qilish", 'en' : "❌ cancel", 'ru' : "❌ Отмена"}

		return [[KeyboardButton(text = appl[lang]), KeyboardButton(text = nont[lang])]]

	def get_oxfor_menu(self, lang = 'uz'):
		home = {'uz' : "🏠 Bosh sahifaga", 'en' : "🏠 Back to Home", 'ru' : "🏠 На главную"}
		manual = {'uz' : "📑 qo'lanma", 'ru' : "📑 руководство", 'en' : "📑  manual"}

		return [[KeyboardButton(text = manual[lang])], [KeyboardButton(text = home[lang])]]


if __name__ == '__main__':
    pass
	# media = Media()
	# print(media.get_inline_regist(lang = 'uz'))