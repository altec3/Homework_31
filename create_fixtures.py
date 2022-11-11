from utils import convert_csv_to_json, create_fixtures


if __name__ == '__main__':

    create_fixtures(
        input_file=convert_csv_to_json('datasets/ad.csv'),
        output_file='ads/fixtures/ad.json',
        model='ads.ad'
    )
    create_fixtures(
        input_file=convert_csv_to_json('datasets/category.csv'),
        output_file='categories/fixtures/category.json',
        model='categories.category'
    )
    create_fixtures(
        input_file=convert_csv_to_json('datasets/location.csv'),
        output_file='locations/fixtures/location.json',
        model='locations.location'
    )
    create_fixtures(
        input_file=convert_csv_to_json('datasets/user.csv'),
        output_file='users/fixtures/user.json',
        model='users.user'
    )
