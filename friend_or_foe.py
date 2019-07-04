def friend(x):
    
    friend_list = []
    for name in x:
        if len(name) == 4:
            friend_list.append(name)
    return friend_list

def friend_bp(x):
    return [f for f in x if len(f) == 4]