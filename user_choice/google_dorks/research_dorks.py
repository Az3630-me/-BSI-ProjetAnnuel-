# import needed python library to open new browser window and submit requests
import user_choice.google_dorks.google_dorks_utils as gd

# test data, remove in other versions
# my_test_data = {
#     "Site": ["stackoverflow.com","github.com"],
#     "Mot-clé dans l'URL": [],
#     "Mot clé dans le titre": [],
#     "Mot clé dans le texte": [],
#     "Type de fichier": [],
#     "Plage de dates": {"Avant": "2024-02-17", "Après": "2024-02-17"},
#     "Cache" : []
# }

# main function that call all other functions, depending if their fields are empty or not
def research(test_data:dict):

    # create new request object and give as argument user's data dictionnary
    test_request = gd.User_resquest(test_data)

    # filter by site Google Dork, OR logic applied, triggered if site field is not empty
    if test_request.data_dict["site:"] != [] :
        test_request.multiple_choice_specified(test_request.data_dict["site:"],"site:"," OR ")

    # filter by keywords in URL Google Dork, AND logic applied, triggered if URL field is not empty
    if test_request.data_dict["inurl:"] != [] :
        test_request.multiple_choice_specified(test_request.data_dict["inurl:"], "inurl:"," AND ")

    # filter by keywords in title Google Dork, AND logic applied, triggered if title field is not empty
    if test_request.data_dict["intitle:"] != [] :
        test_request.multiple_choice_specified(test_request.data_dict["intitle:"], "intitle:"," AND ")

    # filter by keywords in text Google Dork, AND logic applied, triggered if text field is not empty
    if test_request.data_dict["intext:"] != [] :
        test_request.multiple_choice_specified(test_request.data_dict["intext:"], "intext:"," AND ")

    # filter by file type Google Dork, OR logic applied, triggered if filetype field is not empty
    if test_request.data_dict["filetype:"] != [] :
        test_request.multiple_choice_specified(test_request.data_dict["filetype:"], "filetype:"," OR ")
    
        # filter by cache of website Google Dork, OR logic applied, triggered if cache field is not empty
    if test_request.data_dict["cache:"] != [] :
        test_request.multiple_choice_specified(test_request.data_dict["cache:"],"cache:"," OR ")

    # filter given dates Google Dork, triggered if site field is not empty
    if (test_request.data_dict["start_date"] and test_request.data_dict["end_date"]) != "":
        test_request.date_range(test_request.data_dict["start_date"],test_request.data_dict["end_date"])

    # send request with Google dork(s)
    test_request.my_search()


