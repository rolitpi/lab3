from second_task import load_second_task_doc
from first_task import load_first_task_doc

FIRST_FILE_NAME = '9-j4.xls'
SECOND_FILE_NAME = '9-127.xls'


def process() -> None:
    load_first_task_doc(FIRST_FILE_NAME)
    load_second_task_doc(SECOND_FILE_NAME)


if __name__ == '__main__':
    process()
