import pandas as pd
from utils.Product import Product


# Testing purposes:
sampleAubergine = Product({'artikel': 'aubergine', 'herkunft': 'CN', 'unit': 'kg', 'quantity': 4.2})
sampleBanana = Product({'artikel': 'banana', 'herkunft': 'IN', 'unit': 'kg', 'quantity': 1.2})

# Hardcoded directories
input_dir = "inputs/"
filename = "ecoinvent.xlsx"


def get_co2_emission(df, product):
    df_results = df.query('`reference product` == "{0}" and geography == "{1}"'.format(
        product.get_name(),
        product.get_origin())
    )
    co2_factor = -1
    if df_results.empty:
        return co2_factor
    else:
        co2_factor = df_results.iloc[0][9]

    emission = product.get_quantity() * co2_factor
    return emission


if __name__ == '__main__':
    df = pd.read_excel(input_dir+filename, index_col=0, sheet_name='cumulativeLCIAscore')

    emission = get_co2_emission(df, sampleAubergine)
    if emission is not -1:
        print("emission = ", emission)
    else:
        print("Product not found within Excel sheet")
    emission = get_co2_emission(df, sampleBanana)
    if emission is not -1:
        print("emission = ", emission)
    else:
        print("Product not found within Excel sheet")
