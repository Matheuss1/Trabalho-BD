from fileManager import FileManager
import pandas as pd
import sys
sys.path.append(".")


class DatasetManager:
    def __init__(self, data_manager, file_manager=FileManager):
        self.__manager = data_manager
        self.file_manager = file_manager

    def setManager(self, data_manager):
        self.__manager = data_manager

    def saveCountries(self):
        listed_countries = self.__manager.get_index_countries()

        folder_saving_path = self.file_manager.path_join(
            self.__get_raw_data_saving_path(), "countries/countries.csv"
        )

        df = pd.DataFrame(data={'country': list(listed_countries)})

        df.to_csv(folder_saving_path, sep=',', index=False)

    def __get_raw_data_saving_path(self):
        working_directory = self.file_manager.get_working_directory()

        return f"{working_directory}/raw"
