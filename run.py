# -*- coding: utf-8 -*-

from tools.parse_excel import *
from demo_requests.siyue_demo import new_request


execl = ParsExcel()
new_re = new_request()
sheet = execl.SheetName('测试数据')
new_re = new_request()
maxrow = execl.get_row(sheet)

for row in range(2, maxrow+1):
    corpus = execl.get_cell_value(sheet, row, 1)
    intention = execl.get_cell_value(sheet, row, 2)
    new_result = new_re.response_handle(new_re.response_get(corpus))

    print(str(row) + '\t' + new_result)
    execl.set_cell_value(sheet, row, 3, new_result)

    if new_result == intention:
        execl.right_cell_style(sheet, row, 3)
    else:
        execl.wrong_cell_style(sheet, row, 3)

execl.saveData()

