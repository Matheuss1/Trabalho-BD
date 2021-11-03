class InvestAPI:
    def __init__(self, financialAPITarget):
        self.api = financialAPITarget

        self.__set_api_features()

    def __set_api_features(self):
        self.features = {
            "indices": self.api.indices
        }


    def get_feature(self, feature):
        try:
            requestedFeature = self.features[feature]

            return requestedFeature
        except:
            raise KeyError(f"API has no feature named {feature}")