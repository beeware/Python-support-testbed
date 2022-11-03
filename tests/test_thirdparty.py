###########################################################################
# Tests of third-party modules
###########################################################################
import os
import sys
import warnings

import pytest


@pytest.mark.skipif(sys.platform == "win32", reason="cffi not available on windows")
def test_cffi():
    "CFFI can be used as an alternative FFI interface"
    from cffi import FFI

    ffi = FFI()
    ffi.cdef("size_t strlen(char *str);")
    lib = ffi.dlopen(None)
    assert lib.strlen(ffi.new("char[]", b"hello world")) == 11


def test_cryptography():
    "The cryptography module can be used"
    # Cryptography is a common binary library that uses cffi and OpenSSL (1.1.1) internally
    from textwrap import dedent

    from cryptography import x509
    from cryptography.fernet import Fernet
    from cryptography.hazmat.backends import default_backend
    from cryptography.x509.oid import NameOID

    # Encrypt a message with Fernet
    key = Fernet.generate_key()
    f = Fernet(key)
    msg = b"my deep dark secret"
    token = f.encrypt(msg)
    assert msg == f.decrypt(token)

    # Decode an x509 certificate
    cert_pem = dedent(
        """
        -----BEGIN CERTIFICATE-----
        MIIEhDCCA2ygAwIBAgIIF2d9E030vlcwDQYJKoZIhvcNAQELBQAwVDELMAkGA1UE
        BhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczElMCMGA1UEAxMc
        R29vZ2xlIEludGVybmV0IEF1dGhvcml0eSBHMzAeFw0xODA0MTcxMzI0MzhaFw0x
        ODA3MTAxMjM5MDBaMGkxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlh
        MRYwFAYDVQQHDA1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKDApHb29nbGUgSW5jMRgw
        FgYDVQQDDA93d3cuYW5kcm9pZC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
        ggEKAoIBAQC3t8zd3s9oSLFUkogYhD//BoFwvtHnpUHW2n9g3KiAXCHHG5+8QD4Q
        abgAzrpeQqewWngE9B3Feq4rUo9vsk0UpB7Pj97TAgkkmpRMcW0lU4p4rKNhDfri
        c+SvnuZuy048v8Ta7DtMymuCIyejekjTg7Gf/U46PqK87ZbV5RTadSgfvlymnkQb
        SwJLUA8qe/H98bEARpQLyJvWi8dUSurpfKHdbXfd1Dk9GACHNAX9A4bV0BdQBmPu
        6BMGeY5O4CYwwM51U/W+ptyc5eFRMi10up1cck3Udwl/jw5OAx5NP7geuxuIc4uu
        l41Zwbnr5v6sdJJsWMvMg7ot/97+EHvXAgMBAAGjggFDMIIBPzATBgNVHSUEDDAK
        BggrBgEFBQcDATAaBgNVHREEEzARgg93d3cuYW5kcm9pZC5jb20waAYIKwYBBQUH
        AQEEXDBaMC0GCCsGAQUFBzAChiFodHRwOi8vcGtpLmdvb2cvZ3NyMi9HVFNHSUFH
        My5jcnQwKQYIKwYBBQUHMAGGHWh0dHA6Ly9vY3NwLnBraS5nb29nL0dUU0dJQUcz
        MB0GA1UdDgQWBBSYOxV7LRH/9yKSFL5jLJfhwZxCUDAMBgNVHRMBAf8EAjAAMB8G
        A1UdIwQYMBaAFHfCuFCaZ3Z2sS3ChtCDoH6mfrpLMCEGA1UdIAQaMBgwDAYKKwYB
        BAHWeQIFAzAIBgZngQwBAgIwMQYDVR0fBCowKDAmoCSgIoYgaHR0cDovL2NybC5w
        a2kuZ29vZy9HVFNHSUFHMy5jcmwwDQYJKoZIhvcNAQELBQADggEBAI4fv5P+VLSE
        /f+hOoPuxWx2TEDdc/Gt2u3XUiGkMrOSW2k1ob0kUjBDILhear3tpp+V5N5H0NzZ
        Ymvpbbl3ZD5Bk5Co9FIJwFNMfGAlzSAduuYdAblOXTkLzlyLwn5qbzDjbkBIS+0O
        l+1zga+3gZGYbDQiByFyq8P/uAKzc0BAX82bgXDkIC3E26YvvTnUpkKh6l6bOOTB
        xaTg8Uh6KsKGch837BDbNegs3wHw3T3s7PC+H7dvqjELqN7y2GNNA361/aPPCWgs
        jUsy3XnYSd8og34IzY3+W2b3TrU8P+p+pBwOjgXuNHZwobU+3/e2s4/0AfDilpI0
        KX/1hroho1I=
        -----END CERTIFICATE-----
    """
    ).encode("ASCII")

    cert = x509.load_pem_x509_certificate(cert_pem, default_backend())
    domain = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
    assert "www.android.com" == domain


def test_lru_dict():
    "The LRUDict binary module can be used"
    # lru-dict is the simplest possible example of a third-party module.
    # It is pure C, built using distutils, with no dependencies.
    from lru import LRU

    lru_dict = LRU(5)

    # Add 10 items
    for i in range(10):
        lru_dict[f"item_{i}"] = i

    # Items 0-4 have been evicted
    for i in range(5):
        assert f"item_{i}" not in lru_dict
    # Items 5-9 are still there
    for i in range(5, 10):
        assert lru_dict[f"item_{i}"] == i


def test_pillow():
    "Pillow can be used to load images"
    # Pillow is a module that has dependencies on other libraries (libjpeg, libft2)
    from PIL import Image

    for extension in ["png", "jpg"]:
        image = Image.open(
            os.path.join(
                os.path.dirname(__file__), "resources", f"test-pattern.{extension}"
            )
        )
        assert image.size == (1366, 768)


def test_numpy():
    "Numpy Arrays can be created"
    from numpy import array

    # Numpy is the thousand pound gorilla packaging test.
    assert [4, 7] == (array([1, 2]) + array([3, 5])).tolist()


def test_pandas():
    "Pandas DataFrames can be created"
    from pandas import DataFrame

    # Another high profile package, with a dependency on numpy
    df = DataFrame(
        [("alpha", 1), ("bravo", 2), ("charlie", 3)], columns=["Letter", "Number"]
    )

    with warnings.catch_warnings():
        # Pandas 1.5 changed the `line_terminator` argument to `lineterminator`
        warnings.filterwarnings("ignore", category=FutureWarning)

        assert (
            ",Letter,Number\n" "0,alpha,1\n" "1,bravo,2\n" "2,charlie,3\n"
        ) == df.to_csv(line_terminator="\n")
