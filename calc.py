class Calc:
    def sumar(self, num1, num2):
        try:
            if num1 < 0 or num2 < 0:
                return "Invalid"
            return num1 + num2
        except Exception:
            return "Invalid"

    def restar(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return "Invalid"
        return num1-num2

    def multiplicar(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return "Invalid"
        return num1*num2        

    def dividir(self, num1, num2):
        if num1 < 0 or num2 <= 0:
            return "Invalid"
        return num1/num2            