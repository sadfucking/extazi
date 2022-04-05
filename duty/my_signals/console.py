from duty.objects import dp, MySignalEvent
import subprocess, os, sys, math, psutil, time
#run
@dp.longpoll_event_register('к')
@dp.my_signal_event_register('к')
def run(event: MySignalEvent) -> str:
    try:
        if event.args[0] == 'помощь':
            event.msg_op(2, 'тут будет список команд')
        else:
            ct=subprocess.run([*event.args], capture_output=True)
            event.msg_op(2, str(ct).replace("b", "").replace("'", "").replace("\\n", "\n"))
    except:
        event.msg_op(2, 'arguments entered incorrectly')
    return "ok"

#subprocess.popen

@dp.longpoll_event_register('popen')
@dp.my_signal_event_register('popen')
def popen(event: MySignalEvent) -> str:
    try:
        proc = subprocess.Popen([*event.args], stdout=subprocess.PIPE)
        output = proc.stdout.read().decode('utf-8')
        if event.args[0]=='git':
            event.msg_op(2, "✅️")
            event.msg_op(3)
        if event.args[0]=='rm':
            name=event.args[2]
            event.msg_op(2, f"{name}, удалено")
            event.msg_op(3)
        else:
            event.msg_op(2, output)
    except:
        event.msg(2, "недопустимая команда")
    return "ok"

#exec

@dp.longpoll_event_register('ех')
@dp.my_signal_event_register('ех')
def ex(event:MySignalEvent) -> str:
    reply=event.reply_message['text']
    cm=exec(reply)
    event.msg_op(1, cm)
    return "ok"

#eval

@dp.longpoll_event_register('евал')
@dp.my_signal_event_register('евал')
def evl(event:MySignalEvent) -> str:
    evl=eval(*event.args)
    event.msg_op(2, str(evl))
    if event.args[0]=='помощь':
        event.msg_op(2,"""
квадратный корень - math.sqrt()
логарифм - math.log()
+-/* - math.ceil()
""")
    return "ok"

@dp.longpoll_event_register('цпу')
@dp.my_signal_event_register('цпу')
def ps(event: MySignalEvent) -> str:
    cr=psutil.cpu_percent()
    event.msg_op(2, ('cpu: ') + f'{cr}' + ('%'))
    return "ok"
