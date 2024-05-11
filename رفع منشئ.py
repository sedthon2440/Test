import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters

@app.on_message(filters.command("رفع منشئ", ""))
def promote_creator(client, message):
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
    tom_creators = load_tom_creators()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك حتى تستطيع رفع منشئ
√""")
        return
    if chat_id not in tom_creators['creators']:
        tom_creators['creators'][chat_id] = {'creator_id': []}

    if user_id in tom_creators['creators'][chat_id]['creator_id']:
        message.reply_text("""◍ هذا المستخدم منشئ بالفعل
√""")
    else:
        tom_creators['creators'][chat_id]['creator_id'].append(user_id)
        dump_tom_creators(tom_creators)
        message.reply_text("""◍ تم رفع المستخدم ليصبح منشئ
√""")




@app.on_message(filters.command("تنزيل منشئ", ""))
def demote_creator(client, message):
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
    
    tom_creators = load_tom_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك حتى تستطيع تنزيل منشئ
√""")
        return
    if chat_id not in tom_creators['creators']:
        message.reply_text("لا يوجد منشئين حتى الأن")
        return

    if user_id not in tom_creators['creators'][chat_id]['creator_id']:
        message.reply_text("""◍ هذا المستخدم ليس منشئ لتنزيله
√""")
    else:
        tom_creators['creators'][chat_id]['creator_id'].remove(user_id)
        dump_tom_creators(tom_creators)
        message.reply_text("""◍ تم تنزيل المستخدم من المنشئين بنجاح
√""")



@app.on_message(filters.command("مسح المنشئين", ""))
def clear_creators(client, message):
    chat_id = str(message.chat.id)
    tom_creators = load_tom_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك حتى تستطيع حذف المنشئين
√""")
        return
    if chat_id in tom_creators['creators']:
        tom_creators['creators'][chat_id]['creator_id'] = []
        dump_tom_creators(tom_creators)
        message.reply_text("""◍ تم حذف المنشئين
√""")
    else:
        message.reply_text("""◍ لا يوجد منشئين
√""")






@app.on_message(filters.command("المنشئين", ""))
def get_creators(client, message):
    chat_id = str(message.chat.id)
    tom_creators = load_tom_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لستخدام الامر
√""")
        return
    if chat_id not in tom_creators['creators']:
        message.reply_text("""◍ لا يوجد منشئين
√""")
        return
    admins = tom_creators['creators'][chat_id]['creator_id']
    if not admins:
        message.reply_text("""◍ لا يوجد منشئين
√""")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        
        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المنشئين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المنشئين")





#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###