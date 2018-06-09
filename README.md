# Web Scraping with Flask + Scrapy + Cloundant

This is a v1 Web Scraping Test.

In this version we scrap the Star Trek Official Web Site, generate a Json File and sabe the results on the Cloundant Database.


## Prerequisites

You'll need the following:
* [IBM Cloundant Database](https://console.bluemix.net/docs/services/Cloudant/getting-started.html)
* [Git](https://git-scm.com/downloads)
* [Python](https://www.python.org/downloads/)

## 1. Fork

Clone the repository:

```
git clone https://github.com/jcabralc/webScrapingTeste
```

## 2. Requirements

Install the application requirements:

```
pip install -r requirements.txt
```
## 3. Configure Cloudant

You need to provide the credentials of Cloudant in our IBM Cloud account. After this you will be able to save the links on the database

Copy your **Cloundant Service Credentials** into **vcap-local.json** file (you need to create it):

    ```
    {
    "services": {
      "cloudantNoSQLDB": [
        {
          "credentials": {
            "username":"XXXXXXXXXX",
            "password":"XXXXXXXXX",
            "host":"XXXXXXXXXX"
          },
          "label": "cloudantNoSQLDB"
        }
      ]
    }
  }
    ```

## 4. Run the app 

Run the app.
  ```
python server.py
  ```

 View your app at: http://localhost:8000

Firt you will need to click on **Gerar JSON** to start the web scraping on Star Trek Official Web Site.
This will generate a JSON file.

After click on **Salvar na Base** to save the JSON file on the CLoudant DataBase on Cloud.

All the URL scraped will be shown on the screen.

This is the v1 of this project.
