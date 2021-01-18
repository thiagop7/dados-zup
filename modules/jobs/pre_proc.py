import pandas as pd
from modules.utils.pre_proc_utils import \
    calc_total, update_center_cost

from modules.utils.logger_utils import get_logger
from modules.services import services
from modules.repository import unit_of_work


def save_total_cost(df):

    for index, row in df.iterrows():
        services.add_total_cost(
            row['user'],
            row['transaction_date'],
            row['cost_center'],
            row['total_cost'],
            unit_of_work.SqlAlchemyUnitOfWork()
        )


def process(input_path, output_path):

    # read data
    logger = get_logger()
    logger.info('Read input_path: {input_path}'.format(
        input_path=input_path.format(file='Values.xlsx')))

    data_processed = pd.read_excel(input_path.format(file='Values.xlsx'),
                                   engine='openpyxl', sheet_name="Processed")

    logger.info('Read input_path: {input_path}'.format(
        input_path=input_path.format(file='CostCenter.xlsx')))

    cost_center = pd.read_csv(input_path.format(
        file='CostCenter.csv'), delimiter=';')

    # process data
    logger.info('Processing data')
    left_data = data_processed.merge(cost_center, on='cost_center', how='left')

    left_data["total_cost"] = pd.to_numeric(
        left_data["total_cost"], downcast="float")

    left_data["total_cost"] = left_data.apply(
        lambda row: calc_total(row), axis=1)

    left_data["cost_center"] = left_data.apply(
        lambda row: update_center_cost(row), axis=1)

    left_data['transaction_date'] = left_data['transaction_date'].dt.strftime(
        '%Y/%m/%d')

    logger.info(f'Saving data in output path: {output_path}')
    # save data
    left_data[['user', 'transaction_date', 'cost_center', 'total_cost']].to_excel(
        output_path.format(file='TotalCost.xlsx'), index=False)

    logger.info(f'Saving data in database')
    save_total_cost(
        left_data[['user', 'transaction_date', 'cost_center', 'total_cost']])
