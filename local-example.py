# LDAP-Nutzer und Passwort für den Zugriff
LDAP_URI = 'ldaps://server/OU=Users,OU=HS,DC=hs-mittweida,DC=de'
LDAP_USERNAME = 'LDAPUser'
LDAP_PASSWORD = 'XXXXXXXXXXX'

# LDAP-Testdaten
# (Daten eines existierenden Nutzers)
LDAP_TEST = {
    'username': 'testuser',
    'expected_firstname': 'Test',
    'expected_lastname': 'User',
    'expected_mail': 'testuser@server',
}
