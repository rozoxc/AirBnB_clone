import json
"""class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances"""

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self, id):
        self.id = id

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Add a new object to the FileStorage.
        """
        key = f'{type(self). __name__}.{object.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize objects from FileStorage and save them to a JSON file
        """
        obj = {}
        for key, value in FileStorage.__objects.items():
            if isinstance(value, dict):
                obj[key] = value
            else:
                obj[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj, file)

    def reload(self):
        """
        Deserialize objects from the JSON file
        and reload them 0o the FileStorage.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj = json.load(file)
            new_obj = {}
            for key, value in obj.items():
                class_name = value['__class__']
                cls = self.classes()[class_name]
                instance = cls(**value)
                new_obj[key] = instance
            obj = new_obj
            FileStorage.__objects = obj
        except FileNotFoundError:
            pass
