from scapy.all import *
from scapy.layers.tls.all import *

# Define Cipher Suites
TLS_CIPHER_SUITES = [
    0x1301,  # TLS_AES_128_GCM_SHA256
    0x1302,  # TLS_AES_256_GCM_SHA384
    0x1303,  # TLS_CHACHA20_POLY1305_SHA256
    0xC02C,  # ECDHE-RSA-AES256-GCM-SHA384
    0xC02F,  # ECDHE-RSA-AES128-GCM-SHA256
]

# Manually encode the SNI extension (type 0x0000)
server_name = b"accounts.google.com"
sni_extension = (
    b"\x00\x00"  # Extension type (SNI)
    + (len(server_name) + 5).to_bytes(2, "big")  # Total length
    + b"\x00"  # Name type (host_name)
    + len(server_name).to_bytes(2, "big")  # Name length
    + server_name  # Hostname
)

# Create the ClientHello message
client_hello = TLSClientHello(
    version=0x0303,  # TLS 1.2
    gmt_unix_time=0,  # Optional for deterministic output
    random_bytes=bytes.fromhex("b6485be724383ef9ac81d8bc51995ead11c16b954c79fc4417cfc95207fcd7fb"),
    cipher_suites=TLS_CIPHER_SUITES,
    extensions=[sni_extension],  # Add the manually encoded SNI extension
)

# Serialize the ClientHello to hex
hex_string = client_hello.build().hex()
print(f"ClientHello Hex String: {hex_string}")
