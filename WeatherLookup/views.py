from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST["zipcode"]
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="
            + zipcode
            + "&distance=25&API_KEY=B5EBB1CC-54ED-4BF0-8289-235D3392E07D"
        )

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
            
        if api[0]["Category"]["Name"] == "Good":
            category_description = "Enjoy good weather"
            category_color = "Good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_description = "air quality is not so good, take care"
            category_color = "Moderate"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_description = "not advised to go out today"
            category_color = "Unhealthy"
        elif api[0]["Category"]["Name"] == "Harzardous":
            category_description = "Health alert not to go out "
            category_color = "Harzardous"

        return render(
            request,
            "home.html",
            {
                "api": api,
                "category_description": category_description,
                "category_color": category_color,
            },
        )

    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=B5EBB1CC-54ED-4BF0-8289-235D3392E07D"
        )

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    if api[0]["Category"]["Name"] == "Good":
        category_description = "Enjoy good weather"
        category_color = "Good"
    elif api[0]["Category"]["Name"] == "Moderate":
        category_description = "air quality is not so good, take care"
        category_color = "Moderate"
    elif api[0]["Category"]["Name"] == "Unhealthy":
        category_description = "not advised to go out today"
        category_color = "Unhealthy"
    elif api[0]["Category"]["Name"] == "Harzardous":
        category_description = "Health alert not to go out "
        category_color = "Harzardous"

    return render(
        request,
        "home.html",
        {
            "api": api,
            "category_description": category_description,
            "category_color": category_color,
        },
    )


def about(request):
    return render(request, "about.html", {})
