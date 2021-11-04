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

    def saveIndices(self):
        listed_indices_pd_dataframe = self.__manager.get_indices()

        filtered_df = self.__filter_by_major_world_indices_only(
            listed_indices_pd_dataframe
        )

        indices_names_filtered_df = self.__get_indices_name_only(filtered_df)

        folder_saving_path = self.file_manager.path_join(
            self.__get_raw_data_saving_path(),
            "listed-world-indices/listed-world-indices.csv"
        )

        indices_names_filtered_df.to_csv(
            folder_saving_path, sep=',', index=False)

    def __get_indices_name_only(self, indices_df):
        return indices_df['name']

    def __filter_by_major_world_indices_only(self, indices_df):
        rows_selection_condition = (
            (indices_df['class'] == 'major_indices') &
            (indices_df['market'] == 'world_indices')
        )

        return indices_df.loc[rows_selection_condition]

    def __get_raw_data_saving_path(self):
        working_directory = self.file_manager.get_working_directory()

        return f"{working_directory}/raw"
