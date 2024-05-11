import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters


@app.on_message(filters.command("رفع ثانوي", ""))
def promote_basic_dev(client, message):
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

    tom_basic_devs = load_tom_basic_devs()

    if (not TOM(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply("""◍ انت لست المطور الاساسي
√""")
    elif user_id in tom_basic_devs['basic_devs']:
        message.reply_text("""◍ هذا المستخدم مطور ثانوي بالفعل
√""")
    else:
        tom_basic_devs['basic_devs'][user_id] = True
        dump_tom_basic_devs(tom_basic_devs)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مطور ثانوي
√""")





@app.on_message(filters.command("الثانويين", ""))
def list_basic_devs(client, message):
    tom_basic_devs = load_tom_basic_devs()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply("""◍ انت لست المطور الثانوي
√""")
        return

    basic_devs = tom_basic_devs['basic_devs']
    if not basic_devs:
        message.reply_text("لا يوجد مطورين ثانويين")
    else:
        basic_dev_names = []
        for basic_dev_id in basic_devs:
            user = app.get_users(int(basic_dev_id))
            if user:
                basic_dev_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if basic_dev_names:
            basic_dev_list = "\n".join(basic_dev_names)
            message.reply_text(f"◍ قائمة الثانويين:\n\n{basic_dev_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المطورين الثانويين")


@app.on_message(filters.command("تنزيل ثانوي", ""))
def demote_basic_dev(client, message):
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

    tom_basic_devs = load_tom_basic_devs()
    if (not TOM(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الاساسي
√""")
        return

    if user_id not in tom_basic_devs['basic_devs']:
        message.reply_text("""◍ هذا المستخدم ليس ثانويا لتنزيله
√""")
    else:
        del tom_basic_devs['basic_devs'][user_id]
        dump_tom_basic_devs(tom_basic_devs)
        message.reply_text("""◍ تم تنزيل المستخدم من الثانويين بنجاح
√""")


@app.on_message(filters.command("مسح الثانويين", ""))
def clear_basic_devs(client, message):
    tom_basic_devs = load_tom_basic_devs()
    if (not TOM(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الاساسي
√""")
        return
    if 'basic_devs' in tom_basic_devs:
        tom_basic_devs['basic_devs'] = {}
        dump_tom_basic_devs(tom_basic_devs)
        message.reply_text("""◍ تم مسح الثانويين بنجاح
√""")
    else:
        message.reply_text("لا يوجد ثانويين ليتم مسحهم")


#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###