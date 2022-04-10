import re

class rinIRC():
    """ Rin IRC a libary rewriten from the go-irc libray for python
    
        Parameters
        -----------
        rawLine: :class:`str`
            Raw IRC string to prase
        
        Return
        -----------
            `dict`
                returns a dic of parse data
    """
    def __init__(self, rawLine) -> None:
        self.rawLine = rawLine


    def replace_last(self, source_string:str, replace_what:str, replace_with:str) -> str:
        """Replace at the end of a string

        Parameters
        -----------
        source_string: :class:`str`
            String to replace
        replace_what: :class:`str`
            what to replace
        replace_with: :class:`str`
            what to replace with in string

        Return
        -----------
            `str`
                returns a string fixed

        Taken from: http://stackoverflow.com/questions/3675318/ddg#3675423
        """
        head, _sep, tail = source_string.rpartition(replace_what)
        return head + replace_with + tail

    def parseSource(self, rawSource:str) -> dict:
        """Parse the source of the IRC message

        Parameters
        -----------
        rawSource: :class:`str`
            The unparseed data

        Return
        -----------
            source: ` dict[str, str]`
                returns a dict of host, nickname and username
        """

        source = {"Host": "", "Nickname": "", "Username": ""}
        rawSource.replace(":", "", 1)
        regex = re.compile(r"!|@")
        splitS = regex.split(rawSource)
        if len(splitS) == 0:
            return source

        if len(splitS) == 1:
            source["Host"] = splitS[0]
        elif len(splitS) == 2:
            source["Nickname"] = splitS[0]
            source["Host"] = splitS[1]
        else:
            source["Nickname"] = splitS[0]
            source["Username"] = splitS[1]
            source["Host"] = splitS[2]
        return source

    def parseTags(self, rawTags) -> dict:
        """Parse the tags of a irc message

        Parameters
        -----------
        rawTags: :class:`str`
            The unparseed data

        Return
        -----------
            tags: ` dict`
                returns a dict of tags sent in a message
        """
        tags = {}
        rawTags.replace("@", "", 1)

        for tag in rawTags.split(";"):
            pair = tag.split("=", 2)
            key = pair[0]
            value = ""
            if len(pair) == 2:
                value = self.parseIRCTagValue(pair[1])

            tags[key] = value

        return tags

    def parseIRCTagValue(self, rawValue) -> str:
        """Parse the tags values of a irc message

        Parameters
        -----------
        rawValue: :class:`str`
            The unparseed data

        Return
        -----------
            rawValue: ` str`
                returns a fixed string
        """

        tagEscapeCharacters = [("\s", " "),	("\\n", ""),
                               ("\\r", ""), ("\:", ";"), ("\\\\", "\\")]
        for escape in tagEscapeCharacters:
            rawValue.replace(escape[0], escape[1])

        rawValue = self.replace_last(rawValue, "\\", "")
        rawValue = rawValue.strip()
        return rawValue

    def parseIRCMessage(self) -> dict:
        """Parse the raw IRC message

        Parameters
        -----------
        line: :class:`str`
            The unparseed data

        Return
        -----------
            rawValue: ` str`
                returns a fixed string
        """

        message = {"Raw": self.rawLine, "Tags": "", "Params": "",
                   "Source": "", "Command": "", "Params": ""}

        split = self.rawLine.split(" ")
        index = 0
        params = []
        lineSplit = split[index]
        if lineSplit.startswith("@"):
            message["Tags"] = self.parseTags(split[index])
            index += 1

        if index >= len(split):
            return message, 0 # Error(0): partial message

        if split[index].startswith(":"):
            message["Source"] = self.parseSource(split[index])
            index += 1

        if index >= len(split):
            return message, 1 # Error(1): no command

        message["Command"] = split[index]
        index += 1

        if index >= len(split):
            return message, 2 # Error(2): No Prams

        for i, v in enumerate(split[index:]):
            if v.startswith(":"):
                v = " ".join(split[index+i:])
                v.replace(":", "", 1)
                params.append(v.replace(":", "", 1))
                break
            else:
                params.append(v.replace(":", "", 1))

        message["Params"] = params

        return message, None