def load_to_csv(df):
    output = df.to_csv('Bloomberg_data.csv')
    return output


def load_to_json(df):
    output = df.to_json('Bloomberg_data.json')
    return output


def main():

    print('[Load] Start')
    print('[Load] Saving data to csv')
    load_to_csv(df)

    print('[Load] Data saved as "Bloomberg_data.csv"')
    print('[Load] End.')
