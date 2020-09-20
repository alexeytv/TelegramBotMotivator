from event import Event

hello_string = \
'''Здравствуй, мой дорогой друг! Я - твой личный мотиватор!
Ты можешь составить себе расписание дня, а я буду тебе переодически напоминать 
соблюдать его. Команды по составлению можешь посмотреть, введя "/help"'''
help_string = \
'''/start - приветствие;
/show_events - посмотреть расписание;
/add_event - добавить пункт в распорядок;
/del_event - удалить пункт из распорядка;
/edit_event - изменить пункт в распорядке;
/help - список команд.'''

show_events = \
'''Ниже представлен весь твой распорядок дня:'''
show_nothing = \
'''Ты пока еще не внес мероприятия в свой распорядок. Ты можешь сделать это командой /add_event'''

insert_string = \
'''Добавим новую запись в твое расписание...'''
ask_event = \
'''Введи название мероприятия:'''
ask_time = \
'''Введи время мероприятия в формате <hh:mm-hh:mm> :'''
entered_time_error = \
'''Строка не соответствует требуемому формату. Попробуй ещё раз!'''

event_added = \
'''Поздравляю! Строка успешно добавлена!'''
del_string = \
'''Удалим запись из твоего расписания...'''
ask_del_number = \
'''Введи порядковый номер мероприятия на удаление:'''
event_deleted = \
'''Мероприятие успешно удалено из твоего распорядка!'''

edit_string = \
'''Изменим запись в твоем распорядке...'''
ask_edit_number = \
'''Введи порядковый номер мероприятия для изменения:'''
ask_edit_name = \
'''Введи новое название мероприятия:'''

shedule1 = \
'''1. История в 533
2. Английский в 533
3. Русский в 533
4. Литература в 533
5. История в 538
6. Немецкий в 533
7. Физ-ра'''

def make_event_message(event_list):
    result = '\n'.join(event.name for event in event_list)
    return result
