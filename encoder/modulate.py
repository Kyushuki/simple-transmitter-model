class Modulate():
    """
    Класс модуляции QPSK
    """
    map = {
        "00": 1j,
        "01": -1 + 0j,
        "10": -1j,
        "11": 1 + 0j,
    }

    def modulate_qpsk(self, mess: str) -> list[complex]:
        """
        Метод модулирует с помощью QPSK битовое сообщение в комплексные числа для передачи сигнала
        """
        res = []
        for i in range(0, len(mess), 2):
            res.append(self.map[mess[i:i + 2]])
        return res
