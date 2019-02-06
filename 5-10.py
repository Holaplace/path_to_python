current_users = ['admin','a','b','c','d']
new_users = ['admin','g','h','j','k']

for new_user in new_users:
    if new_user in current_users:
        print('Used')
    else:
        print('Permitted')