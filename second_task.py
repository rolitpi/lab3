import math

import pandas as pd
from enum import Flag, auto


class TaskAnswer(Flag):
    NO_SOLUTIONS = auto()
    ONE_WHOLE_ROOT = auto()
    ONE_ROOT = auto()
    TWO_WHOLE_ROOTS = auto()
    TWO_ROOTS = auto()


def load_second_task_doc(file_name: str):
    print('     Вторая задача: ')
    excel_file = pd.ExcelFile(file_name)
    df = excel_file.parse(0)
    df = df.set_axis(['0', '1', '2'], axis=1, copy=True)
    df['3'] = df.transpose().apply(lambda x: solve(x['0'], x['1'], x['2']))
    print(df['3'].value_counts())


def solve(a, b, c) -> TaskAnswer:
    double_a = a * 2
    discr = b ** 2 - 2 * double_a * c
    if discr < 0:
        # нет корней
        return TaskAnswer.NO_SOLUTIONS
    if discr == 0:
        # один кратный корень, нужно проверить на целость
        return TaskAnswer.ONE_WHOLE_ROOT if (-b / double_a).is_integer() else TaskAnswer.ONE_ROOT

    discr_sqrt = math.sqrt(discr)
    # два корня, нужно проверить на целость
    x1 = ((-b + discr_sqrt) / double_a).is_integer()
    x2 = ((-b - discr_sqrt) / double_a).is_integer()
    return TaskAnswer.TWO_ROOTS | (TaskAnswer.TWO_WHOLE_ROOTS
                                   if x1 and x2 else TaskAnswer.ONE_WHOLE_ROOT if x1 or x2 else TaskAnswer.TWO_ROOTS)
