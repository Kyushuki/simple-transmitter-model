class Packet():
    codes = {
        "mycode": "11",
        "basic": "00"
    }

    def __init__(self):
        self.PILOT = "1001"

    def pack(self, mess: str, code: str) -> str:
        """
        Метод упаковывает сообщение в известный вид:

        Пилотный сигнал - код кодировки - сообщение - пилотный сигнал
        """
        result = ""
        result += self.PILOT
        result += self.codes[code]
        result += mess
        # result += self.PILOT
        return result
