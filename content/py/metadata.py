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

    def create(self, collection_name: str, is_private=True, schema={}):
        url = self.base_url() + Metadata.name(collection_name, is_private)

        fields_array = []

        for key, value in schema.items():
            fields_array.append({
                'fieldName': key,
                'fieldType': type(value),
                'defaultValue': value
            })
        r = super()._post(url, {"fieldsArray": fields_array})
        return r

    def delete(self, collection_name, is_private=True):
        url = self.base_url() + Metadata.name(collection_name, is_private)
        r = super()._delete(url)
        return r
