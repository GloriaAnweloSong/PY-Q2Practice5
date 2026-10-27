from pyscript import document, display

def check_country(e):
    country = {
        "ph": "Philippines",
        "au": "Australia",
        "jp": "Japan",
        "fr": "France",
        "sg": "Singapore"

    }

country_code = document.getElementById("countries").value

display(country.get(country_code, "Country code not found"), target = "output1")