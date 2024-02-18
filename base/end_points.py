url = 'https://reqres.in/api/'
end_point = dict()

'''GET'''
end_point['list_users'] = f'{url}users?page='
end_point['single_user'] = f'{url}users/' #patch put


'''POST'''
end_point['create_user'] = f'{url}users'
end_point['register'] = f'{url}register'
end_point['login'] = f'{url}login'



