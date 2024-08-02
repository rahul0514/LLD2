from abc import ABC, abstractmethod


class StatusMapper(ABC):

    @abstractmethod
    def status_mapper(self, staus):
        pass


class databrick(StatusMapper):

    def get_status(self):
        return "SUCCESS"

    def status_mapper(self, status):

        if status == "SUCCESS":
            return "DONE"

        else:
            raise Exception(status)


class SnowFlake(StatusMapper):
    def get_status(self):
        return "SUCCESSFUL"

    def status_mapper(self, status):
        if status == "SUCCESSFUL":
            return "DONE"


def mycode():
    api = SnowFlake()
    if api.status_mapper(api.get_status) == "DONE":
        print("Databricks is on")
