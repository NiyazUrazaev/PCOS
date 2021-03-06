from PCOS.api import (
    print_first_answer, print_second_answer, print_third_answer,
    print_fourth_answer, print_fifth_answer, print_sixth_answer, print_seventh_answer, print_eight_answer,
)


class User:
    reputation = 50
    quality = 0
    time = 100
    budget = 100

    def __str__(self):
        return 'Rep: ' + str(self.reputation) + ' Quality: ' + str(self.quality) + ' Time: ' + str(
            self.time) + ' Budget: ' + str(self.budget)

    def calculate_points(self, quality, budget, reputation, time):
        self.reputation += reputation
        self.quality += quality
        self.time += time
        self.budget += budget


class Question:

    def __init__(self, answers, text):
        self.answers = answers
        self.text = text

    def print_answers(self):
        for idx, ans in enumerate(self.answers):
            print('{} - {}'.format(idx + 1, ans))


q1 = Question(
    [
        'Сперва постараюсь быстро описать один бизнес-процесс и отправить его в разработку',
        'Сперва подготовлю большую часть процессов, а только потом отправлю к разработчикам',
    ],
    'Вы только что получили проект и пол года на его выполнение. Ваш ход действий?',
)

# Если вариант ответа был 1 в вопросе №1
q2 = Question(
    [
        'Постараться убедить его в корректности нашей реализации',
        'Сблефовать на тему некорректного заполнения тз и попробовать выбить доп финансирование и сроки',
        'Признать свою вину и выполнить доработки за свой счет',
    ],
    'Спустя месяц пришел заказчик проекта и ему не понравился реализованный бизнес-процесс.',
)

# Если вариант ответа был 2 в вопросе №!
q3 = Question(
    [
        'Попробовать договориться с заказчиком и выпросить доп финансирование',
        'Попробовать решить вопрос денег поиском новых проектов(вести параллельную работу)',
        'Начать экономить. Перестаем покупать импортные фрукты, дорогой кофе и тд',
    ],
    'Аналитика затянулась и вы понимаете, что денег не хватает для реализации проекта.',
)

# Если вариант ответа был 3 в вопросе №3
q4 = Question(
    [
        'Предложить повышения зп',
        'Попытаться выяснить причину и решить вопрос без повышений',
        'Согласиться с его решением. Ведь рано или поздно он все равно уйдет',
    ],
    'Внезапно из-за ухудшения условий к вам подходит разработчик и говорит о желании уволиться. Ваши действия?',
)

# Если вариант ответа был 2 в вопросе №3
q5 = Question(
    [
        'Извиниться и оставить все как есть',
        'Извиниться и попробовать выбить доп финансирование',
        'Извиниться и не афишируя о работе вести параллельно второй проект',
    ],
    'Ваши поиски оправдались, вы находите проект. Однако выясняется, что первый заказчик против того, '
    'чтобы мы вели параллельно с ним другие работы',
)

q6 = Question(
    [
        'Постараться избежать в нем участия, чтобы все закончилось само',
        'Вынести выговор и депремировать каждого участника конфликта',
        'Возьму ответственность в решении конфликта на себя',
    ],
    'Внезапомно происходит конфликт в команде, что будете делать?',
)

q7 = Question(
    [
        'Посмотрю по наибольшему числу коммитов',
        'Выберу человека с наилучшим значением отношения "Оценки задачи"/"Время выполнения"',
        'Выберу человека, который больше всех говорил на митингах',
    ],
    'В ходе выполнения проекта вы хотите выделить(премией) какого-то из разработчиков. Как вы будете решать кого?',
)

q8 = Question(
    [
        'У меня в команде будет тестировщик, который напишет автотесты и поможет при приемке задач',
        'У меня не будет тестировщика. Возложу эту ответственность на аналитиков',
    ],
    'Как бы вы поступили с тестами?',
)

user = User()

ans = print_first_answer(q1, user)
if ans == 1:
    print_second_answer(q2, user)
elif ans == 2:
    ans = print_third_answer(q3, user)
    if ans == 3:
        print_fourth_answer(q4, user)
    elif ans == 2:
        print_fifth_answer(q5, user)
print_sixth_answer(q6, user)
print_seventh_answer(q7, user)
print_eight_answer(q8, user)

print(user)
if user.quality >= 75 and user.time > 0 and user.reputation > 0 and user.budget > 0:
    print('Вы выиграли эту игру!!!')
else:
    print('Вы проиграли эту игру!!!')




