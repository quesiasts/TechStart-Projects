class NumeroInvalido(Exception):
    pass 

def somar(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        result = num1 + num2
        return result
    raise NumeroInvalido("Deu erro na soma")

def dividir(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        resultado = num1 / num2
        return resultado
    raise NumeroInvalido("Deu erro na divisão")
