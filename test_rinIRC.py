import unittest
from irc import rinIRC 

class TestRinIRC(unittest.TestCase):

    def setUp(self):
        # Sample raw IRC messages for testing
        self.test_cases = [
            ":tmi.twitch.tv 002 justinfan123 :Your host is tmi.twitch.tv",
            ":tmi.twitch.tv 003 justinfan123 :This server is rather new",
            ":tmi.twitch.tv 004 justinfan123 :-",
            ":tmi.twitch.tv 375 justinfan123 :-",
            ":tmi.twitch.tv 372 justinfan123 :You are in a maze of twisty passages, all alike.",
            ":tmi.twitch.tv 376 justinfan123 :>",
            ":tmi.twitch.tv CAP * ACK :twitch.tv/tags",
            ":justinfan123!justinfan123@justinfan123.tmi.twitch.tv JOIN #djclancy",
            "@emote-only=0;followers-only=-1;r9k=0;room-id=268669435;slow=0;subs-only=0 :tmi.twitch.tv ROOMSTATE #djclancy",
            ":justinfan123.tmi.twitch.tv 353 justinfan123 = #djclancy :justinfan123",
            ":justinfan123.tmi.twitch.tv 366 justinfan123 #djclancy :End of /NAMES list",
            "@badge-info=;badges=;client-nonce=214e9aa84441647bfe07b1906158474c;color=#FF7F50;display-name=kinged1130;emotes=emotesv2_e50f8b815384472b899de8fdd470fb19:7-18,20-31,33-44,46-57,59-70,72-83,85-96;first-msg=0;flags=;id=799bc3d8-9add-4866-ae31-8c32ec766bd4;mod=0;returning-chatter=0;room-id=268669435;subscriber=0;tmi-sent-ts=1726799771057;turbo=0;user-id=124995234;user-type= :kinged1130!kinged1130@kinged1130.tmi.twitch.tv PRIVMSG #djclancy :orange thatoneDance thatoneDance thatoneDance thatoneDance thatoneDance thatoneDance thatoneDance",
            "@badge-info=;badges=glhf-pledge/1;client-nonce=d51e31a25b2d22aba5b79ce57d702022;color=#79F8C3;display-name=senibaj;emotes=;first-msg=1;flags=;id=05519ebc-6d80-45f1-8fb0-0c10a1b6c50e;mod=0;returning-chatter=0;room-id=268669435;subscriber=0;tmi-sent-ts=1726799771574;turbo=0;user-id=145985397;user-type= :senibaj!senibaj@senibaj.tmi.twitch.tv PRIVMSG #djclancy :loquacious",
            "@badge-info=;badges=raging-wolf-helm/1;client-nonce=85668a10856f2deb2f099bb45f73c2f4;color=#8A2BE2;display-name=ToxicTaco11;emotes=;first-msg=0;flags=;id=ef9a046d-54f9-4503-94d6-c612df7a21f3;mod=0;returning-chatter=0;room-id=268669435;subscriber=0;tmi-sent-ts=1726799771784;turbo=0;user-id=45681683;user-type= :toxictaco11!toxictaco11@toxictaco11.tmi.twitch.tv PRIVMSG #djclancy :perfect esfand",
        ]

    def test_parseIRCMessage(self):
        for raw_message in self.test_cases:
            irc = rinIRC(raw_message)
            message, error = irc.parseIRCMessage()
            self.assertIsNone(error)
            self.assertEqual(message["Raw"], raw_message)

if __name__ == '__main__':
    unittest.main()
