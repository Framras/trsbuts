import frappe
import requests
import json


@frappe.whitelist()
def test_integration(test, testtoken):
    company = frappe.defaults.get_user_default("Company")
    servicepath = "/UTS/rest/kurum/firmaSorgula"
    # Replace with the correct URL
    url = ""
    if test == "real":
        url = frappe.db.get_single_value("TR UTS Integration Settings", "server")
    if test == "test":
        url = frappe.db.get_single_value("TR UTS Integration Settings", "testserver")
    # her web servis çağrısının başlık (header) kısmına utsToken etiketiyle sistem token’ının değerini eklemelidir
    __headers = {
        'utsToken': testtoken,
        'Content-Type': frappe.db.get_single_value("TR UTS Integration Settings", "contenttype")
    }

    servicedata = "{"
    servicedata = servicedata + "\"VRG\":\"" + frappe.db.get_value("Company", company, "tax_id") + "\""
    servicedata = servicedata + "}"

    servicerequestdatafields = servicedata

    _requesturl = url + servicepath

    s = requests.Session()
    s.headers.update(__headers)
    # Web servislerin tamamında HTTP request method olarak “POST” metodu kullanılmaktadır.
    response = s.post(_requesturl, servicerequestdatafields)

    return response.text
