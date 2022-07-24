import {axiosPromise} from '@davidkhala/axios';

export class Content {
    /**
     * TODO @deprecated base auth is going to be deprecated, migrate to OAuth2
     * @param username
     * @param password
     * @param tenancy tenancy name, not OCID
     * @param instance
     */
    constructor({username, password, tenancy, instance}) {
        this.auth = {
            username,
            password
        }
        this.url = `https://${instance}-${tenancy}.cec.ocp.oraclecloud.com/`
    }


    async homeDir() {

        const url = this.url + 'documents/api/1.2/folders/items'
        const {items} = await axiosPromise({url, method: 'GET'}, {
            auth: this.auth
        })
        return items
    }
}


