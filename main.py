import re


def create_clean_users_list(userfile_or_list, from_file=True, list_it=False, logs=False):

    if from_file:
        usernames = []
        filename = userfile_or_list
        with open(filename, 'r') as file_users:
            for line in file_users:
                if line == '\n':
                    continue
                #remove the whitespaces
                line = line.replace(" ", "")
                splitedline = re.split(' |,', line)
                for xxx in splitedline:
                    if xxx != '':
                        usernames.append(xxx)
    else:
        usernames = list(userfile_or_list)

    usernames_clean = []
    
    
    usernames_clean = [] if list_it else ''

    for username in usernames:
        # lowercase the name
        username = username.lower()

        # remove http.
        try:
            url_to_catch = 'instagram.com'
            username = username[username.index('instagram.com')+len(url_to_catch)+1:]
        except ValueError:
            pass # not contain the url in name

        # remove the keyid relavant directive
        username = re.sub(r'\?utm_source.*', '', username)
        username = re.sub(r'\?igshid.*', '', username)
        username = re.sub(r'\?utm_medium.*', '', username)

        # remove non letters/numbers/periods/underscore from name
        validLetters = "abcdefghijklmnopqrstuvwxyz._1234567890"
        username = ''.join([char for char in username if char in validLetters])

        # create a list based on usernames
        if list_it:
            usernames_clean.append(username)
        else:  # string ready
            usernames_clean += username + '\n'
        
    if logs:
        print('Number of users:{} \nusers:{}'.format(len(usernames_clean), usernames_clean))
        
    return usernames_clean
