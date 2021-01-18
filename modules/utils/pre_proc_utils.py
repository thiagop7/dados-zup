
def calc_total(row):
    if row['active'] == 'Yes':
        percent = (row['total_cost'] / 100) * 10
        return float("{:.2f}".format(row['total_cost'] + percent))
    else:
        return 0


def update_center_cost(row):
    if row['cost_center'] == 'Faturamento':
        return 'Contas a Pagar/Receber'
    else:
        return row['cost_center']
