import random


def generate_luck(user_reputation):
    random_digit = random.randint(0, 100)

    return random_digit <= user_reputation


def before_print_decorator(print_ans_function):
    def wrapper(q, user):
        print(user)
        print(q.text)
        q.print_answers()
        return print_ans_function(q, user)

    return wrapper


@before_print_decorator
def print_first_answer(q1, user):
    lucky_flag = generate_luck(user.reputation)
    ans = int(input())
    if ans == 1:
        user.calculate_points(
            30 if lucky_flag else -5,
            -30 if lucky_flag else -50,
            0,
            -20 if lucky_flag else -40,
        )
    elif ans == 2:
        user.calculate_points(
            40, -60, 0,
            -50 if lucky_flag else -60,
        )

    return ans


@before_print_decorator
def print_second_answer(q2, user):
    ans = int(input())
    lucky_flag = generate_luck(user.reputation)

    if ans == 1:
        user.calculate_points(
            10 if lucky_flag else -10,
            0 if lucky_flag else -30,
            5 if lucky_flag else -10,
            0 if lucky_flag else -20,
        )
    elif ans == 2:
        user.calculate_points(
            0 if lucky_flag else -10,
            -30 if lucky_flag else 20,
            -10 if lucky_flag else 5,
            -20 if lucky_flag else 10,
        )
    elif ans == 3:
        user.calculate_points(
            -5, -30, 10, -20,
        )


@before_print_decorator
def print_third_answer(q3, user):
    ans = int(input())
    lucky_flag = generate_luck(user.reputation)

    if ans == 1:
        user.calculate_points(
            0,
            25 if lucky_flag else 5,
            0 if lucky_flag else -5,
            0,
        )
    elif ans == 2:
        user.calculate_points(
            0, 0, 0, -5,
        )
    elif ans == 3:
        user.calculate_points(
            0, 5, -5, 0,
        )

    return ans


@before_print_decorator
def print_fourth_answer(q4, user):
    ans = int(input())
    lucky_flag = generate_luck(user.reputation)

    if ans == 1:
        user.calculate_points(
            0, -10, 5, 0,
        )
    elif ans == 2:
        user.calculate_points(
            0 if lucky_flag else -5,
            0,
            5 if lucky_flag else 0,
            0 if lucky_flag else -5,
        )
    elif ans == 3:
        user.calculate_points(
            -5, -20, 0, -5,
        )


@before_print_decorator
def print_fifth_answer(q5, user):
    ans = int(input())
    lucky_flag = generate_luck(user.reputation)

    if ans == 1:
        user.calculate_points(
            0, 0, 0, 0,
        )
    elif ans == 2:
        user.calculate_points(
            0,
            10 if lucky_flag else 0,
            0 if lucky_flag else -10,
            0,
        )
    elif ans == 3:
        user.calculate_points(
            -10, 20, -10, -10,
        )


@before_print_decorator
def print_sixth_answer(q6, user):
    ans = int(input())
    lucky_flag = generate_luck(user.reputation)

    if ans == 1:
        user.calculate_points(
            0, 0, 0, 0,
        )
    elif ans == 2:
        user.calculate_points(
            0, 10, -5, 0,
        )
    elif ans == 3:
        user.calculate_points(
            0,
            5 if lucky_flag else 0,
            10 if lucky_flag else -5,
            0,
        )

#     def calculate_points(self, quality, budget, reputation, time):

@before_print_decorator
def print_seventh_answer(q7, user):
    ans = int(input())

    if ans == 1:
        user.calculate_points(
            -5, -5, -5, 0,
        )
    elif ans == 2:
        user.calculate_points(
            5, -5, 5, 0,
        )
    elif ans == 3:
        user.calculate_points(
            -5, -5, -5, 0,
        )


@before_print_decorator
def print_eight_answer(q8, user):
    ans = int(input())

    if ans == 1:
        user.calculate_points(
            30, -15, 5, -5,
        )
    elif ans == 2:
        user.calculate_points(
            -5, 0, -5, 0,
        )