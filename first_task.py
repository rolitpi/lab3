import math

import pandas as pd
import matplotlib.pyplot as plt

MILES_BETWEEN_DIAGNOSIS = 20_000
MILES_BETWEEN_OVERHAUL = 100_000


def load_first_task_doc(file_name: str):
    print('     Первая задача: ')
    excel_file = pd.ExcelFile(file_name)
    df = excel_file.parse(0)

    renamed_df = df.set_axis(range(df.count(axis='columns')[1]), axis=1, copy=True)
    cropped_df_sum = renamed_df[:-1].drop(0, axis=1).sum()
    all_infos_row = renamed_df.transpose()[31]

    miles_from_last_diagnosis = all_infos_row.apply(lambda x: x % MILES_BETWEEN_DIAGNOSIS)
    miles_from_last_overhaul = all_infos_row.apply(lambda x: x % MILES_BETWEEN_OVERHAUL)

    print('Количество диагностик в августе:')
    new_diagnosis_count = (miles_from_last_diagnosis + cropped_df_sum)[1:]\
        .apply(lambda x: math.floor(x / MILES_BETWEEN_DIAGNOSIS))
    print(new_diagnosis_count.sum())
    print('Количество диагностик для каждого борта:')
    print(new_diagnosis_count)

    print('Количество капитальных ремонтов в августе:')
    new_overhaul_count = (miles_from_last_overhaul + cropped_df_sum)[1:]\
        .apply(lambda x: math.floor(x / MILES_BETWEEN_OVERHAUL))
    print(new_overhaul_count.sum())
    print('Количество капитальных ремонтов для каждого борта:')
    print(new_overhaul_count)
