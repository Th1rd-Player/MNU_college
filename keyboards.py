from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
#btn

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)

markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))


inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))

inline_res = InlineKeyboardButton('Рассчитать', callback_data='res')


markup3.row(KeyboardButton("4"), KeyboardButton("5"))
markup3.insert(KeyboardButton("6"))
markup3.add(KeyboardButton("Новая строка"))



course1 = KeyboardButton('1-й')

course2 = KeyboardButton('2-й')

course3 = KeyboardButton('3-й')

course4 = KeyboardButton('4-й')
i_prepo = KeyboardButton("Я преподователь")
inline_course = ReplyKeyboardMarkup().add(i_prepo).add(course1, course2).add(course3, course4)


inline_btn_115 = KeyboardButton('115-я')
inline_btn_125 = KeyboardButton('125-я')
inline_btn_135 = KeyboardButton('135-я')
inline_btn_155 = KeyboardButton('155-я')
inline_btn_165 = KeyboardButton('165-я')
inline_kb_course_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(inline_btn_115, inline_btn_125, inline_btn_135, inline_btn_155, inline_btn_165)
inline_btn_215 = KeyboardButton('215-я')
inline_btn_225 = KeyboardButton('225-я')
inline_btn_235 = KeyboardButton('235-я')
inline_btn_255 = KeyboardButton('255-я')
inline_btn_265 = KeyboardButton('265-я')
inline_kb_course_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(inline_btn_215, inline_btn_225, inline_btn_235, inline_btn_255, inline_btn_265)
inline_btn_315 = KeyboardButton('315-я')
inline_btn_325 = KeyboardButton('325-я')
inline_btn_335 = KeyboardButton('335-я')
inline_btn_355 = KeyboardButton('355-я')
inline_btn_365 = KeyboardButton('365-я')
inline_kb_course_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(inline_btn_315, inline_btn_325, inline_btn_315, inline_btn_355, inline_btn_365)
inline_btn_415 = KeyboardButton('415-я')
inline_btn_425 = KeyboardButton('425-я')
inline_btn_435 = KeyboardButton('435-я')
inline_btn_455 = KeyboardButton('455-я')
inline_btn_465 = KeyboardButton('465-я')
inline_kb_course_4 = ReplyKeyboardMarkup(resize_keyboard=True).add(inline_btn_415, inline_btn_425, inline_btn_435, inline_btn_455, inline_btn_465)

inline_no=KeyboardButton('Нет')

yes115 = KeyboardButton('Да я из 115 группы')
yes125 = KeyboardButton('Да я из 125 группы')
yes135 = KeyboardButton('Да я из 135 группы')
yes155 = KeyboardButton('Да я из 155 группы')
yes165 = KeyboardButton('Да я из 165 группы')

yes215 = KeyboardButton('Да я из 215 группы')
yes225 = KeyboardButton('Да я из 225 группы')
yes235 = KeyboardButton('Да я из 235 группы')
yes255 = KeyboardButton('Да я из 255 группы')
yes265 = KeyboardButton('Да я из 265 группы')

yes315 = KeyboardButton('Да я из 315 группы')
yes325 = KeyboardButton('Да я из 325 группы')
yes335 = KeyboardButton('Да я из 335 группы')
yes355 = KeyboardButton('Да я из 355 группы')
yes365 = KeyboardButton('Да я из 365 группы')

yes415 = KeyboardButton('Да я из 415 группы')
yes425 = KeyboardButton('Да я из 425 группы')
yes435 = KeyboardButton('Да я из 435 группы')
yes455 = KeyboardButton('Да я из 455 группы')
yes465 = KeyboardButton('Да я из 465 группы')
inline_wha115 = ReplyKeyboardMarkup().add(yes115, inline_no)
inline_wha125 = ReplyKeyboardMarkup().add(yes125, inline_no)
inline_wha135 = ReplyKeyboardMarkup().add(yes135, inline_no)
inline_wha155 = ReplyKeyboardMarkup().add(yes155, inline_no)
inline_wha165 = ReplyKeyboardMarkup().add(yes165, inline_no)

inline_wha215 = ReplyKeyboardMarkup().add(yes215, inline_no)
inline_wha225 = ReplyKeyboardMarkup().add(yes225, inline_no)
inline_wha235 = ReplyKeyboardMarkup().add(yes235, inline_no)
inline_wha255 = ReplyKeyboardMarkup().add(yes255, inline_no)
inline_wha265 = ReplyKeyboardMarkup().add(yes265, inline_no)

