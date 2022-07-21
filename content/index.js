// Imports the contentSDK class. You could import the createDeliveryClient or createPreviewClient functions instead.
import { contentSDK }  from '@oracle/content-management-sdk';

const contentDeliveryClient = contentSDK.createDeliveryClient({
    contentServer: 'https://<service-name>-<account-name>.cec.ocp.oraclecloud.com',
    contentVersion: 'v1.1',
    channelToken: '<token>', // Use your published channel token
    logger: console,
});


