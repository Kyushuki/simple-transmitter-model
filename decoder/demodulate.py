import numpy as np


class Demodulate():
    """
    Класс демодуляции комплексных чисел в биты
    """
    map = {
        "00": 1j,
        "01": -1 + 0j,
        "10": -1j,
        "11": 1 + 0j,
    }

    def demodulate_qpsk(self, mess: list[complex]) -> str:
        """
        Метод демодулирует QPSK комплексные числа (сигнал) в биты
        """
        def demodulate(phi, beta, mess: list[complex]) -> str:
            """
            Непосредственно демодулирует
            """
            if abs(phi) >= 1e-6:
                r = complex(np.exp(-1j * phi))
                mess = [c * r for c in mess]
            mess = [c / beta for c in mess]
            res = []
            print(f"Так выглядит перед демодуляцией: \n{mess}")
            for i in mess:
                min_dist = float('inf')
                k = ""
                for key, value in self.map.items():
                    if abs(i - value) < min_dist:
                        min_dist = abs(i - value)
                        k = key
                res += k
            return res

        z01 = self.map["10"]
        z02 = self.map["01"]
        a = [(mess[0] / z01), (mess[1] / z02), (mess[-2] / z01), (mess[-1] / z02)]
        beta = np.mean(np.abs(a))
        phi = np.angle(np.mean(a))
        res = demodulate(phi, beta, mess)
        result = ''.join(res)
        print(result)
        return result
