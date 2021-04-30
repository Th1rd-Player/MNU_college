from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
import logging

from config import TOKEN
import keyboards as kb

from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)
import asyncio
from contextlib import suppress

from aiogram import types




from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton







async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
def send_message_to_admin(message):
    msg = 'От кого: {} \nТип команды: {} \nДата: {}'.format(message.from_user.first_name, message.text, message.date)
 
    return msg

from aiogram import types
@dp.message_handler(commands="special_buttons")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=T_Player_off")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)












from sql import SQLighter

def asT():
    as_mess = "True"
    return as_mess
def asF():
    as_mess = "false"
    return as_mess

from aiogram.utils.exceptions import BotBlocked

db = SQLighter('stud.db')



admin_id = "737108457"


#bot.send_message(admin_id, 'вмамап')
#bot.send_message(admin_id, send_message_to_admin(message))







""" sqlite3 """
help = '''
/start 
/send_id
/admin_list
/student_list
/rank_list
/list_user
/set_curator
/rank
/send_group
/help_rank
/set_rank
/


'''


def messa(message):
	import datetime
	now = datetime.datetime.now()
	mont = str(now.month)
	if len(mont)== 1:
		mont = "0"+mont
	dayy = str(now.day)
	if len(dayy) == 1:
		dayy = "0"+dayy

	hou = str(now.hour)
	if len(hou) == 1:
		hou = "0"+hou
	minut = str(now.minute)
	if len(minut) == 1:
		minut = "0"+minut
	sec = str(now.second)
	if len(sec) == 1:
		sec = "0"+sec
	hourr = ("("+hou+":"+minut+":"+sec+")")
	dayt = (hourr+ dayy+":"+ mont+":"+str(now.year))

	db.add_his(message.from_user.id,dayt, str(message.text))










@dp.message_handler(commands=['set_permision'])
async def set_permision(message: types.Message):
	messag = str(message.text)
	messa(message)
	text = messag.split("-")
	if "admin" in db.what_rank(message.from_user.id):
		if len(text) == 1:
			await bot.send_message(message.from_user.id, """
				При добавлении нескольки превилегий указывайте превилегий через запятую (admin,starosta 155\n
				Пример: \n
				    /set_permision-759130113-starosta 155""")
		elif len(text) == 2:
			await bot.send_message(message.from_user.id, "/set_permision-айди юзера(цыфрами)-привелегия")
		elif len(text) == 3:
			if db.what_id(text[1]) == True:
				if "starosta"in text[2]:
					pass
					


			else:
				await bot.send_message(message.from_user.id, text[1]+ " не является моим пользывателем (его нету в базе)")
			





@dp.message_handler(commands=['start'])
async def subscribe(message: types.Message ):
	#await message.answer("Бот создан студентом T_Player\nОн создан в помощь студентам.\nРасписание, события,если есть идеи пишите создателю ")
	#await bot.answer_callback_query(callback_query.id,'Bot from Th1rd-Player', show_alert=False)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(admin_id, "Новый пользыватель \nid:" + str(message.from_user.id) +"\n username:"+ str(message.from_user.username)+ "\n " + str(message.from_user.first_name) +" "+ str(message.from_user.last_name))
		ide = str(message.from_user.username)
		print(ide)
		if ide == "T_Player":
			msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		else:
			msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		await message.answer("Пожалуйста выберите ваш курс.", reply_markup=kb.inline_course)
	else:
		ide = str(message.from_user.username)
		print(ide)
		if ide == "T_Player":
			msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		else:
			msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
	messa(message)

@dp.message_handler(commands=['send_id'])
async def send_id(message: types.Message):
	messa(message)
	messag = str(message.text)
	if db.what_rank(message.from_user.id) == "admin":
		lv1 = messag.split("/send_id ")[1]
		
		user_id = lv1.split(" ")[0]
		print(user_id)
		messa = lv1.split(user_id)[1]
		from_us = ("{} {}".format(message.from_user.first_name, message.from_user.last_name))
		await bot.send_message(user_id,"Отправитель:" +from_us +"\n"+messa)

	else:
		await bot.send_message(message.from_user.id, "Ваш статус не позволяет выполнение данной команды...")

   



@dp.message_handler(commands=["admin_list"])
async def admin_list(message: types.Message):
	messa(message)
	records = db.all_rank("admin")
	for row in records:
		await bot.send_message(message.from_user.id, row)
		buttons = [
		types.InlineKeyboardButton(text=str(row[0]), url="https://github.com"),
		types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
		]
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		keyboard.add(*buttons)
		await message.answer("Кнопки-ссылки", reply_markup=keyboard)

