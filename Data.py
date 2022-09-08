from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("Start Generating Session ", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="kembali", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("perintah ", callback_data="help"),
            InlineKeyboardButton("support", url="https://t.me/Gladesupportchannel"),
        ],

    ]

    START = """
Hey {}

{}  **adalah bot yang di buat untuk mempermudahkan anda mengabil string session telegram.**


**Jika Anda tidak mempercayai bot ini,**
1) berhenti membaca pesan ini
2) hapus obrolan ini


MANAGE BY : @KUMiSCooLLL
    """

    HELP = """
**Menu Perintah** 

/help - Bantuan
/start - Memulai Bot
/generate - Generate Session
/cancel - Batal Proses
/restart - Batal Proses
"""
