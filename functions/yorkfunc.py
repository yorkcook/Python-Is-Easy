def singer():
    best_singer = 'Frank Sinatra'
    return best_singer

def song_name():
    hit_song = 'Come Fly With Me'
    return hit_song

def song_summary():
    summary = 'Frank Sinatra released the hit Come Fly With Me in 1958. You might also recongized it from the movie Catch Me If You Can starring Leonardo DiCaprio!'
    return summary

def best_singer(name):
    if name == 'Sinatra':
        return print(f'You better believe that it is: {True}!')
        # return True
    else:
        return print(f'You must be not very bright cause that is: {False}')


print('Singer Name:', singer())

print('Song Name:', song_name())

print('Song Description:', song_summary())

print(best_singer('Sinatra'))

print(best_singer('York in the shower'))

