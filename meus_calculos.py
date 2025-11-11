# --- meus_calculos.py ---
import math

def arredondar_nota_para_cima(nota):
    """
    Arredonda uma nota para o múltiplo de 0.5 mais próximo,
    sempre arredondando para cima.
    """
    nota_dobrada = nota * 2
    nota_dobrada_arredondada = math.ceil(nota_dobrada)
    nota_final = nota_dobrada_arredondada / 2
    return nota_final

# Você pode adicionar outras funções de cálculo aqui no futuro