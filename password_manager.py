from cryptography.fernet import Fernet
import hashlib
import json


class File_Enc_Dcr:
    def __init__(self, file_name, password):
        self.file_name = file_name
        self.__fernet_obj = Fernet(hashlib.sha256(bytes(password, 'ascii')).hexdigest()[:43] + "=")

    def enc_file(self, content):
        with open(self.file_name, 'wb') as f:
            f.write(self.__fernet_obj.encrypt(bytes(content, 'ascii')))

    def decr_file(self):
        with open(self.file_name, 'rb') as f:
            content = f.read()

        return self.__fernet_obj.decrypt(content).decode()


class Quires:
    def __init__(self, file_name, password, file_new=False):

        self.file_obj = File_Enc_Dcr(file_name, password)
        self.__data = ""

        if file_new:
            self.file_obj.enc_file(self.__data)
        else:
            try:
                self.__data = self.file_obj.decr_file()
            except FileNotFoundError:
                print("New User Created. Please Remember Password. There is no way to reset it.")
                self.file_obj.enc_file(self.__data)
                input()

    def get_data(self):
        return self.__data

    def put_data(self, data):
        self.__data = data

    def append_data(self, data):
        self.__data += data

    def del_data(self):
        self.__data = ""

    def commit(self):
        self.file_obj.enc_file(self.__data)


class PasswordManager:
    def __init__(self, m_password):
        self.__FILE_NAME = "pm.bin"
        self.quire_obj = Quires(self.__FILE_NAME, m_password)

        if self.quire_obj.get_data() == "":
            self.__passwords = {}
        else:
            self.__passwords = json.loads(self.quire_obj.get_data())

    def get_all_pass(self):
        return self.__passwords

    def get_pass_by_key(self, key):
        key = key.upper().strip()
        if key in self.__passwords:
            return self.__passwords[key]
        return None

    def add_new_entrie(self, key, value):
        key = key.upper().strip()
        if key in self.__passwords:
            return False

        self.__passwords[key] = value
        self.quire_obj.put_data(json.dumps(self.__passwords))
        self.quire_obj.commit()
        return True

    def update_entrie(self, key, value):
        key = key.upper().strip()
        if key in self.__passwords:
            self.__passwords[key] = value
            self.quire_obj.put_data(json.dumps(self.__passwords))
            self.quire_obj.commit()
            return True
        return False

    def del_entrie(self, key):
        key = key.upper().strip()
        if key in self.__passwords:
            del self.__passwords[key]
            self.quire_obj.put_data(json.dumps(self.__passwords))
            self.quire_obj.commit()
            return True
        return False

    def update_password(self, m_password):
        data = self.quire_obj.get_data()
        if data == "":
            data = json.loads("{}")
        else:
            data = json.loads(data)
        self.quire_obj = Quires(self.__FILE_NAME, m_password, True)
        self.quire_obj.put_data(json.dumps(data))
        self.quire_obj.commit()
