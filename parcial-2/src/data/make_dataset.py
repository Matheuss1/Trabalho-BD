import investpy

from api import InvestAPI
from fileManager import FileManager
from datasetManager import DatasetManager

# You can implement a custom api class that uses the same interfaces as the
#  library originally used in this project, that is the "investpy".
# Nonetheless, you can implemente another interfaces, since you change
# parts of this source code as needed for your goals.
investAPI = InvestAPI(investpy)


def checkIfCanWriteDataToCurrentWorkingDirectory():
    currentWorkingDirectory = FileManager.get_working_directory()
    head, tail = FileManager.path_split(currentWorkingDirectory)

    if tail != "data":
        raise RuntimeError(
            "Can't write downloaded data in current working directory")


def main():
    checkIfCanWriteDataToCurrentWorkingDirectory()

    indicesManager = investAPI.get_feature("indices")
    datasetManager = DatasetManager(indicesManager)

    datasetManager.saveCountries()


if __name__ == "__main__":
    main()
