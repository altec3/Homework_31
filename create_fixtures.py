from utils import convert_csv_to_json, create_fixtures


if __name__ == '__main__':

    create_fixtures(
        input_file=convert_csv_to_json('datasets/ads.csv'),
        output_file='ads/fixtures/ad.json',
        model='ads.ad'
    )
    create_fixtures(
        input_file=convert_csv_to_json('datasets/categories.csv'),
        output_file='ads/fixtures/category.json',
        model='ads.category'
    )
