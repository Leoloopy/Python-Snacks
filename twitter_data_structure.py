users = [
    {
        "name": "Hadiza",
        "age": 21,
        "gender": "Female",
        "username": "deezah",
        "is_verified": False,
        "tweets": [{"contents": "PO for president", "likes": 450, "retweets": 233},
                   {"contents": "Atiku is our man", "likes": 4, "retweets": 2}]
    },

    {
        "name": "Ibrahim",
        "age": 45,
        "gender": "Male",
        "username": "Ibro",
        "is_verified": True,
        "tweets": [{"contents": "Programming is fun", "likes": 10, "retweets": 2},
                   {"contents": "Atiku is our man", "likes": 4, "retweets": 2}]
    },

    {
        "name": "James",
        "age": 25,
        "gender": "Male",
        "username": "amez",
        "is_verified": True,
        "tweets": [{"contents": "Rachael is my one and only love", "likes": 6, "retweets": 2},
                   {"contents": "Atiku is our man", "likes": 4, "retweets": 2}]
    },

    {
        "name": "Rachael",
        "age": 21,
        "gender": "Female",
        "username": "Betty",
        "is_verified": False,
        "tweets": [{"contents": ".", "likes": 1450, "retweets": 1330},
                   {"contents": "Thinking about amez", "likes": 4, "retweets": 2},
                   {"contents": "Amezing grace", "likes": 4, "retweets": 2}]
    },

    {
        "name": "Elijah",
        "age": 17,
        "gender": "Male",
        "username": "El_d_si",
        "is_verified": False,
        "tweets": [{"contents": "Osun Decides", "likes": 12, "retweets": 6},
                   {"contents": "imole-de", "likes": 8, "retweets": 12}]
    },

    {
        "name": "Dorris",
        "age": 16,
        "gender": "Female",
        "username": "anything_counts",
        "is_verified": False,
        "tweets": [{"contents": "I love Chimamanda Adichie", "likes": 450, "retweets": 233},
                   {"contents": "Feminism is the goal", "likes": 4000, "retweets": 12}]
    },

    {
        "name": "Jacob",
        "age": 37,
        "gender": "Male",
        "username": "elder_j",
        "is_verified": True,
        "tweets": [{"contents": "Reflection is my gola", "likes": 5, "retweets": 3},
                   {"contents": "How to get more likes on twitter", "likes": 3, "retweets": 0}]
    },

    {
        "name": "Derrick",
        "age": 29,
        "gender": "Male",
        "username": "standby_gen",
        "is_verified": False,
        "tweets": [{"contents": "PO for president", "likes": 450, "retweets": 233},
                   {"contents": "Atiku is our man", "likes": 4, "retweets": 2}]
    },

    {
        "name": "Mubarak",
        "age": 49,
        "gender": "Male",
        "username": "Whistle",
        "is_verified": True,
        "tweets": [{"contents": "PO for president", "likes": 450, "retweets": 233},
                   {"contents": "Atiku is our man", "likes": 4, "retweets": 2}]
    },
]

no_of_users = len(users)
usernames = {user['username'] for user in users}
female_users = [user['name'] for user in users if user['gender'] == 'Female']
inactive_user = [user for user in users if len(user['tweets']) == 0]
user_age = [user['age'] for user in users]
name_and_age = [{'name': user['name'] , 'age': user['age']} for user in users]
average_age_of_users = round(sum(user['age'] for user in users) / len(users))

print(usernames)
print(female_users)
print(inactive_user)
print(user_age)
print(name_and_age)
print(average_age_of_users)
