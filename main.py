from pyscript import document, display

def check_country(e):
    document.getElementById("output1").innerHTML = ""
    country= {
        "ph": "Philippines",
        "au": "Australia",
        "jp": "Japan",
        "fr": "France",
        "sg": "Singapore"

    }

    
    country_code = document.getElementById("countries").value

    #add a country
    country["ca"] = "Canada"

    display(country.get(country_code, "Country code not found"), target="output1")

def show_country(e):
    document.getElementById("output1").innerHTML = ""
    country= {
        "ph": "Philippines",
        "au": "Australia",
        "jp": "Japan",
        "fr": "France",
        "sg": "Singapore"

    }

    country_code = document.getElementById("countries").value

    show_country = country_code in country
    list_country = list(country.values())

    display("The number of countries are ", len(country), target="output1")
    display("Is it in the country code list? ", show_country, target="output1")
    display("What are the countries in the list? ", list_country, target="output1")