@dp.message_handler(commands=["student_list"])
async def admin_list(message: types.Message):
	messa(message)
	records = db.all_rank("student")
	for row in records:
		await bot.send_message(message.from_user.id, row)

@dp.message_handler(commands=["student_list"])
async def admin_list(message: types.Message):
	messa(message)
	records = db.all_rank("student")
	for row in records:
		await bot.send_message(message.from_user.id, row)




rank_list = '''
admin все возможности управляющий
student обычный пользыватель
prepod преподователь управление рассылка групам в которых преподаёт
kurator управление групой которую курирует

'''
@dp.message_handler(commands=["rank_list"])
async def admin_list(message: types.Message):
	messa(message)
	await bot.send_message(message.from_user.id, rank_list)

@dp.message_handler(commands=['list_user'])
async def all_user(message: types.Message):
	messa(message)
	subscriptions = db.get_subscriptions()
	for s in subscriptions:
		await bot.send_message(message.from_user.id, "user_id: "+ s[0] + " group: "+ s[1]+ "status: "+ s[2] + "username: "+s[3]+ "rank: "+s[4])



@dp.message_handler(commands=['set_curator'])
async def send_id_uss(message: types.Message):
	messa(message)
	messa = str(message.text)
	messag = messa.split("set_curator ")[1]
	print(messag)
	group = messag.split(" ")[1]# user_id
	print(group)
	id_user = messag.split(" ")[0]
	print(id_user)
	db.set_curator(id_user, group)
	
	#if "kurato"

@dp.message_handler(commands=['rank'])
async def send_id_uss(message: types.Message):
	messa(message)
	rank = db.what_rank(message.from_user.id)
	for rank in rank:
		await bot.send_message(message.from_user.id, db.what_rank(message.from_user.id))
		break








@dp.message_handler(commands=['help_rank'])
async def send_id_uss(message: types.Message):
	messa(message)
	await bot.send_message(message.from_user.id, "student обычный пользыватель (студент) \n teacher преподователь \n admin куратор бота (управляющий)")


@dp.message_handler(commands=['set_rank'])
async def send_id_uss(message: types.Message):
	messa(message)
	mess = message.text
	messa = mess.split("/set_rank ")[1]
	rank = messa.split(" ")[1]# user_id
	id_user = messa.split(" ")[0]
	await bot.send_message(message.from_user.id, "установить уровень "+ rank + " для полдьзывателя "+ id_user)
	db.update_rank(id_user, rank)
	await bot.send_message(message.from_user.id, db.what_rank(message.from_user.id))


@dp.message_handler(text='Я преподователь')
async def process_callback_button1(message: types.Message):
	messa(message)
	await bot.send_message(admin_id, str(message.from_user.first_name) + str(message.from_user.last_name) + 'пытается получить статус преподователя \n username: @'+str(message.from_user.username)+' \n user_id : '+str(message.from_user.id)) 
	await bot.send_message(message.from_user.id, "Напишите @T_Player для завершения авторизации как преподователь...")

'''
@dp.message_handler(text='Я преподователь')
async def process_callback_button1(message: types.Message):
    #await bot.send_message(admin_id,send_message_to_admin)
    await bot.send_message(admin_id,'{} {} пытается получить статус преподователя \n username: @{} \n user_id : {}'.format(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id) )
    await bot.send_message(message.from_user.id, ) '''

@dp.message_handler(text=['1-й'])
async def process_callback_button1(message: types.Message):
	messa(message)
	await bot.send_message(message.from_user.id, 'Вы выбрали 1 курс?', reply_markup=kb.inline_kb_course_1 )

@dp.message_handler(text=['2-й'])
async def process_callback_button1(message: types.Message):
	messa(message)
	await bot.send_message(message.from_user.id, 'Вы выбрали 2 курс?', reply_markup=kb.inline_kb_course_2 )

@dp.message_handler(text=['3-й'])
async def process_callback_button1(message: types.Message):
	messa(message)
	await bot.send_message(message.from_user.id, 'Вы выбрали 3 курс?', reply_markup=kb.inline_kb_course_3 )

@dp.message_handler(text=['4-й'])
async def process_callback_button1(message: types.Message):
	messa(message)
	await bot.send_message(message.from_user.id, 'Вы выбрали 4 курс?', reply_markup=kb.inline_kb_course_4 )


