

class FieldModel:

    __name_field = None
    __field_included_inicial_position = None
    __field_excluded_final_position = None

    def __init__(
            self,
            name_field: str,
            field_included_inicial_position: int,
            field_excluded_final_position: int,
    ):
        self.__name_field = name_field
        self.__field_included_inicial_position = field_included_inicial_position
        self.__field_excluded_final_position = field_excluded_final_position

    @property
    def name_field(self):
        return self.__name_field

    @property
    def field_included_inicial_position(self):
        return self.field_included_inicial_position

    @property
    def field_excluded_final_position(self):
        return self.field_excluded_final_position



if __name__ == '__main__':
    name = "teste"
    a = FieldModel(name,1, 0)
    a.name_field = "joao"
    print(a.name_field)