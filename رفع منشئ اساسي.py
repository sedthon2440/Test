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





@app.on_message(filters.command("رفع منشئ اساسي", ""))
def promote_basic_creator(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[3]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[2].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return
    tom_basic_creators = load_tom_basic_creators()

    if user_id in tom_basic_creators['basic_creators']:
        message.reply_text("""◍ هذا المستخدم منشئ اساسي بالفعل
√""")
    else:
        tom_basic_creators['basic_creators'][user_id] = True
        dump_tom_basic_creators(tom_basic_creators)
        message.reply_text("""◍ تم رفع المستخدم ليصبح منشئ اساسي
√""")



@app.on_message(filters.command("تنزيل منشئ اساسي", ""))
def demote_basic_creator(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[3]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[2].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return
        
    tom_basic_creators = load_tom_basic_creators()

    if user_id not in tom_basic_creators['basic_creators']:
        message.reply_text("""◍ هذا المستخدم ليس منشئ اساسي لتنزيله
√""")
    else:
        del tom_basic_creators['basic_creators'][user_id]
        dump_tom_basic_creators(tom_basic_creators)
        message.reply_text("""◍ تم تنزيل المستخدم من المنشئين الاساسيين بنجاح
√""")


@app.on_message(filters.command("المنشئين الاساسيين", ""))
def get_basic_creators(client, message):
    tom_basic_creators = load_tom_basic_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return

    if 'basic_creators' not in tom_basic_creators:
        message.reply_text("لا يوجد منشئين اساسيين حتى الأن")
        return

    basic_creators = tom_basic_creators['basic_creators']
    if not basic_creators:
        message.reply_text("لا يوجد منشئين اساسيين حتى الأن")
    else:
        creator_names = []
        for creator_id in basic_creators:
            user = app.get_users(int(creator_id))
            if user:
                creator_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if creator_names:
            creator_list = "\n".join(creator_names)
            message.reply_text(f"◍ قائمة المنشئين الاساسيين:\n\n{creator_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المنشئين الاساسيين")

@app.on_message(filters.command("مسح المنشئين الاساسيين", ""))
def clear_basic_creators(client, message):
    tom_basic_creators = load_tom_basic_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return

    if 'basic_creators' in tom_basic_creators:
        tom_basic_creators['basic_creators'] = {}
        dump_tom_basic_creators(tom_basic_creators)
        message.reply_text("""◍ تم مسح المنشئين الاساسيين بنجاح
√""")
    else:
        message.reply_text("لا يوجد منشئين اساسيين ليتم مسحهم")



#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###