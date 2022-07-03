import xml_elements

class problem_in_library(xml_elements.single_tag):
    #name = ""
    #properties = {}
    #dash = 0

    def __init__(self, dash=0):
        super().__init__(dash)
        self.name = "problem"

    def add_url(self, url_value):
         self.add_property("url_name", url_value)

class library(xml_elements.intermediate_container):
    #name = ""
    #properties = {}
    #dash = 0
    #list = list()

    def __init__(self, dash=0):
        super().__init__(dash)
        self.name = "library"

    def add_opening(self, text):
        res_str = "<" + self.name
        res_str += " xblock-family=\"xblock.v1\""
        if (self.properties).get("display_name") == None:
            print("Warning! The display name of the test not found. Used \"Test\". You have to add it to the final file manually.")
        if (self.properties).get("org") == None:
            print("Warning! Organization name not found. Used \"LETI\". You have to add it to the final file manually.")
        if (self.properties).get("library") == None:
            print("Warning! Library name not found. Used \"Test\". You have to add it to the final file manually.")
        res_str += " display_name=\"" + (self.properties).get("display_name", "Test") + "\""
        res_str += " org=\"" + (self.properties).get("org", "LETI") + "\""
        res_str += " library=\"" + (self.properties).get("library", "Test") + "\""
        text.append(' ' * self.dash + res_str + ">")

    def add_problem(self, problem_url):
        new_problem = problem_in_library(self.dash + 2)
        new_problem.add_url(problem_url)
        self.list.append(new_problem)

    def add_display_name(self, value):
        self.add_property("display_name", value)

    def add_org(self, value):
        self.add_property("org", value)

    def add_library(self, value):
        self.add_property("library", value)




