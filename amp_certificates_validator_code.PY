import re
import subprocess

if __name__ == "__main__":

    def certificates():
        certifcates_list, applied_certificates, i = (
            [
                [
                    "3B1EFD3A66EA28B16697394703A72CA340A05BD5",
                    "CN=Microsoft Root Certificate Authority 2010",
                ],
                ["D69B561148F01C77C54578C10926DF5B856976AD", "CN=GlobalSign"],
                [
                    "D4DE20D05E66FC53FE1A50882C78DB2852CAE474",
                    "CN=Baltimore CyberTrust Root",
                ],
                [
                    "D1EB23A46D17D68FD92564C2F1F1601764D8E349",
                    "CN=AAA Certificate Services",
                ],
                ["B1BC968BD4F49D622AA89A81F2150152A41D829C", "CN=GlobalSign Root CA"],
                [
                    "AD7E1C28B064EF8F6003402014C3D0E3370EB58A",
                    "OU=Starfield Class 2 Certification Authority",
                ],
                [
                    "A8985D3A65E5E5C4B2D7D66D40C6DD2FB19C5436",
                    "CN=DigiCert Global Root CA",
                ],
                [
                    "742C3192E607E424EB4549542BE1BBC53E6174E2",
                    "OU=Class 3 Public Primary Certification Authority",
                ],
                [
                    "5FB7EE0633E259DBAD0C4C9AE6D38F1A61C7DC25",
                    "CN=DigiCert High Assurance EV Root CA",
                ],
                [
                    "4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5",
                    "CN=VeriSign Class 3 Public Primary Certification Authority - G5",
                ],
                [
                    "2796BAE63F1801E277261BA0D77770028F20EEE4",
                    "OU=Go Daddy Class 2 Certification Authority",
                ],
                [
                    "0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43",
                    "CN=DigiCert Assured ID Root CA",
                ],
                [
                    "DDFB16CD4931C973A2037D3FC83A4D7D775D05E4",
                    "CN=DigiCert Trusted Root G4",
                ],
                ["CA3AFBCF1240364B44B216208880483919937CF7", "CN=QuoVadis Root CA 2"],
                [
                    "2B8F1B57330DBBA2D07A6C51F70EE90DDAB9AD8E",
                    "CN=USERTrust RSA Certification Authority",
                ],
                [
                    "F40042E2E5F7E8EF8189FED15519AECE42C3BFA2",
                    "CN=Microsoft Identity Verification Root Certificate Authority 2020",
                ],
                [
                    "DF717EAA4AD94EC9558499602D48DE5FBCF03A25",
                    "CN=IdenTrust Commercial Root CA 1",
                ],
            ],
            [],
            0,
        )
        certificates_dictionary = dict(enumerate(certifcates_list))
        # print(certificates_dictionary)
        # print(*(f"{k}: {v}" for k, v in certificates_dictionary.items()), sep="\n", end="\n\n")
        try:
            powershell_executable = subprocess.Popen(
                ["powershell", "Get-ChildItem -Path Cert:LocalMachine\Root"],
                stdout=subprocess.PIPE,
            )
            result = powershell_executable.communicate()[0]
            # print(result.decode("utf-8"))
            """if re.compile("|".join(search_list), re.IGNORECASE).search(result.decode("utf-8")):
            print("found", search_list)
                else:
            print("Incomplete list")"""
            for sha_number, certificate_value in certificates_dictionary.items():
                if certificate_value[0] not in result.decode("utf-8"):
                    print(
                        "[MISSING]", certificate_value[0], "with", certificate_value[1]
                    )
                else:
                    applied_certificates.append(
                        [certificate_value[0], certificate_value[1]]
                    )
            if len(applied_certificates) > 0:
                for certs in applied_certificates:
                    print(
                        "[OK]",
                        certs[0],
                        "with name",
                        certs[1],
                    )
                    i += 1
            if i == 17:
                print("[ALL YOUR ATS CERTS ARE IN ORDER]")
            else:
                print(
                    "You can install the missing certificates by following the next link: https://youtu.be/jc_b6rQpDMc?si=Jriywsp2cQyov_r9"
                )
        except subprocess.CalledProcessError as e:
            print("No Powershell: ", e)


certificates()
