import json
import os

# Verifique o diretório atual
print("Diretório de trabalho atual:", os.getcwd())

# Certifique-se de que o arquivo JSON está no mesmo diretório do script
arquivo_json = 'todas_as_tasks/faturamento.json'

# Carregar os dados do arquivo JSON
try:
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)  # Certifique-se de que json.load() seja usado para carregar o JSON como dicionário

    faturamento_diario = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]

    # Calcular o menor, maior faturamento e dias acima da média
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    dias_acima_da_media = len([valor for valor in faturamento_diario if valor > media_mensal])

    # Exibir os resultados
    print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

except FileNotFoundError:
    print(f"Arquivo '{arquivo_json}' não encontrado. Verifique o nome e o caminho do arquivo.")
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON. Verifique se o conteúdo do arquivo está correto.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
