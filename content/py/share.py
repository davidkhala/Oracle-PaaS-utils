from content.py import Base


class Share(Base):
    def base_url(self):
        return super().url() + '/documents/api/1.2/publiclinks/'

    def folder(self, folder_id: str):
        url = self.base_url() + 'folder/' + folder_id
        data = {
            'assignedUsers': '@serviceinstance',
            'role': 'viewer',
        }
        r = self._post(url, data)
        link_id = r['linkID']

        return super().url() + '/documents/link/' + link_id + '/folder/' + folder_id

    # https://cx-hktwlab.cec.ocp.oraclecloud.com/documents/link/LD979F1CE34F573A64CBE3A90E1FC11A7E8838DA8482/fileview/D5DE1AA963B6312CF888905E9A109EE6244765C62812/_CafeSupremoBlogManagement.zip
    def file(self, file_id: str):
        url = self.base_url() + 'file/' + file_id
        data = {
            'assignedUsers': '@serviceinstance',
            'role': 'viewer',
        }
        r = self._post(url, data)
        link_id = r['linkID']
        return super().url() + '/documents/link/' + link_id + '/fileview/' + file_id
