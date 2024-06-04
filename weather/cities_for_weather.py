import yaml
from config.global_config import cities_list
class Cities:
    @staticmethod
    def cities_in_yaml():
        with open('cities.yaml', 'w') as f:
            yaml.dump(cities_list, f)
    @staticmethod
    def str_cities():
        with open('cities.yaml') as f:
            return yaml.load(f, Loader=yaml.Loader)

Cities.cities_in_yaml()



