def awesome_activated(person1, person2, cool_factor = None):
    if person1 == 'York' and person2 == 'Gabe':
        return True
    elif person1 != 'York' and person2 !='Gabe' and cool_factor >= int("8"):
        return True
    else:
        return False

print(awesome_activated("York", "Gabe"))

print(awesome_activated("John", "Doe", 3))

print(awesome_activated("Jane", "Doe", 8))
