import socket
from irc import rinIRC
import json
import sys
import time


class Simplebot():
    def __init__(self) -> None:
        self.sock = socket.socket()
        self.SetMessage = []
        pass

    def connect(self) -> None:

        print("Socket dial -> irc.twitch.tv:6667")
        self.sock.connect(("irc.twitch.tv", 6667))
        self.sock.send("NICK justinfan123\r\n".encode("utf-8"))

        self.sock.send(bytes("CAP REQ :twitch.tv/tags\r\n", "UTF-8"))
        self.sock.send(bytes("CAP REQ :twitch.tv/membership\r\n", "UTF-8"))
        self.sock.send(bytes("CAP REQ :twitch.tv/commands\r\n", "UTF-8"))

        self.sock.send("JOIN #djclancy\r\n".encode("utf-8"))

        return


    def readfuntion(self):
        buffer = ""
        buffer += self.sock.recv(4096).decode('utf-8')
        temp = buffer.split("\r\n")
        buffer = temp.pop()
        try:
            for line in temp:
                _line = str(line.encode("utf-8").decode("utf-8"))
                if line == "PING :tmi.twitch.tv":
                    self.sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))

                ircTranslate = (rinIRC(str(_line)).parseIRCMessage())
                if ircTranslate[0]["Command"] == "001" and ircTranslate[1] == None:
                    print("Connected!")
                else:
                    print(ircTranslate[0])
                    self.SetMessage.append(ircTranslate[0])

        except Exception as e:
            print(e)
        return


    def run(self):
        self.connect()
        while True:
            try:
                self.readfuntion()
            except KeyboardInterrupt:
                with open(f"stream-{round(time.time() * 1000)}.json", 'w',  encoding='utf-8') as f:
                    json.dump(self.SetMessage, f, ensure_ascii=False, indent=4)
                sys.exit(0)

if __name__ == "__main__":
    Simplebot().run()