import pyexcel_ods3 as p
import json
import collections
from openpyxl.chart import BarChart, Reference

data = p.get_data("transactions.ods")

print(data)
print(type(data))

# json_data = json.dumps(data)
# print(json_data)

for k, v in data.items():
    print(v)
    print(type(v))

abc = data["Sheet1"]
print(f'\n abc is of type {type(abc)} ... \n')

# for a in abc:
#     print(a)

for row in range(1, len(abc)):
    cell = abc[row][2]
    print(cell)
    discounted_price = cell * 0.9
    print(discounted_price)


