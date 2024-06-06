from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
    <b>𝐇𝐄𝐋𝐋𝐎 {} 😍👋,
𝗦𝗲𝗹𝗲𝗰𝘁 𝗧𝗵𝗲 𝗚𝗥𝗢𝗨𝗣 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧🌺‼️

നിങ്ങൾക് ഇഷ്ടമുള്ള ഗ്രുപ്പ് select ചെയ്യുക.!!!</b>
"""
    DETAILS_TEXT = """
<b>Hello {} 🫦
 
» രോമാഞ്ചം പ്രീമിയം 🔕

✅ • Daily Videos Updated
✅ • iOS supported
✅ • Full Direct Videos
✅ • Rare Collections & Hot Collections
✅ • Mallu aunty, Girls, etc… available 


🔞Many More Features 👍🏻

Price: 100

Click Pay Button, Pay The Amount And JOIN 🫦</b>
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
    <b>Pᴀʏ Aɴᴅ Sᴇɴᴅ Sᴄʀᴇᴇɴꜱʜᴏᴛ 

    പേയ്‌മെന്റ് ചെയ്യുക എന്നിട്ട് screenshot ഇതിലേക്ക് അയക്കുക 

ചെയ്യാൻ അറിയില്ലെങ്കിൽ @Luffy0000007 ഇതിൽ മെസ്സേജ് അയക്കുക 🤲
    

Dɪʀᴇᴄᴛ Pᴀʏ: t.me/Luffy0000007</b>
    """

    ADS_TEXT = """
    **[Must Watch 🔥](https://t.me/+yxNSj8_0_7dlMTVh)**
    """

    STATUS_TXT = """<b>◉ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>  
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
◉ ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ: <code>{}</code>
◉ ꜰᴇᴇᴇ ᴅʙ ꜱɪᴢᴇ: <code>{}</code></b>"""

    PROGRESS = """
🏎️ Sᴘᴇᴇᴅ : {3}/s\n\n
✅ Dᴏɴᴇ : {1}\n\n
🟰 Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""

    DEMO_TEXT = """
    <b>☝️DEMO OF രോമാഞ്ചം പ്രീമിയം 🔕</b>
    """

    PROOF_UPLOAD = """
    <b>Your Proof Is Submitted ✅
    Admin Will Verify Within Minutes</b>
    """
    ADMINI_ACCEPTED = """
    Enjoy 💦

Admin Is Accepted Your Payment Here Is Your Link: 

⚠️ One Time Link ⚠️
    """

    PIC = "https://telegra.ph/file/13138bb072d6ae54386d4.jpg"

    PAYMENT_QR = "https://telegra.ph/file/4acfd5a112e10ba0bf34f.jpg"

    DEMO_PIC = "https://telegra.ph/file/db021d838de84e8cf7676.jpg"
    
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
         InlineKeyboardButton('Dᴇᴍᴏ Pɪᴄꜱ 🏞️', callback_data='demopic')
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
        InlineKeyboardButton('Sᴇɴᴛ Sᴄʀᴇᴇɴꜱʜᴏᴛ 📲', user_id='6807518752')           
        ],[
        InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='premium'),       
        InlineKeyboardButton('✘ Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    INVITE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗️ Sʜᴀʀᴇ Yᴏᴜʀ Lɪɴᴋ', url='https://t.me/share/url?url=https://t.me/Lufffybro_bot?start={message.from_user.id}')           
        ]]
    )

