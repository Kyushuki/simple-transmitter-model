class DePacket():
    codes = {
        "11": "mycode",
        "00": "basic"
    }

    def __init__(self):
        self.PILOT = "1001"

    def depacket(self, mess: str) -> tuple:
        """
        Метод распаковывает демодулированное сообщение, убирая из него пилотные сигналы и определяя заданную кодировку
        """
        res = ""
        code = ""
        if mess[0:4] != self.PILOT:
            return mess, "error"
        else:
            res = mess[4:]
            res = mess[-4:]
            code = res[0:2]
            if code not in self.codes:
                return mess, "error"
            res = res[2:]
            return res, self.codes[code]
        # return mess[6:], "basic"
        pass
