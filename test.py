from main import create_clean_users_list

# file input test
usernames_clean = create_clean_users_list('tests/followers.txt', from_file=True, list_it=True, logs=False, rm_dup=False)
#print(usernames_clean)

# text input test
list_it = True
followers = ['zendigii', 'https://www.instagram.com/freedom_moses/', 'https://www.instagram.com/meitalbruner/',
 'https://www.instagram.com/avihay_dei/;', 'https://instagram.com/dry_wild_?igshid=1onso7ta4hddk']
 
expected_results = ['zendigii', 'freedom_moses', 'meitalbruner', 'avihay_dei', 'dry_wild_']

if len(followers) != len(expected_results):
    print('ERROR ! make expected_results and followers the same length')
    
usernames_clean = create_clean_users_list(followers, from_file=False, list_it=list_it, logs=True, rm_dup=False)
if list_it:
    for i, user in enumerate(usernames_clean):
        if user != expected_results[i]:
            print('FAIL!!!')
        else:
            print('PASS!!!')
else:
    print(usernames_clean)