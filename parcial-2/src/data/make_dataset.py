import investpy
import os.path

from api.InvestAPI import InvestAPI


def main():

    # You can implement a custom api class that uses the same interfaces as the library
    # originally used in this project, that is the "investpy".
    # Nonetheless, you can implemente another interfaces, since you change parts of this source code
    # as needed for your goals.

    investAPI = InvestAPI(investpy)

    indicesManager = investAPI.get_feature("indices")

    countries_with_listed_indices = indicesManager.get_index_countries()

    countries = os.path.join()