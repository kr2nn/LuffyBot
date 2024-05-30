from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
𝐇𝐄𝐋𝐋𝐎 {} 😍👋,
𝗦𝗲𝗹𝗲𝗰𝘁 𝗧𝗵𝗲 𝗚𝗥𝗢𝗨𝗣 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧🌺‼️

__**നിങ്ങൾക് ഇഷ്ടമുള്ള ഗ്രുപ്പ് select ചെയ്യുക.!!!**__
"""
    DETAILS_TEXT = """
**Hello {} 🫦
 
» രോമാഞ്ചം പ്രീമിയം 🔕

✅ • Daily Videos Updated
✅ • iOS supported
✅ • Full Direct Videos
✅ • Rare Collections & Hot Collections
✅ • Mallu aunty, Girls, etc… available 


🔞Many More Features 👍🏻

Price: 100

Click Pay Button, Pay The Amount And JOIN 🫦**
"""
    ABOUT_TEXT = """
**Mʏ ɴᴀᴍᴇ** : [ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ ᴠ4](https://t.me/UploadLinkToFileBot)

**Sᴏᴜʀᴄᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/LISA-KOREA/UPLOADER-BOT-V4)

**Dᴀᴛᴀʙᴀsᴇ** : [MᴏɴɢᴏDB](https://cloud.mongodb.com)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.12.3](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [ᴘʏʀᴏɢᴀᴍ 2.0.106](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** @Luffy
"""
    INFO_TXT = """<i>
<u>Yᴏᴜʀ Dᴇᴛᴀɪʟꜱ</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc}</code>
○ First Name : <code>{n}<code>
○ UserName : @{u}
○ link : <code>https://t.me/{u}</code>

Thank You For Using Me❣️</i>"""

    INVITE_TEXT = "**INVITE YOUR FRIENDS 🫶**"

    QR_TEXT = """
    **Pᴀʏ Aɴᴅ Sᴇɴᴅ Sᴄʀᴇᴇɴꜱʜᴏᴛ** 

    **പേയ്‌മെന്റ് ചെയ്യുക എന്നിട്ട് screenshot ഇതിലേക്ക് അയക്കുക 

ചെയ്യാൻ അറിയില്ലെങ്കിൽ @Luffy0000007 ഇതിൽ മെസ്സേജ് അയക്കുക 🤲
    

Dɪʀᴇᴄᴛ Pᴀʏ:** t.me/Luffy0000007
    """

    PROGRESS = """
🏎️ Sᴘᴇᴇᴅ : {3}/s\n\n
✅ Dᴏɴᴇ : {1}\n\n
🟰 Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""

    PIC = "https://telegra.ph/file/72b1efaa44944d2b9e1b9.jpg"

    PAYMENT_QR = "https://telegra.ph/file/4acfd5a112e10ba0bf34f.jpg"
    
    START_BUTTONS = InlineKeyboardMarkup(
        [[  
        InlineKeyboardButton('രോമാഞ്ചം പ്രീമിയം 🔕', callback_data='premium')
        ],[
        InlineKeyboardButton('✘ Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    PREMIUM_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('💰 Pᴀʏ 100', callback_data='payment')
        ],[
         InlineKeyboardButton('Dᴇᴍᴏ Pɪᴄꜱ 🏞️', callback_data='about')
        ],[ 
        InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='home'),   
        InlineKeyboardButton('✘ Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('❔ ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👤 Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ', user_id='6807518752'),    
        InlineKeyboardButton('💰 Payment', callback_data='qrpay')       
        ],[
        InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='premium'),       
        InlineKeyboardButton('✘ Cʟᴏsᴇ', callback_data='close')
        ]]
    )
