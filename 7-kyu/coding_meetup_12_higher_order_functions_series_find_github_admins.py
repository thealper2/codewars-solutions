def find_admin(lst, lang): 
    return [item for item in lst if item['language'] == lang and item['githubAdmin'] == 'yes']
