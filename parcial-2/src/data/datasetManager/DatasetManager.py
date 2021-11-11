from fileManager import FileManager
import pandas as pd
import os
import sys
sys.path.append(".")


class DatasetManager:
    def __init__(self, data_manager, file_manager=FileManager):
        self.__manager = data_manager
        self.file_manager = file_manager

    def set_manager(self, data_manager):
        self.__manager = data_manager

    def save_countries(self):
        listed_countries = self.__manager.get_index_countries()

        folder_saving_path = self.__get_absolute_saving_path(
            "countries/countries.csv"
        )

        df = pd.DataFrame(data={'country': list(listed_countries)})

        df.to_csv(folder_saving_path, sep=',', index=False)

    def save_indices(self):

        world_major_indices = self.__get_major_world_indices()

        indices_names_filtered_df = world_major_indices.filter(
            items=['name', 'currency']
        )

        folder_saving_path = self.__get_absolute_saving_path(
            "listed-world-indices/listed-world-indices.csv"
        )

        indices_names_filtered_df.to_csv(
            folder_saving_path, sep=',', index=False)

    def save_country_indices_relation(self):
        major_world_indices = self.__get_major_world_indices()

        country_indices_relation_table_df = (
            self.__get_country_indices_relation_table(
                major_world_indices
            )
        )

        folder_saving_path = self.__get_absolute_saving_path(
            "indices-from-country/indices-from-country.csv"
        )

        country_indices_relation_table_df.to_csv(
            folder_saving_path, sep=',', index=False
        )

    def save_indices_historical_data(self, from_date, to_date, interval):
        major_world_indices = self.__get_major_world_indices()

        country_indices_relation_table_df = (
            self.__get_country_indices_relation_table(major_world_indices)
        )

        from_year, to_year = (
            self.__get_initial_and_final_year_of_historical_data(
                from_date, to_date
            )
        )

        for index, row in country_indices_relation_table_df.iterrows():
            try:
                historical_data_df = self.__manager.get_index_historical_data(
                    index=row['indice_name'],
                    country=row['country'],
                    from_date=from_date,
                    to_date=to_date,
                    interval=interval
                )
                self.__create_indice_historical_data_folders_by_year(
                    row['indice_name'],
                    from_year,
                    to_year
                )

                for year in range(from_year, to_year + 1):
                    pass
            except Exception:
                continue

    def __create_indice_historical_data_folders_by_year(
        self,
        indice_name,
        from_year,
        to_year
    ):
        for year in range(from_year, to_year + 1):
            try:
                os.makedirs(
                    self.__get_absolute_saving_path(
                        f'indices-historical-data/{indice_name}/{year}'
                    )
                )
            except FileExistsError:
                continue

    def __get_initial_and_final_year_of_historical_data(
        self,
        from_date,
        to_date
    ):
        from_year = int(from_date.split('/')[2])
        to_year = int(to_date.split('/')[2])

        return from_year, to_year

    def __get_major_world_indices(self):
        listed_indices_pd_dataframe = self.__manager.get_indices()

        major_world_indices = self.__filter_by_major_world_indices_only(
            listed_indices_pd_dataframe
        )

        return major_world_indices

    def __get_country_indices_relation_table(self, indices_df):
        country_indices_relation_table_df = indices_df.filter(
            items=['country', 'name']
        )

        country_indices_relation_table_df.rename(
            columns={'name': 'indice_name'},
            inplace=True
        )

        return country_indices_relation_table_df

    def __filter_by_major_world_indices_only(self, indices_df):
        rows_selection_condition = (
            (indices_df['class'] == 'major_indices') &
            (indices_df['market'] == 'world_indices')
        )

        return indices_df.loc[rows_selection_condition]

    def __get_raw_data_saving_path(self):
        working_directory = self.file_manager.get_working_directory()

        return f"{working_directory}/raw"

    def __get_absolute_saving_path(self, path):
        return self.file_manager.path_join(
            self.__get_raw_data_saving_path(),
            path
        )