@dp.message_handler(text =['115-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 115 группы?', reply_markup=kb.inline_wha115 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 115 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "1","15", username, "student")
	ide = str(message.from_user.username)
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)

@dp.message_handler(text =['125-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 125 группы?', reply_markup=kb.inline_wha125 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 125 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not  message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "125", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['135-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 135 группы?', reply_markup=kb.inline_wha135 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 135 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not  message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "135", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['155-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 155 группы?', reply_markup=kb.inline_wha155 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 155 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "155", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	#db.update_sqlite_table("1",message.from_user.id)
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)

@dp.message_handler(text=['165-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 165 группы?', reply_markup=kb.inline_wha165 )
	else:
		await bot,send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 165 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	# если юзера нет в базе, добавляем его
	db.add_group(message.from_user.id,"165", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text =['215-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 215 группы?', reply_markup=kb.inline_wha215 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 215 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
		# если юзера нет в базе, добавляем его
	db.add_group(message.from_user.id, "215", username, "student")
	ide = str(message.from_user.username)
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text =['225-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 225 группы?', reply_markup=kb.inline_wha225 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 225 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "225", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['235-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 235 группы?', reply_markup=kb.inline_wha235 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 235 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username :
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "235", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['255-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 255 группы?', reply_markup=kb.inline_wha255 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 255 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "255", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	#db.update_sqlite_table("1",message.from_user.id)
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)

@dp.message_handler(text=['265-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 265 группы?', reply_markup=kb.inline_wha265 )
	else:
		await bot,send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 265 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id,"265", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)

@dp.message_handler(text =['315-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 315 группы?', reply_markup=kb.inline_wha315 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 315 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "315", username, "student")
	ide = str(message.from_user.username)
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
    #asyncio.create_task(delete_message(msgg))

@dp.message_handler(text =['325-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 325 группы?', reply_markup=kb.inline_wha325 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 325 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "325", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)

@dp.message_handler(text=['335-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 335 группы?', reply_markup=kb.inline_wha335 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 335 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "335", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)

@dp.message_handler(text=['355-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 355 группы?', reply_markup=kb.inline_wha355 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 355 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "355", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	#db.update_sqlite_table("1",message.from_user.id)
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['365-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 365 группы?', reply_markup=kb.inline_wha365 )
	else:
		await bot,send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 365 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
		# если юзера нет в базе, добавляем его
	db.add_group(message.from_user.id,"365", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text =['415-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 415 группы?', reply_markup=kb.inline_wha415 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 415 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
		# если юзера нет в базе, добавляем его
	db.add_group(message.from_user.id, "415", username, "student")
	ide = str(message.from_user.username)
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text =['425-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 425 группы?', reply_markup=kb.inline_wha425 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 425 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "425", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['435-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 435 группы?', reply_markup=kb.inline_wha435 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 435 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "435", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['455-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 455 группы?', reply_markup=kb.inline_wha455 )
	else:
		await bot.send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 455 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
	db.add_group(message.from_user.id, "455", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	#db.update_sqlite_table("1",message.from_user.id)
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
		#asyncio.create_task(delete_message(msgg))
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['465-я'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if(not db.subscriber_exists(message.from_user.id)):
		await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 465 группы?', reply_markup=kb.inline_wha465 )
	else:
		await bot,send_message(message.from_user.id, "Вы уже есть в базе")

@dp.message_handler(text=['Да я из 465 группы'])
async def process_callback_button1(message: types.Message):
	messa(message)
	if not message.from_user.username:
		username = "not_add"
	else:
		username = message.from_user.username
		# если юзера нет в базе, добавляем его
	db.add_group(message.from_user.id,"465", username, "student")
	await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
	ide = str(message.from_user.username)
	if ide == "T_Player":
		msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
	else:
		msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
		#asyncio.create_task(delete_message(msgg))

@dp.message_handler(text=['Нет'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите из какой вы группы...', reply_markup=kb.inline_course)

'''
@dp.message_handler(text=['Обновить статус'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите из какой вы группы...', reply_markup=kb.new_schedul)
'''

@dp.message_handler(text=['Обновить расписание'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=kb.new_what_course)
    #messa(message)

@dp.callback_query_handler(lambda c: c.data == 'button115')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id,'bot made T_Player ', show_alert=False)
    #messa(callback_query)


@dp.callback_query_handler(text=["/start"])
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id,'bot made T_Player ', show_alert=False)


@dp.callback_query_handler(lambda c: c.data == 'c1')
async def process_callback_button1(callback_query: types.CallbackQuery):
	#asyncio.create_task(delete_message(msg))
	await bot.answer_callback_query(callback_query.id,'Изменение расписания для 1 курса.')
	msg = await bot.send_message(callback_query.from_user.id, 'Изменение расписания для 1 курса.',reply_markup=kb.new_schedule_course1)

@dp.callback_query_handler(lambda c: c.data == 'c2')
async def process_callback_button1(callback_query: types.CallbackQuery):
	#asyncio.create_task(delete_message(msg))
	await bot.answer_callback_query(callback_query.id,'Изменение расписания для 2 курса.')
	msg = await bot.send_message(callback_query.from_user.id, 'Изменение расписания для 2 курса.',reply_markup=kb.new_schedule_course1)

@dp.callback_query_handler(lambda c: c.data == 'c3')
async def process_callback_button1(message: types.Message):
	#asyncio.create_task(delete_message(msg))
	await bot.answer_callback_query(callback_query.id,'Изменение расписания для 3 курса.')
	msg = await bot.send_message(callback_query.from_user.id, 'Изменение расписания для 3 курса.',reply_markup=kb.new_schedule_course1)
	await bot.send_message(message.from_user.id,"3",reply_markup=kb.new_schedule_course3)

@dp.callback_query_handler(lambda c: c.data == 'c4')
async def process_callback_button1(callback_query: types.CallbackQuery):
	#asyncio.create_task(delete_message(msg))
	await bot.answer_callback_query(callback_query.id,'Изменение расписания для 4 курса.')
	msg = await bot.send_message(callback_query.from_user.id, 'Изменение расписания для 4 курса.',reply_markup=kb.new_schedule_course1)




@dp.message_handler(commands=['send_group'])

async def process_command_1(message: types.Message):
    #if admin_id  == message.from_user.id:
    message = str(message.text)
    messag = message.split()
    subscriptions = db.get_group(messag[1])
    mes = message.split(messag[0])[1]
    mess= message.split(messag[1])[1]
    print(mess)
    for s in subscriptions:
    	await bot.send_message(s[0],mess)
    messa(message)


@dp.message_handler(text=["Расписание"])
async def allsa_prover(message: types.Message):
	import datetime
	from datetime import date
	now = datetime.datetime.now()
	dt = datetime.date(now.year, now.month, now.day)
	wk = dt.isocalendar()[1]
	iso = (wk & 1) == 0
	gg = db.group(message.from_user.id)
	dda = str(now.isoweekday())
	#if db.group(message.from_user.id) == str(gg):
	fd = db.all_in_rozkla(gg)
	for row in fd:
		if row[0] == dda:
			await bot.send_message(message.from_user.id, str(row[2]))
			fun = True
			#break

	if fun == False:
		await bot.send_message(message.from_user.id, "Извените но для вас нету расписания(возможно его ещё не добавили)")
	messa(message)


@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)  # отправит след текст челез 10 сек
    await message.reply("Вы заблокированы")
    messa(message)


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    await bot.send_message(admin_id,F"Меня заблокировал пользователь!\nСообщение: \nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True





@dp.message_handler(commands=["new_rozk"])
async def all_prover(message: types.Message):
	ss = str(message.text)
	s = ss.split("/new_rozk ")[1]
	d = s.split()
	t = s.split(d[0])
	t = s.split(d[1])[1]
	print(t)
	t = str(t)
	db.set_in_rozkla(d[0], d[1], t)
	await bot.send_message(message.from_user.id, "Добавлено\n")
	messa(message)


@dp.message_handler()
async def add_his(message: types.Message):
	import datetime
	now = datetime.datetime.now()
	mont = str(now.month)
	if len(mont)== 1:
		mont = "0"+mont
	dayy = str(now.day)
	if len(dayy) == 1:
		dayy = "0"+dayy
	
	hou = str(now.hour)
	if len(hou) == 1:
		hou = "0"+hou
	minut = str(now.minute)
	if len(minut) == 1:
		minut = "0"+minut
	sec = str(now.second)
	if len(sec) == 1:
		sec = "0"+sec
	hourr = ("("+hou+":"+minut+":"+sec+")")
	dayt = (hourr+ dayy+":"+ mont+":"+str(now.year))

	db.add_his(message.from_user.id,dayt, str(message.text))
	messa(message)
	

if __name__ == '__main__':
    executor.start_polling(dp)