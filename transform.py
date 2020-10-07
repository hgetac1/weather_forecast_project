"""
>>> convert_kelvin_to_celsius(df_test_convert_kelvin_to_celsius)
      country   temp  temp_min  temp_max  pressure  humidity  wind_speed  wind_deg          dt radiation
ITA     Italy  71.85     16.85     69.85        12        56         110       180  1600234345      high
ESP     Spain  15.85     24.85     59.85        13        67          90       189  1600234345       low
GRC    Greece  59.85     25.85     60.85        14        64          98       178  1600234345    medium
FRA    France  38.85    -55.15     71.85        15        63          99       177  1600234345   average
PRT  Portugal  35.85     14.85    -41.15        11        62         100       190  1600234345       low

>>> keep_columns(df_test_keep_columns)
     main.temp  main.temp_min  main.temp_max  main.pressure  main.humidity  wind.speed  wind.deg          dt
ITA        345            290            343             12             56         110       180  1600234345
ESP        289            298            333             13             67          90       189  1600234345
GRC        333            299            334             14             64          98       178  1600234345
FRA        312            218            345             15             63          99       177  1600234345
PRT        309            288            232             11             62         100       190  1600234345
"""

import pandas as pd

# Fake data for testing
data_test_keep_columns = {'country': ['Italy', 'Spain', 'Greece', 'France', 'Portugal'],
                         'main.temp': [345, 289, 333, 312, 309],
                         'main.temp_min': [290, 298, 299, 218, 288],
                         'main.temp_max': [343, 333, 334, 345, 232],
                         'main.pressure': [12,13,14,15,11],
                         'main.humidity': [56,67,64,63,62],
                         'wind.speed': [110,90,98,99,100],
                         'wind.deg': [180,189,178,177,190],
                         'dt': 1600234345,
                         'radiation':['high','low','medium','average','low']}

df_test_keep_columns = pd.DataFrame(data_test_keep_columns, index=[
                               'ITA', 'ESP', 'GRC', 'FRA', 'PRT'])
data_test_convert_kelvin_to_celsius = {'country': ['Italy', 'Spain', 'Greece', 'France', 'Portugal'],
                         'temp': [345, 289, 333, 312, 309],
                         'temp_min': [290, 298, 299, 218, 288],
                         'temp_max': [343, 333, 334, 345, 232],
                         'pressure': [12,13,14,15,11],
                         'humidity': [56,67,64,63,62],
                         'wind_speed': [110,90,98,99,100],
                         'wind_deg': [180,189,178,177,190],
                         'dt': 1600234345,
                         'radiation':['high','low','medium','average','low']}

df_test_convert_kelvin_to_celsius = pd.DataFrame(data_test_convert_kelvin_to_celsius, index=[
                               'ITA', 'ESP', 'GRC', 'FRA', 'PRT'])

def keep_columns(pandas_df):
    """ Keep only the necessary columns of the dataframe
    """
    return pandas_df[['main.temp','main.temp_min','main.temp_max','main.pressure','main.humidity','wind.speed','wind.deg','dt']]


def change_col_name(pandas_df_kept_columns):
    """ Change columns names to  match the SQL database.
    """
    return pandas_df_kept_columns.rename(columns={'main.temp': 'temp', 'main.temp_min': 'temp_min', 'main.temp_max': 'temp_max', 'main.pressure': 'pressure', 'main.humidity': 'humidity', 'wind.speed': 'wind_speed', 'wind.deg': 'wind_deg'})


def convert_kelvin_to_celsius(pandas_df_kept_renamed_columns):
    """ Convert the temp, temp_min, temp_max measurement unit from Kelvin to Celsius.
    """
    columns = ["temp", "temp_min", "temp_max"]
    for column in columns:
        pandas_df_kept_renamed_columns[column] = pandas_df_kept_renamed_columns[column] - 273.15
    return pandas_df_kept_renamed_columns


def set_datetime_col_as_row_index(pandas_df_kept_renamed_columns_in_celsius):
    """ Set the datetime column to be the dataframe row index.
    """
    return pandas_df_kept_renamed_columns_in_celsius.set_index('dt')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
