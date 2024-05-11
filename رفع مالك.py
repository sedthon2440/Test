import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters



#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###




@app.on_message(filters.command("رفع مالك", ""))
def promote_owner(client, message):
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
    tom_owners = load_tom_owners()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return
    if chat_id not in tom_owners['owners']:
        tom_owners['owners'][chat_id] = {'owner_id': []}

    if user_id in tom_owners['owners'][chat_id]['owner_id']:
        message.reply_text("""◍ هذا المستخدم مالك بالفعل
√""")
    else:
        tom_owners['owners'][chat_id]['owner_id'].append(user_id)
        dump_tom_owners(tom_owners)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مالك
√""")


@app.on_message(filters.command("تنزيل مالك", ""))
def demote_owner(client, message):
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

    tom_owners = load_tom_owners()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return
    if chat_id not in tom_owners['owners']:
        message.reply_text("لا يوجد مالكين في هذه الدردشة حتى الأن")
        return

    if user_id not in tom_owners['owners'][chat_id]['owner_id']:
        message.reply_text("""◍ هذا المستخدم ليس مالك لتنزيله
√""")
    else:
        tom_owners['owners'][chat_id]['owner_id'].remove(user_id)
        dump_tom_owners(tom_owners)
        message.reply_text("""◍ تم تنزيل المستخدم من المالكين بنجاح
√""")


@app.on_message(filters.command("مسح المالكين", ""))
def clear_owner(client, message):
    chat_id = str(message.chat.id)
    tom_owners = load_tom_owners()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return
    if chat_id in tom_owners['owners']:
        tom_owners['owners'][chat_id]['owner_id'] = []
        dump_tom_owners(tom_owners)
        message.reply_text("""◍ تم مسح المالكين بنجاح
√""")
    else:
        message.reply_text("لا يوجد مالكين ليتم مسحهم")





@app.on_message(filters.command("المالكين", ""))
def get_owner(client, message):
    chat_id = str(message.chat.id)
    tom_owners = load_tom_owners()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك على الاقل لستخدام الامر
√""")
        return
    if chat_id not in tom_owners['owners']:
        message.reply_text("لا يوجد مالكين حتى الأن")
        return

    admins = tom_owners['owners'][chat_id]['owner_id']
    if not admins:
        message.reply_text("لا يوجد مالكين حتى الأن")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المالكين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المالكين")



#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###