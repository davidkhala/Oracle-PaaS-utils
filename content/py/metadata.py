from content.py import Base


class Metadata(Base):
    def base_url(self):
        return super().url() + '/documents/api/1.2/metadata/'

    def create(self, collection_name, schema={}, is_private=True):

        if is_private:
            collection_name = 'Personal.' + collection_name

        url = self.base_url() + collection_name

        fields_array = []

        for key, value in schema.items():
            fields_array.append({
                'fieldName': key,
                'fieldType': type(value),
                'defaultValue': value
            })
        r = super().post(url, {"fieldsArray": fields_array})
        return r
