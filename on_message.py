import logging

from modis import main
from modis.tools import data

from . import api_hexconvert, ui_embed

logger = logging.getLogger(__name__)


async def on_message(msgobj):
    """The on_message event handler for this module

    Args:
        msgobj (discord.Message): Input message
    """

    # TODO make an option to limit hex to only the !hex command instead of reading all messages

    if msgobj.content.startswith(data.cache["guilds"][str(msgobj.guild.id)]["prefix"]):
        return

    hex_strs = api_hexconvert.convert_hex_value(msgobj.content)
    if len(hex_strs) > 0:
        for hex_str in hex_strs:
            await msgobj.channel.trigger_typing()
            image_url = "https://dummyimage.com/350x200.png/{0}/{0}".format(hex_str)
            embed = ui_embed.success(msgobj.channel, image_url, hex_str)
            await embed.send()
