# import needed library to open browser windo and submit requests
import webbrowser

# create our request class
class User_resquest:

    # initialize our Google dorks request object with user's data
    def __init__(self,user_data:dict):

        # initialize our user request
        self.user_request = ""

        # link user's data to corresponding Google dorks
        self.data_dict = {
            "site:": user_data["Site"],
            "inurl:": user_data["Mot-clé dans l'URL"],
            "intitle:": user_data["Mot clé dans le titre"],
            "filetype:" : user_data["Type de fichier"],
            "intext:": user_data["Mot clé dans le texte"],
            "cache:": user_data["Cache"],
            "start_date":user_data["Plage de dates"]["Avant"],
            "end_date": user_data["Plage de dates"]["Après"]
        }

    # function that open new browser tab and send request
    def my_search(self):
        webbrowser.open_new("https://www.google.com/search?q="+self.user_request)

    # function that reads user's data and transform them into a Google dork request
    def multiple_choice_specified(self,user_list: list, google_dork: str, logic_operator: str):
        formated_string = ""
        for i in user_list:
            if user_list.index(i) < (len(user_list) - 1):
                formated_string += (google_dork + str(i) + logic_operator)
            else:
                formated_string += (google_dork + str(i))
        self.user_request += (" "+formated_string)


    # function that filters using chosen dates
    def date_range(self,start_date:str, end_date:str):
        self.user_request += (" "+f"(before:{start_date} after:{end_date})")