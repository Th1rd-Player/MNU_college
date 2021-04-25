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
async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def send_message_to_admin(message):
    msg = 'От кого: {} \nТип команды: {} \nДата: {}'.format(message.from_user.first_name, message.text, message.date)
 
    return msg


from sql import SQLighter

def asT():
    as_mess = "True"
    return as_mess
def asF():
    as_mess = "false"
    return as_mess
logging.basicConfig(level=logging.INFO)

db = SQLighter('stud.db')



admin_id = "737108457"


#bot.send_message(admin_id, 'вмамап')
#bot.send_message(admin_id, send_message_to_admin(message))






""" sqlite3 """

































'''
def send_message_to_admin(message):
    msg = 'От кого: {} \nТип команды: {} \nДата: {}'.format(message.from_user.first_name, message.text, message.date)
    return msg'''


#start



@dp.message_handler(commands=['del'])
async def all_msg_handler(message: types.Message):
    await ms.reply('прячем клавиатуру', reply_markup='')
@dp.message_handler(commands=['new_course'])
async def subscribe(message: types.Message):
    # если юзера нет в базе, добавляем его
    msg =  await message.answer("Пожалуйста выберите вашу группу.", reply_markup=kb.inline_kb11)
    asyncio.create_task(delete_message(msg))

#send_all

@dp.message_handler(commands=['start'])
async def subscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        ide = str(message.from_user.username)
        print(ide)
        if ide == "T_Player":
            
            msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
            #asyncio.create_task(delete_message(msgg))
        else:
            
            msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
            #asyncio.create_task(delete_message(msgg))
            
        await message.answer("Пожалуйста выберите ваш курс.", reply_markup=kb.inline_course)
    else:
        ide = str(message.from_user.username)
        print(ide)
        if ide == "T_Player":
            
            msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
            #asyncio.create_task(delete_message(msgg))
        else:
            
            msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
            #asyncio.create_task(delete_message(msgg))

        # если он уже есть, то просто обновляем ему статус подписки
        pass
        #db.update_subscription(message.from_user.id, True)
        #await message.answer("Вы уже есть в базе если вы перейшли на новый курс введите команду /new_course")

# инициализируем соединение с БД

# инициализируем парсер




# Команда отписки

