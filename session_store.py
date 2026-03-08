sessions = {}

def track_session(user):

    if user not in sessions:
        sessions[user] = 1
    else:
        sessions[user] += 1

    return sessions[user]