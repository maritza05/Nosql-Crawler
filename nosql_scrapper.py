from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class NosqlDatabase:

    def __init__(self, name, url, description):
        self.data_model = "Ninguno"
        self.name = name
        self.url = url
        self.description = description
        self.useful_links = []

    def get_description(self):
        return "Data model: %s \tName: %s \tURL: %s" %(self.data_model, self.name, self.url)

    def set_data_model(self, data_model):
        self.data_model = data_model

    def set_useful_link(self, link):
        self.useful_links.append(link)


class NosqlStorage:

    def __init__(self, nosql_list=set()):
        self.nosql_list = nosql_list

    # Quiero poder buscar una base de datos en particular por su nombre
    def search_by_name(self, nosql_name):
        for nosql in self.nosql_list:
            if nosql.name == nosql_name:
                return nosql
        return None

    # Quero buscar todas las bd por su modelo de dato
    def search_by_model(self, data_model):
        query_results = set()
        for nosql in self.nosql_list:
            if nosql.data_model == data_model:
                query_results.add(nosql)
        return query_results

    # Quiero imprimir los resultados de mi busqueda
    def print_results(self, query_result_list):
        for nosql in query_result_list:
            print(nosql.get_description())
            print(nosql.description)
            print("=" * 100)


def get_data_models_tags_new(bsObj):
    datamodels = []
    categories = bsObj.findAll("section")
    for category in categories:
        datamodels.append(category)
    return datamodels

def get_databases_tags_new(url):
    nosql_list = []
    html = urlopen("http://nosql-database.org/")
    bsObj = BeautifulSoup(html, "html.parser")
    data_models = get_data_models_tags_new(bsObj)
    for data_model in data_models:
        database_sections = data_model.findAll("article")
        for section in database_sections:
            tag_with_names = section.find("h3")
            if tag_with_names is not None:
                names_links = tag_with_names.findAll("a")
                if names_links is not None:
                    for name_link in names_links:
                        db_name = name_link.get_text()
                        db_url = name_link.attrs['href']
                        db_info = section.get_text()
                        data_model_name = data_model.find("h2").get_text()
                        nosql_object = NosqlDatabase(db_name, db_url, db_info)
                        nosql_object.set_data_model(data_model_name)
                        useful_links = section.findAll("a")
                        for link in useful_links:
                            nosql_object.set_useful_link(link)

                        nosql_list.append(nosql_object)
                        #print(nosql_object.get_description())
    nosql_list = set(nosql_list)
    return nosql_list


nosql_storage = NosqlStorage(get_databases_tags_new(""))
search = nosql_storage.search_by_model("Document Store")
nosql_storage.print_results(search)
#break_articles()
