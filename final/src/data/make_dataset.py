import investpy

from api import InvestAPI
from fileManager import FileManager
from datasetManager import DatasetManager

# You can implement a custom api class that uses the same interfaces as the
# library originally used in this project, that is the "investpy".
# Nonetheless, you can implemente another interfaces, since you change
# parts of this source code as needed for your goals.
investAPI = InvestAPI(investpy)


HISTORICAL_DATA_FROM_DATE = '01/01/2015'
HISTORICAL_DATA_TO_DATE = '31/12/2020'
HISTORICAL_DATA_INTERVAL = 'Monthly'


def check_if_can_write_data_to_current_working_directory():
    currentWorkingDirectory = FileManager.get_working_directory()
    head, tail = FileManager.path_split(currentWorkingDirectory)

    if tail != "data":
        raise RuntimeError(
            "Can't write downloaded data in current working directory")


def main():
    check_if_can_write_data_to_current_working_directory()

    indicesManager = investAPI.get_feature("indices")
    datasetManager = DatasetManager(indicesManager)

    datasetManager.save_countries()

    datasetManager.save_indices()

    datasetManager.save_country_indices_relation()

    datasetManager.save_indices_historical_data(
        HISTORICAL_DATA_FROM_DATE,
        HISTORICAL_DATA_TO_DATE,
        HISTORICAL_DATA_INTERVAL
    )


if __name__ == "__main__":
    main()
