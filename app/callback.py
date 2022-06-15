def callback_worker(call, bot):
    if call.text == "Добавить дело в список":
        msg = bot.send_message(call.chat.id, 'Давайте добавим дело! Напишите его в чат')
        # bot.register_next_step_handler(msg, add_plan)

    elif call.text == "Показать список дел":
        try:
            show_plans(call)
        except:
            bot.send_message(call.chat.id, 'Здесь пусто. Можно отдыхать :-)')
            send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Удалить дело из списка":
        try:
            delete_one_plan(call)
        except:
            bot.send_message(call.chat.id, 'Здесь пусто. Можно отдыхать :-)')
            send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Удалить все дела из списка":
        try:
            delete_all_plans(call)
        except:
            bot.send_message(call.chat.id, 'Здесь пусто. Можно отдыхать :-)')
            send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Другое":
        bot.send_message(call.chat.id, 'Больше я пока ничего не умею :-(')
        send_keyboard(call, "Чем еще могу помочь?")

    elif call.text == "Пока все!":
        bot.send_message(call.chat.id, 'Хорошего дня! Когда захотите продолжнить нажмите на команду /start')