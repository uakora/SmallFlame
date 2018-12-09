import random
import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def plugin_space_index(request):
    return render(request, 'index.html')

def datatable_learn01(request):
    return render(request, 'datatables/learn01.html')

def datatable_learn02(request):
    table_head = ['姓名', '性别', '角色', '全年', '月均',
                  'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.',
                  'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    return render(request, 'datatables/learn02.html', {'table_head': table_head})
def datatable_learn02_data(request):
    names = ['Abbie', 'Acacia', 'Adalia', 'Adelaide', 'Adonia', 'Amber', 'Antonia', 'Aurora', 'Azura', 'Alysa', 'Akili',
             'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie',
             'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie',
             'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie',
             'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie', 'Abbie']
    sex_enum = ['男', '女']
    role_enum = ['LM', 'PL', 'SE', 'MDE', 'DEVELOPER', 'TEST']
    month_enum = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    data = []
    for name in names:
        code_enum = []
        year_total = 0
        for i in range(len(month_enum)):
            month_code = random.randint(0, 3500)
            code_enum.append(month_code)
            year_total += month_code
        month_avg = year_total//len(month_enum)
        item = {}
        item['name'] = name
        item['sex'] = sex_enum[random.randint(0, 1)]
        item['role'] = role_enum[random.randint(0, 5)]
        item['year_total'] = year_total
        item['month_avg'] = month_avg
        item['code_enum'] = code_enum

        data.append(item)
    return HttpResponse(json.dumps({'data': data}))

def datatable_learn03(request):
    return render(request, 'datatables/learn03.html')