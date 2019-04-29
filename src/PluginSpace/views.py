import random
import json
import time

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def plugin_space_index(request):
    return render(request, 'index.html')


def datetimepicker_demo_idx(request, demo_idx=1):
    html = 'datetimepicker/demo_%d.html' % (demo_idx)
    return render(request, html, {"demo_idx": demo_idx})


def echarts_demo_idx(request, demo_idx=1):
    html = 'echarts/demo_%d.html' % (demo_idx)
    return render(request, html, {"demo_idx": demo_idx})


def highcharts_demo_idx(request, demo_idx=1):
    html = 'highcharts/demo_%d.html' % (demo_idx)
    return render(request, html, {"demo_idx": demo_idx})


def droppable_demo_01(request):
    return render(request, 'droppable/demo_1.html')

def droppable_demo_02(request):
    return render(request, 'droppable/demo_02.html')

def droppable_demo_03(request):
    return render(request, 'droppable/demo_03.html')

def droppable_demo_04(request):
    return render(request, 'droppable/demo_04.html')

def droppable_demo_05(request):
    return render(request, 'droppable/demo_05.html')

def droppable_demo_06(request):
    return render(request, 'droppable/demo_06.html')

def droppable_demo_07(request):
    return render(request, 'droppable/demo_07.html')

def draggable_demo_01(request):
    return render(request, 'draggable/demo_1.html')

def draggable_demo_02(request):
    return render(request, 'draggable/demo_02.html')

def draggable_demo_03(request):
    return render(request, 'draggable/demo_03.html')

def draggable_demo_04(request):
    return render(request, 'draggable/demo_04.html')

def draggable_demo_05(request):
    return render(request, 'draggable/demo_05.html')

def draggable_demo_06(request):
    return render(request, 'draggable/demo_06.html')

def draggable_demo_07(request):
    return render(request, 'draggable/demo_07.html')

def draggable_demo_08(request):
    return render(request, 'draggable/demo_08.html')

def draggable_demo_09(request):
    return render(request, 'draggable/demo_09.html')

def draggable_demo_10(request):
    return render(request, 'draggable/demo_10.html')

def draggable_demo_11(request):
    return render(request, 'draggable/demo_11.html')

def datatable_learn01(request):
    return render(request, 'datatables/learn01.html')

def datatable_learn02(request):
    table_head = ['姓名', '性别', '角色', '全年', '月均',
                  'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.',
                  'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    return render(request, 'datatables/learn02.html', {'table_head': table_head})

def datatable_learn03(request):
    table_head = ['姓名', '性别', '角色', '全年', '月均',
                  'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.',
                  'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    return render(request, 'datatables/learn03.html', {'table_head': table_head})

def datatable_learn04(request):
    table_head = ['姓名', '性别', '角色', '全年', '月均',
                  'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.',
                  'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    return render(request, 'datatables/learn04.html', {'table_head': table_head})


def datatable_learn05(request):
    return render(request, 'datatables/learn05.html')


def datatable_learn05_data(request):
    old_versions = ['18A', '19A', '19B', '20A', '20B']
    user_sn_list = ['lwx372241', 'cwx665544', 'zwx123456', 'swx346521', 'wwx768932']
    user_name_list = ['系统同步更新', '李四', '蔡丽', '张三', '孙六', '王五']
    status_list = ['未确认', '已确认', '已合入', '未合入', '无需合入']
    reason_list = ['', '备注一', '备注二', '备注三', '备注四']
    data = []
    for i in range(105):
        mr = {}
        num = random.randint(0, 4)
        mr['mr_id'] = i + random.randint(0, 3500)
        mr['mr_url'] = 'http://www.datatables.club/reference/option/'
        mr['mr_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        mr['old_version'] = old_versions[num]
        mr['project_path'] = 'BTS/WN_5G'
        mr['user_sn'] = user_sn_list[num]
        mr['user_name'] = user_name_list[num]
        mr['status_update_user'] = user_name_list[num]
        mr['status_update_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        mr['status'] = status_list[num]
        mr['reason'] = reason_list[num]

        data.append(mr)

    return HttpResponse(json.dumps({"data": data}))


def datatable_demo_06(request):
    return render(request, 'datatables/demo_06.html')


def datatable_demo_07(request):
    return render(request, 'datatables/demo_07.html')


def datatable_demo_08(request):
    return render(request, 'datatables/demo_08.html')


def datatable_demo_09(request):
    return render(request, 'datatables/demo_09.html')


def datatable_demo_10(request):
    return render(request, 'datatables/demo_10.html')


def dt_demo_06_logs(request):

    user_sn_list = ['lwx372241', 'cwx665544', 'zwx123456', 'swx346521', 'wwx768932']
    user_name_list = ['系统同步更新', '李四', '蔡丽', '张三', '孙六', '王五']
    status_list = ['未确认', '已确认', '已合入', '未合入', '无需合入']
    reason_list = ['', '备注一,....', '备注二,....', '备注三,....', '备注四,....']
    logs = []
    for i in range(10):
        num = random.randint(0, 4)
        item = {}
        item["modify_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        item["modify_user_sn"] = user_sn_list[num]
        item["modify_user_name"] = user_name_list[num]
        item["modify_status"] = status_list[num]
        item["modify_reason"] = reason_list[num]
        logs.append(item)
    return HttpResponse(json.dumps({"logs": logs, "code": 200}))

def datatable_data_year(request):
    names = ['Abbie', 'Joe', 'Darwin', 'Eilian', 'David', 'Ken', 'Joseph', 'Duke', 'Eric', 'Luke', 'Evan',
             'Denny', 'Johnny', 'Joe', 'Leo', 'Benjamin', 'Alysa', 'Gary', 'Mark', 'Michael', 'Blake', 'George',
             'Acacia', 'Adalia', 'Lawrence', 'Azura', 'Benson', 'Billy', 'Brown', 'Hank', 'Glen', 'Mike', 'Nicholas',
             'Adelaide', 'Ray', 'Jason', 'Antonia', 'Jeffery', 'Aurora', 'Charles', 'Cameron', 'Howard', 'Robinson', 'Norman',
             'Amber', 'James', 'Adonia', 'James', 'Cecil', 'Jeffery', 'Christian', 'Akili', 'Harry', 'Quentin', 'Owen']
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




def multiselect_learn01(request):
    roles = [
        {'id': -1, 'name': 'LM'}, {'id': 0, 'name': 'PM'}, {'id': 1, 'name': 'SE'}, {'id': 2, 'name': 'MDE'},
        {'id': 3, 'name': 'DEVELOPER'}, {'id': 4, 'name': 'TEST'}
    ]
    return render(request, 'multiselect/learn01.html', {'roles': roles})