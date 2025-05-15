import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import config
import random
bot = telebot.TeleBot(config.token)

quiz = [
    {"question": "1 - Вы человек?",
     "options": ["да", "нет", "Нет, я тостер"], "correct": "Нет, я тостер"},

    {"question": "2 - Откуда появисля мем -Ой мама пришла-?",
    "options": ["Из сериала по майнкрафту", "Из АГШ", "Да"], "correct": "Из АГШ"},

    {"question": "3 - Чем мы дышим?",
     "options": ["Цианистым калием ☺", "Пропаном", "Водой ☺", "Водородом", "Чем-то", "Воздухом"], "correct": "Воздухом"},

    {"question": "4 - Что такое BREATHEGE?",
     "options": ["Игра", "Фильм", "Серия игр"], "correct": "Серия игр"},

    {"question": "переход на стадию 2! (Сложность) 5 - Кто создал MINECRAFT",
     "options": ["Я", "Нотч", "Маркус Персон", "Майкрософт"], "correct": "Маркус Персон"},

    {"question": "6 - Как называется папка с проектом на моем ноуте?!",
     "options": ["Papochka", "pensil", "pk", "projekt", "sekretnije_fajli_pentagona"], "correct": "sekretnije_fajli_pentagona"},

    {"question": "7 - 2+2*2?",
     "options": ["8", "6", "2"], "correct": "6"},
     
    {"question": "8 - Откуда появисля мем -МАЙНКРАФТ МОЯ ЖИЗНЬ-?",
    "options": ["Из сериала по майнкрафту", "Из АГШ", "Да"], "correct": "Из АГШ"},

    {"question": "9 - Что мы едим?",
     "options": ["Крысинный яд", "Я веган, траву", "Веганов", "Импостеров", "Что-то", "Воздух"], "correct": "Веганов"},

    {"question": "переход на стадию 3! (Сложность) 10 - Что такое Алцгеймер?",
     "options": ["Что такое Альцгеймер?", "ЩТА", "Какойто геймер"], "correct": "Что такое Альцгеймер?"},

    {"question": "11 - Летели 2 верблюда, 1 рыжий, другой на лево, сколько весить чайная ложка Тролля-А, если Димончик пошол в первый класс в 699435883434858 лет?",
     "options": ["3 Огурца", "Банан", "ЧЕГО", "Майкрософт"], "correct": "3 Огурца"},

    {"question": "12 - Если январь равен 717, март равен 5315, а июнь равен 4624, то чему равен август? Ответьте здесь. Ли ехал, когда заметил, что его милометр показал 16961 и был одинаковым и вперед, и назад. Каким будет следующий миля, который также будет показывать одинаково и вперед, и назад?",
     "options": ["Хз", "зх", "69", "Гомункул", "1945", "Сталин", "Июль", "Чего", "Жить или не жить? Вот в чем вопрос"], "correct": "Сталин"},

    {"question": "13 - Они не будут нагонять тоску, наводить на мысль о катастрофах, напоминать о густых туманах и музыке Вагнера. Они будут заостренными на концах, империалистическими, сверхреалистическими, обращенными к небу, подобно вертикальному мистицизму, подобно вертикальным испанским синдикатам, словно башни Бургосского собора, всегда обращены в небо». О чем говорил Сальвадор Дали?",
        "options": ["О ракетах", "О своих усах", "О бегствии", "Я чё знаю"], "correct": "О своих усах"},

    {"question": "14 - Гомер, желая вознести хвалу одному из самых великих своих героев, вместо того чтобы сравнивать его со львом, пантерой или, скажем, кабаном, проводит параллели между неустрашимостью и постоянством своего великого героя и ею. Она никогда не оставит своей добычи, но непременно вернется к ней не один раз, пока не насладится ей полностью. О ком или о чем это Гомер?",
        "options": ["О кошке", "О еде", "О мухе"], "correct": "О мухе"},

    {"question": "переход на стадию 4! (Сложность)15 - В Венском естественно-историческом музее сохранилась таблица, датированная XVII веком — «Краткое описание народов, пребывающих в Европе, и их свойства». В графе «основное времяпрепровождение» напротив поляков написано «распри», напротив венгров — «ходить в гости», напротив англичан — «работа», напротив французов — «обман». А что являлось основным времяпрепровождением русских согласно таблице?",
        "options": ["Мыться в бане", "Сон", "Карта"], "correct": "Сон"},
]

user_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_state[chat_id] = {"score": 0, "question_index": 0}
    bot.send_message(chat_id, "Привет! Давай проверим твою адекватность. Если у тебя баллов больше 5, поздровляю, вам нужно провериться у специалиста. Вот первый вопрос:")
    send_question(chat_id)

def send_question(chat_id):
    index = user_state[chat_id]["question_index"]
    
    if index < len(quiz):
        q = quiz[index]
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for option in q["options"]:
            markup.add(KeyboardButton(option))
        bot.send_message(chat_id, q["question"], reply_markup=markup)
    else:
        score = user_state[chat_id]["score"]
        bot.send_message(chat_id, f"Тест окончен! Ты набрал {score} баллов, если это число больше 5, поздровляю, вам надо проверится у специалиста")
        del user_state[chat_id]


@bot.message_handler(func=lambda message: message.chat.id in user_state)
def check_answer(message):
    chat_id = message.chat.id
    index = user_state[chat_id]["question_index"]
    correct_answer = quiz[index]["correct"]

    if message.text == correct_answer:
        bot.send_message(chat_id, "Пон")
        user_state[chat_id]["score"] += 1
    else:
        bot.send_message(chat_id, f"Не пон. Пон = {correct_answer}")

    user_state[chat_id]["question_index"] += 1
    send_question(chat_id)


bot.polling()
