# Maria pegou um emprestimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o emprestimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
data_final_emprestimo = data_emprestimo + relativedelta(years=5)
mensalidade = relativedelta(months=1)
parcelas = []
datas_parcela = data_emprestimo


while datas_parcela < data_final_emprestimo:
    parcelas.append(datas_parcela)
    print(f'{datas_parcela.strftime('%d/%m/%Y')}, {len(parcelas)}x')
    datas_parcela += mensalidade

valor_parcela = 1_000_000 / len(parcelas)

print(
    f'Você pegou R$1.000.000 para pagar em {len(parcelas)} meses. O valor de cada parcela será de R${valor_parcela:.2f}')
