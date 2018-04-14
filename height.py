def feet_to_cm(height):
    if height == "4\'0\"":
        return 122
    elif height == "4\'1\"":
        return 124
    elif height == "4\'2\"":
        return 127
    elif height == "4\'3\"":
        return 130
    elif height == "4\'4\"":
        return 132
    elif height == "4\'5\"":
        return 135
    elif height == "4\'6\"":
        return 137
    elif height == "4\'7\"":
        return 140
    elif height == "4\'8\"":
        return 142
    elif height == "4\'9\"":
        return 145
    elif height == "4\'10\"":
        return 147
    elif height == "4\'11\"":
        return 150
    elif height == "5\'0\"":
        return 152
    elif height == "5\'1\"":
        return 152
    elif height == "5\'2\"":
        return 157
    elif height == "5\'3\"":
        return 160
    elif height == "5\'4\"":
        return 163
    elif height == "5\'5\"":
        return 165
    elif height == "5\'6\"":
        return 168
    elif height == "5\'7\"":
        return 170
    elif height == "5\'8\"":
        return 173
    elif height == "5\'9\"":
        return 175
    elif height == "5\'10\"":
        return 178
    elif height == "5\'11\"":
        return 180
    elif height == "6\'0\"":
        return 183
    elif height == "6\'1\"":
        return 185
    elif height == "6\'2\"":
        return 188
    elif height == "6\'3\"":
        return 191
    elif height == "6\'4\"":
        return 193
    elif height == "6\'5\"":
        return 196
    elif height == "6\'6\"":
        return 198
    elif height == "6\'7\"":
        return 201
    elif height == "6\'8\"":
        return 203
    else:
        return 205

def define_goal(customer_goal):
    goal = customer_goal.upper()
    if goal == "OTHER":
        return 1
    elif goal == "GAIN MUSCLE":
        return 2
    elif goal == "LOSE FAT":
        return 3
    elif goal == "COMPETE":
        return 4
    elif goal == "TRANSFORM MY BODY":
        return 5
    elif goal == "LIVE HEALTHIER":
        return 6
    elif goal == "IMPROVE FOR A SPORT":
        return 7
    else:
        return 8
