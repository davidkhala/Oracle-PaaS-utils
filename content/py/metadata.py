import datetime

from content.py import Base


class Metadata(Base):
    def base_url(self):
        return super().url() + '/documents/api/1.2/metadata/'

    @staticmethod
    def name(collection_name: str, is_private: bool):
        if is_private:
            return 'Personal.' + collection_name
        else:
            return collection_name

    @staticmethod
    def type(value):
        _type = type(value)
        if _type == int or _type == float:
            return 'number'
        if _type == datetime.datetime:
            return 'date'
        if _type == str:
            return 'text'
        if _type == bool:
            return 'boolean'

    @staticmethod
    def serialize_date(value):
        if type(value) == datetime.datetime:
            return value.strftime("%Y-%m-%dT%H:%M:%S")
        return value

    # schema is a must to make a valid collection
    def create(self, collection_name: str, schema: dict, is_private=True):
        url = self.base_url() + Metadata.name(collection_name, is_private)

        fields_array = []

        for key, value in schema.items():
            field_type = Metadata.type(value)

            fields_array.append({
                'fieldName': key,
                'fieldType': field_type,
                'defaultValue': Metadata.serialize_date(value)
            })
        r = super()._post(url, {"fieldsArray": fields_array})
        return r

    def list(self):
        url = self.base_url()
        r = super()._get(url)
        return r

    def delete(self, collection_name, is_private=True):
        url = self.base_url() + Metadata.name(collection_name, is_private)
        r = super()._delete(url)
        return r
