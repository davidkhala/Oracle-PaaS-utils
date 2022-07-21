## AuthN
[Integrate with Oracle Content Management Using OAuth](https://docs.oracle.com/en/cloud/paas/content-cloud/solutions/integrate-oracle-content-management-using-oauth.html#GUID-AC061A7E-6488-4BCB-AAB6-C9928AF23EE0)

The OCM REST APIs have been certified to work with the following three grant types: 
- **Client Credentials**: 
  - when integrating application users are not users of OCM
- **Authorization Code**
  - you want to obtain an authorization code first by using an authorization server as an intermediary between the client application and the resource owner.
  - An authorization code is returned to the client through a browser redirect after the resource owner gives consent to the authorization server. 
- **Resource Owner**: The resource owner's password credentials (user name and password) can be used directly as an authorization grant to obtain an access token. Therefore, this grant type is used when the resource owner has a trust relationship with the client, because the client must discard the password after obtaining the access token. 

## Reference
https://github.com/oracle/content-management-sdk
