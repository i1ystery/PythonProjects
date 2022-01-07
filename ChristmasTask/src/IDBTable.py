from abc import ABC, abstractmethod


class IDBTable(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save(self, entry):
        pass

    @abstractmethod
    def delete(self, entry):
        pass

    @abstractmethod
    def import_data(self, path):
        pass

    @abstractmethod
    def export_data(self, path):
        pass
