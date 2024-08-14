import requests
import pandas as pd
import json
import yaml
from datetime import datetime
from aws_conn import S3Buckets


# Access Config File for Pipeline Variables
with open('config.yaml', 'r') as file:
    variables = yaml.safe_load(file)


class EconomicDataETL:
    def __init__(self, indicators, base_url = "https://api.worldbank.org/v2/country/", countries = "NGA", page = 1):
        self.base_url = base_url
        self.countries = countries
        self.indicators = indicators
        self.page = page

    def extract(self):
        final_data = []
        for indicator in self.indicators:
            for country in self.countries:
                url = f"{self.base_url}{country}/indicator/{indicator}?format=json&page={self.page}&per_page=50"
                response = requests.get(url)
                json_data = response.json()

                if not json_data:
                    print('No JSON file has been collected')

                else:
                    final_data.extend(json_data[1])

        return final_data


    def transform(self, json_data):
        # Create Empty Lists to Collect Information From URL Response
        country_name = []
        country_code = []
        indicator = []
        year = []
        value = []

        for i in json_data:
            country_name.append(i['country']['value'])
            country_code.append(i['countryiso3code'])
            indicator.append(i['indicator']['value'])
            year.append(i['date'])
            value.append(i['value'])

        dataframe = pd.DataFrame(list(zip(country_name, country_code,indicator, year, value)),
                          columns=['country_name', 'country_code', 'indicator', 'year', 'value']).reset_index(drop=True)
        return dataframe

    def load(self, df, current_time=datetime.now().strftime("%d%m%Y%H%M%S")):
        # Initialize S3 Bucket For Data Loading
        s3 = S3Buckets.credentials('us-east-2')
        # Create Bucket for Storing/Staging Data if Not Created
        s3.create_bucket(bucket_name=variables['BUCKET_NAME'])
        # Upload Transformed Dataframe to S3 Bucket Created
        s3.upload_dataframe_to_s3(df, variables['BUCKET_NAME'], f'economic_data_{current_time}.csv')

        return f"economic_data_{current_time} was successfully uploaded to {variables['BUCKET_NAME']}"

    def run_pipeline(self):
        raw_data = self.extract()
        df = self.transform(raw_data)
        self.load(df)

        return "File was uploaded to S3 Bucket"


if __name__ == "__main__":
    ed = EconomicDataETL(indicators=variables['INDICATORS'], countries=variables['COUNTRIES'])
    ed.run_pipeline()