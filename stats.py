# coding=utf8
"""
stats.py
"""

import willie

def setup(bot):
    if not bot.memory.contains('stats_site'):
        bot.memory['stats_site'] = "http://rc.softcheese.net"

@commands('stats')
@example('.stats')
def report_stats(bot, trigger):
   site = bot.memory['stats_site']
   return bot.reply("See IRC stats at %s! Ask an owner for username/password." % site)
   