@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Я увидел что вы  не были ни разу автоизированы")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        
@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)
# проверяем наличие новых игр и делаем рассылки
@dp.message_handler(text =['115-я'])
async def process_callback_button1(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 115 группы?', reply_markup=kb.inline_wha115 )
    else:
        await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 115 группы'])
async def process_callback_button1(message: types.Message):
    # если юзера нет в базе, добавляем его
    db.add_group(message.from_user.id, "1","15", message.from_user.username, "student")
    ide = str(message.from_user.username)
    await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
    if ide == "T_Player":
        msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
        #asyncio.create_task(delete_message(msgg)
    else:
        msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
            #asyncio.create_task(delete_message(msgg))


@dp.message_handler(text=['125-я'])
async def process_callback_button1(message: types.Message):
    if(not db.update_subscription(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 125 группы?', reply_markup=kb.inline_wha125 )
    else:
        await bot.send_message(message.from_user.id, "Вы уже есть в базе",)



@dp.message_handler(text='Я преподователь')
async def process_callback_button1(message: types.Message):
    #await bot.send_message(admin_id,send_message_to_admin)
    await bot.send_message(admin_id,'{} {} пытается получить статус преподователя \n username: @{} \n user_id : {}'.format(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id) )
    await bot.send_message(message.from_user.id, )

@dp.message_handler(commands=['stop'])
async def stoped(message: types.Message):
    #from sys import exit
    #exit()
    pass
@dp.message_handler(commands=['rank'])
async def process_callback_button1(message: types.Message):
    rank = db.what_rank(message.from_user.id)
    if "admin" in rank:
        await bot.send_message(message.from_user.id, "Ваш уровень допуска: 1"+db.what_rank(message.from_user.id))
    elif "starosta" in rank:

        await bot.send_message(message.from_user.id, "Ваш уровень допуска: 2"+db.what_rank(message.from_user.id))
        await bot.send_message(message.from_user.id, "Вам доступно: \n Рассылка вашей группе \n Добавление домашнего задание \n Назначение и снятие заместителя\n Назначение человека который будет отвечать за домашнее задание")
    elif "староста" in  rank:
        
        await bot.send_message(message.from_user.id, "Ваш уровень допуска: 3"+db.what_rank(message.from_user.id))
        await bot.send_message(message.from_user.id, "Вам доступно: \n Рассылка вашей группе \n Добавление домашнего задание \n Назначение и снятие заместителя\n Назначение человека который будет отвечать за домашнее задание")
    elif "админ" in rank:
        
        await bot.send_message(message.from_user.id, "Ваш уровень допуска: 4"+db.what_rank(message.from_user.id))
        await bot.send_message(message.from_user.id, "Вам доступно: \n всё")

    else:

        await bot.send_message(message.from_user.id, "Ваш уровень допуска: " + rank)

@dp.message_handler(commands=['set_rank'])
async def send_id_uss(message: types.Message):
    mess = message.text
    messa = mess.split("/set_rank ")[1]
    #await bot.send_message(message.from_user.id,'')
    rank = messa.split(" ")[1]# user_id
    id_user = messa.split(" ")[0]

    await bot.send_message(message.from_user.id, "установить уровень "+ rank + " для полдьзывателя "+ id_user)
    db.update_rank(id_user, rank)
    print(id_user)
    print(rank, db.what_rank(message.from_user.id))
    await bot.send_message(message.from_user.id, db.what_rank(message.from_user.id))


#'CallbackQuery'
@dp.message_handler(commands=['send_id'])
async def send_id_uss(message: types.Message):
    messa = str(message.text)
    id_us = messa.split(" ")[1]
    messag = messa.split(id_us)[1]
    await bot.send_message(id_us,messag)

@dp.message_handler(text=['1-й'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали 1 курс?', reply_markup=kb.inline_kb_course_1 )

@dp.message_handler(text=['2-й'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали 2 курс?', reply_markup=kb.inline_kb_course_2 )

@dp.message_handler(text=['3-й'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали 3 курс?', reply_markup=kb.inline_kb_course_3 )

@dp.message_handler(text=['4-й'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали 4 курс?', reply_markup=kb.inline_kb_course_4 )


@dp.message_handler(text=['Да я из 125 группы'])
async def process_callback_button1(message: types.Message):
    db.add_group(message.from_user.id, "1","25", message.from_user.username, "student")
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
    if(not db.subscriber_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 135 группы?', reply_markup=kb.inline_wha135 )
    else:
        await bot.send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 135 группы'])
async def process_callback_button1(message: types.Message):
    db.add_group(message.from_user.id, "1","35", message.from_user.username, "student")
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
    if(not db.subscriber_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 155 группы?', reply_markup=kb.inline_wha155 )
    else:
        await bot.send_message(message.from_user.id, "Вы уже есть в базе")
    
    
    
@dp.message_handler(text=['Да я из 155 группы'])
async def process_callback_button1(message: types.Message):
    db.add_group(message.from_user.id, "1","55", message.from_user.username, "student")
    await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
    #db.update_sqlite_table("1",message.from_user.id)
    ide = str(message.from_user.username)
    if ide == "T_Player":
            
        msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
        #asyncio.create_task(delete_message(msgg))
    else:
        
        msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
        #asyncio.create_task(delete_message(msgg))



@dp.message_handler(text=['165-я'])
async def process_callback_button1(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Вы подтвержаете что вы из 165 группы?', reply_markup=kb.inline_wha165 )
    else:
        await bot,send_message(message.from_user.id, "Вы уже есть в базе")
@dp.message_handler(text=['Да я из 165 группы'])
async def process_callback_button1(message: types.Message):
    # если юзера нет в базе, добавляем его
    db.add_group(message.from_user.id,"1","65", message.from_user.username, "student")
    await bot.send_message(message.from_user.id, 'Вы подтвердили что вы из '+db.what_group(message.from_user.id)+' группы.')
    ide = str(message.from_user.username)

    if ide == "T_Player":
            
        msgg = await message.answer("Меню добавленно",reply_markup=kb.admin_key)
        #asyncio.create_task(delete_message(msgg))
    else:
        
        msgg = await message.answer("Меню добавленно",reply_markup=kb.user_key)
        #asyncio.create_task(delete_message(msgg))


@dp.message_handler(text=['Нет'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите из какой вы группы...', reply_markup=kb.inline_course)





































@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


@dp.callback_query_handler(commands=['sdf'])
async def process(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉',
        show_alert=True)




@dp.callback_query_handler(lambda c: c.data == 'res')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'{callback_query.message.text}')


##

@dp.message_handler(commands=['new_version'])
async def process_callback_button1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Нажата первая кнопка!')
    subscriptions = db.get_subscriptions()
    # отправляем всем новость
    #await bot.send_message(message.chat.id, message)
    for s in subscriptions:
        await bot.send_message(s[0],"Наш бот потерпел обновленийнекоторых изменений нажмите /start")





'''
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    ide = str(message.from_user.username)
    print(ide)
    if ide == "T_Player":
        print(ide+"1")
        await message.reply("Привет!", reply_markup=kb.admin_key)
    else:
        print(ide+"2")
        await message.reply("Привет! ", reply_markup=kb.gret_kb44)
'''

help_message = text(
    "Это урок по клавиатурам.",
    "Доступные команды:\n",
    "/start - приветствие",
    "\nШаблоны клавиатур:",
    "/hi1 - авто размер",
    "/hi2 - скрыть после нажатия",
    "/hi3 - больше кнопок",
    "/hi4 - кнопки в ряд",
    "/hi5 - больше рядов",
    "/hi6 - запрос локации и номера телефона",
    "/hi7 - все методы"
    "/rm - убрать шаблоны",

    "\nИнлайн клавиатуры:",
    "/1 - первая кнопка",
    "/2 - сразу много кнопок",
    sep="\n"
)
@dp.message_handler(commands=["help_send_group"])
async def process_admi(message: types.Message): 
    await bot.send_message(message.from_user.id, "Пример:")
    await bot.send_message(message.from_user.id, "/send_group 155 После пар оставайтесь в аудитории ")
    await bot.send_message(message.from_user.id, "Все пользыватели с отметкой 155 группы получат сообщение:")
    await bot.send_message(message.from_user.id, "­­­­После пар оставайтесь в аудитории")
@dp.message_handler(commands=['help_send_all'])
async def procc(message: types.Message):
    await bot.send_message(message.from_user.id, "Пример:")
    await bot.send_message(message.from_user.id, "/send_all в пятницю о 15;00 конференція посилання скину пізніше")
    await bot.send_message(message.from_user.id, "все пользыватели со статусом студент получат сообщение:")
    await bot.send_message(message.from_user.id, "в пятницю о 15;00 конференція посилання скину пізніше")









admin_help = text(
    "/help_команда  о которой нужно узнать больше\n"
    "/send_group номер группы  текст сообщения\n"
    "/send_all текст\n"
    ""
    ""
    ""
    )
@dp.message_handler(commands=["admin_help"])
async def process_admin_help(message: types.Message):
    await bot.send_message(message.from_user.id, admin_help)
async def process_admin_help(message: types.Message):
    await bot.send_message(message.from_user.id, admin_help)
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)

@dp.message_handler(commands=['send_all'])
#set_rank
async def process_command_1(message: types.Message):
    #if admin_id  == message.from_user.id:
    subscriptions = db.get_subscriptions()
    message = str(message.text)
    messag = message.split("/send_all")[1]











    for s in subscriptions:
        #await bot.send_message(s[0],message) 
        await bot.send_message(s[0],messag)
    #if message.text == 'Математические операции':
        #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
@dp.message_handler(commands=['send_group'])

async def process_command_1(message: types.Message):
    #if admin_id  == message.from_user.id:
    message = str(message.text)

    messag = message.split("/send_group")[1]

    if messag[:4] == " 155":
        subscriptions = db.get_group(155)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 115":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 125":
        subscriptions = db.get_group(125)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 135":
        subscriptions = db.get_group(135)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 165":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4] == " 255":
        subscriptions = db.get_group(155)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 215":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 225":
        subscriptions = db.get_group(125)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 235":
        subscriptions = db.get_group(135)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 265":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4] == " 355":
        subscriptions = db.get_group(155)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 315":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 325":
        subscriptions = db.get_group(125)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 335":
        subscriptions = db.get_group(135)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 365":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4] == " 455":
        subscriptions = db.get_group(155)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 415":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 425":
        subscriptions = db.get_group(125)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 435":
        subscriptions = db.get_group(135)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)
    elif messag[:4]== " 465":
        subscriptions = db.get_group(115)
        for s in subscriptions:
            #await bot.send_message(s[0],message) 
            await bot.send_message(s[0],messag)
        #if message.text == 'Математические операции':
            #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)

@dp.message_handler(text=['start'])
#send_group
async def process_rass(message: types.Message):
    await message.answer('Для разссылки своей группе введите "/send_group текст сообщения которое нужно отослать"')
@dp.message_handler(commands=['all_new_course'])
async def all_new_course(message: types.Message):
    ide = str(message.from_user.username)
    print(ide)
    if ide == "T_Player":
    
        import datetime
        now = datetime.datetime.now()
        if now.month == 6 and now.day > 13:
            db.new_course()
        else:
            await message.answer("Извените сейчас смена курса невозможна она будет доступна в июне после 13 числа(после последней атестации)")
    else:
        await message.answer('Вам данная команда недоступна обратитесь к творцу @T_Player')
@dp.message_handler(commands=['new_sche'])
async def all_sched(message: types.Message):
    pass
    

    


    #print(fd, " ", message.from_user.id)


@dp.message_handler(commands=['list_user'])
async def all_user(message: types.Message):
#if admin_id  == message.from_user.id:
    subscriptions = db.get_subscriptions()
    #message = str(message.text)
    #messag = message.split("/send_all")[1]

    for s in subscriptions:
        #await bot.send_message(s[0],message) 
        await bot.send_message(message.from_user.id, "user_id: "+s[0]+"  : "+s[1]+"  : "+s[2]+"  : "+s[3]+" username: "+s[4]+"  : "+s[5])
        #message.from_user.id, s[0]+":"+s[1]+":"+s[2]+":"+s[3]+":"+s[4]+":"+s[5]
    #if message.text == 'Математические операции':
        #await message.answer("Напишите выражение и нажмите кнопку", reply_markup=kb.inline_kb)





@dp.message_handler()
async def all_prover(message: types.Message):

    if message.text == "Расписание":
        import datetime
        from datetime import date
        now = datetime.datetime.now()
        #date = date.today()
        dt = datetime.date(now.year, now.month, now.day)
        #print (now.strftime("%d-%m-%Y %H:%M"))
        wk = dt.isocalendar()[1]
        iso = (wk & 1) == 0
        #print(iso)
        if iso == True:
            print("help")
        else:
            print("hee")
        if db.group(message.from_user.id) == "125":
            #print(db.group(message.from_user.id))
            #import schedule
            f = open('schedule_125.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "115":
            #print(db.group(message.from_user.id))
            f = open('schedule_115.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "155":
            #print(db.group(message.from_user.id))
            f = (open('schedule_155.txt'))
            #print(f)
            fd = (f.read())
            #print(fd)
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]
                print(fd)

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")

        elif db.group(message.from_user.id) == "135":
            #print(db.group(message.from_user.id))
            f = (open('schedule_135.txt'))
            #print(f)
            fd = (f.read())
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "165":
            #print(db.group(message.from_user.id))
            f = open('schedule_165.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]
#Домашнее задание
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "215":
            f = open('schedule_215.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "225":
            f = open('schedule_225.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "235":
            f = open('schedule_235.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "255":
            f = open('schedule_255.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "265":
            f = open('schedule_265.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "315":
            f = open('schedule_315.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "325":
            f = open('schedule_325.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "335":
            f = open('schedule_335.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "355":
            f = open('schedule_355.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "365":
            f = open('schedule_365.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "415":
            f = open('schedule_415.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "425":
            f = open('schedule_425.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "435":
            f = open('schedule_435.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "455":
            f = open('schedule_455.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        elif db.group(message.from_user.id) == "465":
            f = open('schedule_465.txt')
            fd = f.read()
            if now.isoweekday() == 1:
                fd = fd.split("№0")[0]
                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 2:
                fd = fd.split("№0")[1]
                fd = fd.split("№1")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 3:
                fd = fd.split("№1")[1]
                fd = fd.split("№2")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 4:
                fd = fd.split("№2")[1]
                fd = fd.split("№3")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 5:
                fd = fd.split("№3")[1]
                fd = fd.split("№4")[0]

                await bot.send_message(message.from_user.id, fd)
            elif now.isoweekday() == 6:
                await bot.send_message(message.from_user.id, "Субота какое расписание")
            elif now.isoweekday() == 7:
                await bot.send_message(message.from_user.id, "Воскресенье какое расписание")
        else:
            await bot.send_message(message.from_user.id, "я не смог вас найти в базе(вы не преднадлежите ни к одной группе нашего колледжа)")


        
        #b = db.new_course()
        #await message.answer(b)







#gret_kb44



    else:
        pass




if __name__ == '__main__':
    executor.start_polling(dp)