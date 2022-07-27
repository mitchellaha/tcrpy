from enum import Enum

class SortDir(Enum):
    ASC = 0
    DESC = 1

    def fromSettings(settings: str):
        """Convert the settings value to a SortDir enum value"""
        if settings == "sort-asc":
            return SortDir.ASC.value
        elif settings == "sort-desc":
            return SortDir.DESC.value
        else:
            return SortDir.ASC.value
