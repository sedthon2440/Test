import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters



@app.on_message(filters.command("رفع مميز", ""))
def promote_distinct(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_id = str(message.chat.id)
    tom_distinct = load_tom_distinct()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message) and not admin(client, message, message)):
        message.reply_text("""◍ يجب ان تكون ادمن على الاقل لكى تستطيع رفع مميز
√""")
        return

    if chat_id not in tom_distinct['admin']:
        tom_distinct['admin'][chat_id] = {'admin_id': []}

    if user_id in tom_distinct['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم مميز بالفعل
√""")
    else:
        tom_distinct['admin'][chat_id]['admin_id'].append(user_id)
        dump_tom_distinct(tom_distinct)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مميز
√""")


@app.on_message(filters.command("تنزيل مميز", ""))
def demote_distinct(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_id = str(message.chat.id)

    tom_distinct = load_tom_distinct()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message) and not admin(client, message, message)):
        message.reply_text("""◍ يجب ان تكون ادمن على الاقل لكى تستطيع تنزيل مميز
√""")
        return
    if chat_id not in tom_distinct['admin']:
        message.reply_text("لا يوجد مميزين حتى الأن")
        return

    if user_id not in tom_distinct['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم ليس مميز لتنزيله
√""")
    else:
        tom_distinct['admin'][chat_id]['admin_id'].remove(user_id)
        dump_tom_distinct(tom_distinct)
        message.reply_text("""◍ تم تنزيل المستخدم من المميزين بنجاح
√""")


@app.on_message(filters.command("مسح المميزين", ""))
def clear_distinct(client, message):
    chat_id = str(message.chat.id)
    tom_distinct = load_tom_distinct()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message) and not admin(client, message, message)):
        message.reply_text("""◍ يجب ان تكون ادمن على الاقل لكى تستطيع استخدام الأمر
√""")
        return

    if chat_id in tom_distinct['admin']:
        tom_distinct['admin'][chat_id]['admin_id'] = []
        dump_tom_distinct(tom_distinct)
        message.reply_text("""◍ تم مسح المميزين بنجاح
√""")
    else:
        message.reply_text("لا يوجد مميزين ليتم مسحهم")


@app.on_message(filters.command("المميزين", ""))
def get_distinct(client, message):
    chat_id = str(message.chat.id)
    tom_distinct = load_tom_distinct()

    if chat_id not in tom_distinct['admin']:
        message.reply_text("لا يوجد مميزين في هذه الدردشة")
        return

    admins = tom_distinct['admin'][chat_id]['admin_id']
    if not admins:
        message.reply_text("لا يوجد مميزين في هذه الدردشة")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المميزين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المميزين")