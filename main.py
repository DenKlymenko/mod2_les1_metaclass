import pickle


class SerializationInterface:
    def __init__(self, object, directory, write_mode):
        self.dumps = None
        self.object = object
        self.directory = directory
        self.write_mode = write_mode


class convert_to_bin(SerializationInterface):
    def dumps(self):
        with open(self.directory, self.write_mode) as file:
            self.dumps = pickle.dumps(self.object)
            file.write(self.dumps)


class convert_to_json(SerializationInterface):
    def dump(self):
        with open(self.directory, self.write_mode) as file:
            pickle.dump(self.object, file)
