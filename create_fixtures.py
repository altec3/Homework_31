from utils import convert_csv_to_json, convert_json_to_fixtures


if __name__ == '__main__':

    convert_csv_to_json('datasets/ads.csv', 'datasets/json/ads.json')
    convert_csv_to_json('datasets/categories.csv', 'datasets/json/categories.json')

    convert_json_to_fixtures(
        input_file='datasets/json/ads.json',
        output_file='ads/fixtures/ad.json',
        model='ads.ad'
    )
    convert_json_to_fixtures(
        input_file='datasets/json/categories.json',
        output_file='ads/fixtures/category.json',
        model='ads.category'
    )
