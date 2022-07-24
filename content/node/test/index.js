import {Content} from '../index.js'

describe('content management', function () {
    this.timeout(0)
    it('connect', async () => {
        const username = 'david.yx.liu@oracle.com';
        const {password} = process.env
        const tenancy = 'hktwlab'
        const instance = 'cx'
        const content = new Content({username, password, tenancy, instance})
        const result = await content.homeDir()

        console.debug(result)
    })
})