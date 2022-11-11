from utils import convert_csv_to_json, create_fixtures


if __name__ == '__main__':
    apps = [
        ('ads', 'ad'),
        ('categories', 'category'),
        ('locations', 'location'),
        ('users', 'user')
    ]

    for ap in apps:
        directory, table = ap
        create_fixtures(
            input_file=convert_csv_to_json(f'datasets/{table}.csv'),
            output_file=f'{directory}/fixtures/{table}.json',
            model=f'{directory}.{table}'
        )
