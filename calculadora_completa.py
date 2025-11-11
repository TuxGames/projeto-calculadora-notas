import math

def arredondar_nota_para_cima(nota):
    """
    Arredonda uma nota para o múltiplo de 0.5 mais próximo,
    sempre arredondando para cima (para o "teto").
    """
    nota_dobrada = nota * 2
    nota_dobrada_arredondada = math.ceil(nota_dobrada)
    nota_final = nota_dobrada_arredondada / 2
    return nota_final

def iniciar_programa():
    """
    Função principal que roda a calculadora.
    """
    print(' ')
    print('Calculadora de Notas v2.0 (Online)') # v2.0
    print(' ')
    print('Calcule sua nota necessária para passar de ano sem estresse')
    print(' ')
    print('A nota da AV1 do 4º bimestre')
    print('dessa matéria já foi publicada?')

    try:
        pergunta1 = input('Responda com S ou N: ').upper()

        if pergunta1 == 'S':
            nota_semestral1 = float(input('Sua média do 1º Semestre: '))
            nota_3bimestre = float(input('Sua média do 3º bimestre: '))
            nota_av1_4bimestre = float(input('Sua nota da AV1 do 4º bimestre: '))
            
            resultado_final = 28 - (nota_semestral1 * 2 + nota_3bimestre + (nota_av1_4bimestre / 2))
            
            if resultado_final <= 0:
                print('Você já está passado nessa matéria!!!')
            else:
                nota_exata_av2 = 2 * resultado_final
                nota_arredondada = arredondar_nota_para_cima(nota_exata_av2)
                print(f'Sua nota necessária na AV2 para passar de ano é {nota_arredondada}.')

        elif pergunta1 == 'N':
            nota_semestral1 = float(input('Sua média do 1º Semestre: '))
            nota_3bimestre = float(input('Sua média do 3º bimestre: '))
            
            resultado_final = 28 - (nota_semestral1 * 2 + nota_3bimestre)
            
            if resultado_final <= 0:
                print('Você já está passado nessa matéria!!!')
            else:
                nota_arredondada = arredondar_nota_para_cima(resultado_final)
                print(f'Sua média necessária na 4ª unidade para passar de ano é {nota_arredondada}.')
        else:
            print('Resposta inválida. Por favor, responda apenas com S ou N.')

    except ValueError:
        print("\nErro: Você digitou um valor inválido. Use apenas números e ponto (ex: 8.5)")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

# --- Ponto de Partida ---
# Qnd o script for executado, ele começa por aq
if __name__ == "__main__":
    iniciar_programa()