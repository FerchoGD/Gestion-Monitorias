from django import template
register = template.Library()

@register.filter(name='hour_in_slots_fun')
def hour_in_slots_fun(hour, slots):
    return hour in slots

@register.filter(name='hour_in_slots_duple')
def hour_in_slots_fun_duple(hour, slots):
    slots = [slot[0] for slot in slots]
    return hour in slots

@register.filter(name='get_id_from_duple')
def get_id_from_duple(hour, slots):
    id_slot = 0
    for slot in slots:
        if hour == slot[0]:
            id_slot = slot[1]
            break
    return id_slot

@register.filter(name='concat')
def concat(arg1, arg2):
    return '%s-%s' % (arg1, arg2)