inline_wha315 = ReplyKeyboardMarkup().add(yes315, inline_no)
inline_wha325 = ReplyKeyboardMarkup().add(yes325, inline_no)
inline_wha335 = ReplyKeyboardMarkup().add(yes335, inline_no)
inline_wha355 = ReplyKeyboardMarkup().add(yes355, inline_no)
inline_wha365 = ReplyKeyboardMarkup().add(yes365, inline_no)

inline_wha415 = ReplyKeyboardMarkup().add(yes415, inline_no)
inline_wha425 = ReplyKeyboardMarkup().add(yes425, inline_no)
inline_wha435 = ReplyKeyboardMarkup().add(yes435, inline_no)
inline_wha455 = ReplyKeyboardMarkup().add(yes455, inline_no)
inline_wha465 = ReplyKeyboardMarkup().add(yes465, inline_no)





strostat = InlineKeyboardButton("Я староста",callback_data="i_starosta")
inline_star = InlineKeyboardMarkup().add(strostat)






butt1 = KeyboardButton('Расписание')
butt2 = KeyboardButton('Домашнее задание')
butt3 = KeyboardButton('/admin_help')
butt4 = KeyboardButton('/star_help')
butt5 = KeyboardButton("Обновить расписание")
admin_key = ReplyKeyboardMarkup(resize_keyboard=True).add(
    butt1, butt2).add(butt3, butt4).add(butt5)

bthmm = KeyboardButton("Расписание")
dz = KeyboardButton("Домашнее задание")

bthmm = KeyboardButton("Расписание")
rass_all = KeyboardButton("Разослать всем")
rass_my_gr = KeyboardButton("Разослать всем")
user_key = ReplyKeyboardMarkup(resize_keyboard=True).add(bthmm)#, dz)



new_shed115 = InlineKeyboardButton("115", callback_data='button115')
new_shed125 = InlineKeyboardButton("125", callback_data='button125')
new_shed135 = InlineKeyboardButton("135", callback_data='button135')
new_shed155 = InlineKeyboardButton("155", callback_data='button155')
new_shed165 = InlineKeyboardButton("165", callback_data='button165')
new_shed215 = InlineKeyboardButton("215", callback_data='button215')
new_shed225 = InlineKeyboardButton("225", callback_data='button225')
new_shed235 = InlineKeyboardButton("235", callback_data='button235')
new_shed255 = InlineKeyboardButton("255", callback_data='button255')
new_shed265 = InlineKeyboardButton("265", callback_data='button265')
new_shed315 = InlineKeyboardButton("315", callback_data='button315')
new_shed325 = InlineKeyboardButton("325", callback_data='button325')
new_shed335 = InlineKeyboardButton("335", callback_data='button335')
new_shed355 = InlineKeyboardButton("355", callback_data='button355')
new_shed365 = InlineKeyboardButton("365", callback_data='button365')
new_shed415 = InlineKeyboardButton("415", callback_data='button415')
new_shed425 = InlineKeyboardButton("425", callback_data='button425')
new_shed435 = InlineKeyboardButton("435", callback_data='button435')
new_shed455 = InlineKeyboardButton("455", callback_data='button455')
new_shed465 = InlineKeyboardButton("465", callback_data='button465')

#inline_btn_1 = InlineKeyboardButton('115', callback_data='button115')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
new_schedule_course1 = InlineKeyboardMarkup(resize_keyboard=True).add(new_shed115, new_shed125, new_shed135 ,new_shed155 ,new_shed165)
new_schedule_course2 = InlineKeyboardMarkup(resize_keyboard=True).add(new_shed215, new_shed225, new_shed235 ,new_shed255 ,new_shed265)
new_schedule_course3 = InlineKeyboardMarkup(resize_keyboard=True).add(new_shed315, new_shed325, new_shed335 ,new_shed355 ,new_shed365)
new_schedule_course4 = InlineKeyboardMarkup(resize_keyboard=True).add(new_shed415, new_shed425, new_shed435 ,new_shed455 ,new_shed465)
new_course1 = InlineKeyboardButton("1", callback_data='c1')
new_course2 = InlineKeyboardButton("2", callback_data='c2')
new_course3 = InlineKeyboardButton("3", callback_data='c3')
new_course4 = InlineKeyboardButton("4", callback_data='c4')
new_what_course = InlineKeyboardMarkup(resize_keyboard=True).add(new_course1, new_course2).add(new_course3 ,new_course4)
#admin_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(bthmm,dz).add(rass_all, rass_my_gr)
 