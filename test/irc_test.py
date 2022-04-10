import unittest

from irc import rinIRC

class TestBrainMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_normal(self):
        message = ":tmi.twitch.tv 002 ringomar :Your host is tmi.twitch.tv"
        self.assertEqual(rinIRC(message).parseIRCMessage(), ({'Raw': ':tmi.twitch.tv 002 ringomar :Your host is tmi.twitch.tv', 'Tags': '', 'Params': [
                         'ringomar', 'Your host is tmi.twitch.tv'], 'Source': {'Host': ':tmi.twitch.tv', 'Nickname': '', 'Username': ''}, 'Command': '002'}, None))

    def test_message(self):
        message = "@badge-info=;badges=broadcaster/1,premium/1;color=#00FF88;display-name=RingoMar;emotes=;first-msg=0;flags=;id=fdc5148e-c163-47db-82cb-36cc2d6cdc16;mod=0;room-id=78844558;subscriber=0;tmi-sent-ts=1649619048713;turbo=0;user-id=78844558;user-type= :ringomar!ringomar@ringomar.tmi.twitch.tv PRIVMSG #ringomar :test"
        self.assertEqual(rinIRC(message).parseIRCMessage(), ({'Raw': '@badge-info=;badges=broadcaster/1,premium/1;color=#00FF88;display-name=RingoMar;emotes=;first-msg=0;flags=;id=fdc5148e-c163-47db-82cb-36cc2d6cdc16;mod=0;room-id=78844558;subscriber=0;tmi-sent-ts=1649619048713;turbo=0;user-id=78844558;user-type= :ringomar!ringomar@ringomar.tmi.twitch.tv PRIVMSG #ringomar :test',
                                                              'Tags': {'@badge-info': '', 'badges': 'broadcaster/1,premium/1', 'color': '#00FF88', 'display-name': 'RingoMar', 'emotes': '', 'first-msg': '0', 'flags': '', 'id': 'fdc5148e-c163-47db-82cb-36cc2d6cdc16', 'mod': '0', 'room-id': '78844558', 'subscriber': '0', 'tmi-sent-ts': '1649619048713', 'turbo': '0', 'user-id': '78844558', 'user-type': ''},
                                                              'Params': ['#ringomar', 'test'], 'Source': {'Host': 'ringomar.tmi.twitch.tv', 'Nickname': ':ringomar', 'Username': 'ringomar'}, 'Command': 'PRIVMSG'}, None))


if __name__ == '__main__':
    unittest.main()
