import os
import csv

from django.core.management import BaseCommand

from iranian_cities import data
from iranian_cities.models import (
    Province, County, District,
    City, RuralDistrict, Village
)


class Command(BaseCommand):
    help = 'Generate all data'

    def add_arguments(self, parser):
        """initialize arguments"""
        pass

    def read_csv(self, path):
        with open(path, encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                print(row)
            return csv_reader

    def generate_province(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            province_objs = [
                Province(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    code=row.get('code')
                ) for row in data
            ]
            Province.objects.bulk_create(province_objs)
            print('Province Objects Created Successfully')

    def generate_county(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            county_objs = [
                County(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    code=row.get('code'),
                    province_id=int(row.get('province'))
                ) for row in data
            ]
            County.objects.bulk_create(county_objs)
            print('County Objects Created Successfully')

    def generate_district(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            district_objs = [
                District(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    code=row.get('code'),
                    province_id=int(row.get('province')),
                    county_id=int(row.get('county'))
                ) for row in data
            ]
            District.objects.bulk_create(district_objs)
            print('District Objects Created Successfully')

    def generate_city(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            city_objs = [
                City(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    code=row.get('code'),
                    province_id=int(row.get('province')),
                    county_id=int(row.get('county')),
                    district_id=int(row.get('district')),
                    city_type=row.get('city_type')
                ) for row in data
            ]
            City.objects.bulk_create(city_objs)
            print('City Objects Created Successfully')

    def generate_rural_district(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            rural_district_objs = [
                RuralDistrict(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    code=row.get('code'),
                    province_id=int(row.get('province')),
                    county_id=int(row.get('county')),
                    district_id=int(row.get('district'))
                ) for row in data
            ]
            RuralDistrict.objects.bulk_create(rural_district_objs)
            print('RuralDistrict Objects Created Successfully')

    def generate_village(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            village_objs = [
                Village(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    code=row.get('code'),
                    province_id=int(row.get('province')),
                    county_id=int(row.get('county')),
                    district_id=int(row.get('district')),
                    village_type=row.get('village_type'),
                    rural_district_id=int(row.get('rural_district'))
                ) for row in data
            ]
            Village.objects.bulk_create(village_objs)
            print('Village Objects Created Successfully')

    def handle(self, *args, **options):
        province_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'province.csv')
        county_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'county.csv')
        district_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'district.csv')
        city_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'city.csv')
        rural_district_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'rural_district.csv')
        village_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'village.csv')

        self.generate_province(province_data_path)
        self.generate_county(county_data_path)
        self.generate_district(district_data_path)
        self.generate_city(city_data_path)
        self.generate_rural_district(rural_district_data_path)
        self.generate_village(village_data_path)

        self.stdout.write(
            self.style.SUCCESS('Data generated successfully.')
        )
