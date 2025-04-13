from onelogin.saml2.utils import OneLogin_Saml2_Utils
from onelogin.saml2.authn_request import OneLogin_Saml2_Authn_Request
from onelogin.saml2.settings import OneLogin_Saml2_Settings

settings = OneLogin_Saml2_Settings()

# Create a SAML AuthnRequest
authn_request = OneLogin_Saml2_Authn_Request(settings)

# Get the SAML Request XML
saml_request_xml = authn_request.get_request()

# Encode and prepare for transmission
encoded_request = OneLogin_Saml2_Utils.deflate_and_base64_encode(saml_request_xml)

print(encoded_request)
