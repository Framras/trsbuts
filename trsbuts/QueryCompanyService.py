from trsbuts.UTSConnection import UTSConnection


class QueryCompanyService:
    def __init__(self):
        self._servicepath = "/UTS/rest/kurum"

    # FİRMA SORGULAMA SERVİSİ
    # Firmaların MERSİS numarası, vergi numarası, ÇKYS numarası ve/ya firma unvanı ile firma tanımlayıcı numarası
    # içeren firma bilgilerini sorgulamasını sağlayan servistir.
    def firmasorgula(self, mrs="", vrg="", unv="", krn="", cky=""):
        parametercheck = False
        servicedata = "{"
        if mrs != "":
            servicedata = servicedata + "\"MRS\":\"" + mrs + "\""
            parametercheck = True
        if vrg != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"VRG\":\"" + vrg + "\""
            parametercheck = True
        if unv != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"UNV\":\"" + unv + "\","
            parametercheck = True
        if krn != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"KRN\":" + krn
            parametercheck = True
        if cky != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"CKY\":\"" + cky + "\""
            parametercheck = True

        if parametercheck:
            c: UTSConnection = UTSConnection()
            return c.connect(
                self._servicepath + "/firmaSorgula",
                servicedata + "}"
            )
        else:
            return ""
