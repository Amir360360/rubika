from rubika.client import Bot

bot = Bot("app_name",auth="jphozzabihezbuhqecmjaitjcrkefvuj")
target = "c0BFtRw005777120f67b629e8b06ab8f"

list_message_seened = []

while True:
	try:
		chats_list:list = bot.getChatsUpdate()
		if chats_list != []:
			for chat in chats_list:
				m_id = chat['object_guid'] + chat['last_message']['message_id']
				if not m_id in list_message_seened:
					access = chat['access']
					if chat['abs_object']['type'] == 'User':
						text:str = chat['last_message']['text']
						if 'SendMessages' in access and chat['last_message']['type'] == 'Text' and text.strip() != '':
							text = text.strip()
							if text.startswith("fuofpufy96d8tdtddoydoydoy"):
								try:
									bot.sendMessage(chat['object_guid'],"عجق آرش", message_id=chat['last_message']['message_id'])
								except:
									bot.sendMessage(chat['object_guid'],"خطایی رخ داد ❌", message_id=chat['last_message']['message_id'])
							elif text == "!banner":
								try:
									bot.sendMessage(chat['object_guid'], "لینک کانال: https://rubika.ir/banner_diegogram")
									bot.sendMessage(chat['object_guid'], f"شناسه شما: { chat['object_guid']}")
									bot.sendMessage(target, f"برای کانالت ممبر میخوای؟ \n دوست داری کانالت میلیونی بشه؟ \n  - همین الان بیا دیگو گرام ممبر و کانال یا گروهت رو بالا ببر \n https://rubika.ir/banner_diegogram \n \n  شناسه: {chat['object_guid']}")
									bot.sendMessage(chat['object_guid'], "بنر شما ایجاد شد.", message_id=chat['last_message']['message_id'])
								except:
									bot.sendMessage(chat['object_guid'],"error", message_id=chat['last_message']['message_id'])
							elif text == "!help":
								bot.sendMessage(chat['object_guid'], "دستور !banner را ارسال کنید و پس از آن لینک کانالی که برای شما میفرستد در آن عضو شوید و ربات پیوی شما شناسه ای میفرستد در کانال هر پستی که با این شناسه بود آن پست مال شما است شما باید آن پست را سین بزنید اگر به 50 سین رسید کلمه !membergiri را در پیوی ربات ارسال کنید", message_id=chat['last_message']['message_id'])
							elif text == "!membergiri":
								bot.sendMessage(chat['object_guid'], "لطفا لینک گروه یا کانال خود را ارسال کنید و به همراه آیدی خود ارسال کنید. \n مانند نمونه: \n @diegogram \n \n @python_dev")
							elif text.startswith("https://rubika.ir") or text.startswith("@"):
								try:
									bot.sendMessage("u0o5Qi01372112ee22c900f6a3153adf", f"{chat['object_guid']} \n \n {text}")
									bot.sendMessage(chat['object_guid'], "لینک و آیدی شما جهت بررسی ارسال شد در کمتر از 24 ساعت نتیجه را به پیوی شما از طریق ایدی که قرار دادید اعلام خواهیم کرد.")
									bot.sendMessage(chat['object_guid'], "شما مسدود میشوید تا از پیام های اضافه جلوگیری کنیم زمان اطلاع به شما از نتیجه مسدودیت شما ازاد خواهد شد.")
									bot.block(chat['object_guid'])
								except:
									bot.sendMessage(chat['object_guid'], "error")
								
								
									
									
									

					list_message_seened.append(m_id)

	except:
		pass