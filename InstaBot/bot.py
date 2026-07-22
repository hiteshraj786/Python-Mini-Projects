# from instabot import Bot
# bot =  Bot()
# bot.login(username = "rishi_prajapat_20",password = "@rahul123456")
# # bot.follow('wscubetechindia')
# # bot.upload_photo("C://Python Course//Python_Project//InstaBot//java.jpg",caption="i love java")
# # bot.unfollow("rashmika_mandanna")
# # bot.send_message("I love you Rahul",["_rahulprajapat_07"])
# # followers = bot.get_user_followers("rishi_prajapat_20")
# # for follower in followers:
# #     print(bot.get_user_info(follower))
# following = bot.get_user_following("rishi_prajapat_20")
# for Following in following:
#     print(bot.get_user_info(Following))


# from instagrapi import Client

# cl = Client()
# cl.login("rishi_prajapat_20", "@rahul123456")
# cl.photo_upload("java.jpg", "I love Java ❤️")

# from instagrapi import Client

# cl = Client()
# cl.login("rishi_prajapat_20", "@rahul123456")

# # 🔽 Username jisko message bhejna hai
# username = "wscubetechindia"
# user_id = cl.user_id_from_username("_rahulprajapat_07")

# # 🔽 Message text
# message = "I like you rahul"

# # 🔽 Send the message
# cl.direct_send(message, [user_id])

# print("Message sent successfully ✅")


# from instagrapi import Client

# # Step 1: Login
# cl = Client()
# cl.login("rishi_prajapat_20", "@rahul123456")

# # Step 2: Get your own user ID
# my_user_id = cl.user_id

# # Step 3: Get all followers
# followers = cl.user_followers(my_user_id)
# print(f"\n📌 Total Followers: {len(followers)}")
# print("📍 Followers List:")
# for user_id, user in followers.items():
#     print(f"➡️ Username: {user.username} | Name: {user.full_name}")

# # Step 4: Get all followings
# followings = cl.user_following(my_user_id)
# print(f"\n📌 Total Followings: {len(followings)}")
# print("📍 Followings List:")
# for user_id, user in followings.items():
#     print(f"➡️ Username: {user.username} | Name: {user.full_name}")


# setx PATH "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\Scripts\"
