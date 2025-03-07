import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = environ.get("START_TXT", '''𝐻𝑒𝑙𝑙𝑜 {},
𝑀𝑦 𝑁𝑎𝑚𝑒 𝐼𝑠 <a href=https://t.me/{}>{}</a>, 𝐼 𝐴𝑚 𝐴 𝑆𝑖𝑚𝑝𝑙𝑒 𝐴𝑢𝑡𝑜𝐹𝑖𝑙𝑡𝑒𝑟 𝐵𝑜𝑡, 𝐼 𝐶𝑎𝑛 𝑃𝑟𝑜𝑣𝑖𝑑𝑒 𝑀𝑜𝑣𝑖𝑒𝑠, 𝐽𝑢𝑠𝑡 𝑆𝑒𝑎𝑟𝑐ℎ 𝑌𝑜𝑢𝑟 𝑅𝑒𝑞𝑢𝑒𝑠𝑡𝑒𝑑 𝑀𝑜𝑣𝑖𝑒 𝑜𝑟 𝑆𝑒𝑟𝑖𝑒𝑠 𝑁𝑎𝑚𝑒 𝐴𝑛𝑑 𝐸𝑛𝑗𝑜𝑦 😍''')
    HELP_TXT = """𝙷𝙴𝚈 {}
𝐻𝐸𝑅𝐸 𝐼𝑆 𝑇𝐻𝐸 𝐻𝐸𝐿𝑃 𝐹𝑂𝑅 𝑀𝑌 𝐶𝑂𝑀𝑀𝐴𝑁𝐷𝑆."""
    ABOUT_TXT = """<b><i>🤖 𝖬ʏ 𝖭ᴀᴍᴇ : <a href=https://t.me/TGCWFilterbot><b>File Search Bot 𝐓𝐆𝐂𝐖⚡</b></a>\n
👨‍💻 𝖣ᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/VishnuMBbot>𝐕𝐢𝐬𝐡𝐧𝐮 𝐌𝐁</b></a>\n
📝 𝖫ᴀɴɢᴜᴀɢᴇ : P𝗒𝗍𝗁𝗈𝗇\n
📚 𝖥ʀᴀᴍᴇᴡᴏʀᴋ : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 3.10\n
📡 𝖧ᴏsᴛᴇᴅ ᴏɴ : 𝖯𝗋𝗂𝗏𝖺𝗍𝖾 𝖲𝖾𝗋𝗏𝖾𝗋\n
🌟 𝖵ᴇʀsɪᴏɴ : 𝖴𝗇𝖢𝗅𝖺𝗌𝗌𝗂𝖿𝗂𝖾𝖽😌 [ 𝙱𝙴𝚃𝙰 ]\n</b></i>"""
    SOURCE_TXT = """<b>𝐂𝐫𝐞𝐚𝐭𝐞 𝐎𝐧𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬:</b>
» I will Create One Bot For You<b>
» Contact Me @Vishnumbbot<b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/vishnumb14)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝖳𝖮𝖳𝖠𝖫 𝖥𝖨𝖫𝖤𝖲: <code>{}</code>
★ 𝖳𝖮𝖳𝖠𝖫 𝖴𝖲𝖤𝖱𝖲: <code>{}</code>
★ 𝖳𝖮𝖳𝖠𝖫 𝖢𝖧𝖠𝖳𝖲: <code>{}</code>
★ 𝖴𝖲𝖤𝖣 𝖲𝖳𝖮𝖱𝖠𝖦𝖤: <code>{}</code> 𝙼𝚒𝙱
★ 𝖥𝖱𝖤𝖤 𝖲𝖳𝖮𝖱𝖠𝖦𝖤: <code>{}</code> 𝙼𝚒𝙱"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>

Bʏ @TGCWFilterbot</b>"""   
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}

Bʏ @TGCWFilterbot</b>
"""
