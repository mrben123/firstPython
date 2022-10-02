import re
import json
import os


def main(file_path):
    from os import path
    file_name = os.path.basename(file_path).split('.')[0]

    print(file_name.startswith("~$"))
    print(os.path.basename(file_path).split('.'))


main('./乡镇分配试剂-泰安.docx')