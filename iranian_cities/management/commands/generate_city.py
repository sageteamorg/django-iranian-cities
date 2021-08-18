import os
import csv

from django.core.management import BaseCommand

from iranian_cities import data
from iranian_cities.models import (
    Ostan, Shahrestan, Bakhsh,
    Shahr, Dehestan, Abadi
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

    def generate_ostan(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            ostan_objs = [
                Ostan(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    amar_code=row.get('amar_code')
                ) for row in data
            ]
            Ostan.objects.bulk_create(ostan_objs)
            print('Ostan Objects Created Successfully')

    def generate_shahrestan(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            shahrestan_objs = [
                Shahrestan(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    amar_code=row.get('amar_code'),
                    ostan_id=int(row.get('ostan'))
                ) for row in data
            ]
            Shahrestan.objects.bulk_create(shahrestan_objs)
            print('Shahrestan Objects Created Successfully')

    def generate_bakhsh(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            bakhsh_objs = [
                Bakhsh(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    amar_code=row.get('amar_code'),
                    ostan_id=int(row.get('ostan')),
                    shahrestan_id=int(row.get('shahrestan'))
                ) for row in data
            ]
            Bakhsh.objects.bulk_create(bakhsh_objs)
            print('Bakhsh Objects Created Successfully')

    def generate_shahr(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            shahr_objs = [
                Shahr(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    amar_code=row.get('amar_code'),
                    ostan_id=int(row.get('ostan')),
                    shahrestan_id=int(row.get('shahrestan')),
                    bakhsh_id=int(row.get('bakhsh')),
                    shahr_type=row.get('shahr_type')
                ) for row in data
            ]
            Shahr.objects.bulk_create(shahr_objs)
            print('Shahr Objects Created Successfully')

    def generate_dehestan(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            dehestan_objs = [
                Dehestan(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    amar_code=row.get('amar_code'),
                    ostan_id=int(row.get('ostan')),
                    shahrestan_id=int(row.get('shahrestan')),
                    bakhsh_id=int(row.get('bakhsh'))
                ) for row in data
            ]
            Dehestan.objects.bulk_create(dehestan_objs)
            print('Dehestan Objects Created Successfully')

    def generate_abadi(self, path):
        with open(path, encoding='utf-8') as f:
            data = csv.DictReader(f)
            abadi_objs = [
                Abadi(
                    id=int(row.get('id')),
                    name=row.get('name'),
                    amar_code=row.get('amar_code'),
                    ostan_id=int(row.get('ostan')),
                    shahrestan_id=int(row.get('shahrestan')),
                    bakhsh_id=int(row.get('bakhsh')),
                    abadi_type=row.get('abadi_type'),
                    dehestan_id=int(row.get('dehestan'))
                ) for row in data
            ]
            Abadi.objects.bulk_create(abadi_objs)
            print('Dehestan Objects Created Successfully')

    def handle(self, *args, **options):
        ostan_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'ostan.csv')
        shahrestan_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'shahrestan.csv')
        bakhsh_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'bakhsh.csv')
        shahr_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'shahr.csv')
        dehestan_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'dehestan.csv')
        abadi_data_path = os.path.abspath(data.__file__).replace('__init__.py', 'abadi.csv')

        self.generate_ostan(ostan_data_path)
        self.generate_shahrestan(shahrestan_data_path)
        self.generate_bakhsh(bakhsh_data_path)
        self.generate_shahr(shahr_data_path)
        self.generate_dehestan(dehestan_data_path)
        self.generate_abadi(abadi_data_path)

        self.stdout.write(
            self.style.SUCCESS('Data generated successfully.')
        )
