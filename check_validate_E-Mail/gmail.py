email = input("Enter your Email: ")  # g@g.in,wscube@gmail.com
k,j,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")== 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if(i.isspace()):
                        k=1
                    elif i.isalpha():
                        if  i.isupper():
                            j =1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i =="." or i =="@":
                        continue
                    else:
                        d =1
                if k==1 or j ==1 or d==1:
                    print("wrong email 5")
                else: 
                    print("Right Email ")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1 ")




# email = input("Enter your Email: ")  # Example: g@g.in, wscube@gmail.com

# k, j, d = 0, 0, 0
# allowed_tlds = ["com", "in", "org", "net"]
# allowed_symbols = "._@"

# if len(email) >= 6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@") == 1):

#             # Get username and domain parts
#             username, domain = email.split("@")

#             # Extra checks start here

#             if ".." in email:
#                 print("❌ Invalid: Consecutive dots not allowed")

#             elif email[0] in allowed_symbols or email[-1] in allowed_symbols:
#                 print("❌ Invalid: Cannot start or end with special characters")

#             elif domain.startswith(".") or domain.endswith("."):
#                 print("❌ Invalid: Domain cannot start or end with dot")

#             elif ".." in domain:
#                 print("❌ Invalid: Double dot in domain part")

#             elif not domain.replace(".", "").isalnum():
#                 print("❌ Invalid: Domain name must be alphabetic or digits only")

#             elif not username.replace(".", "").replace("_", "").isalnum():
#                 print("❌ Invalid: Username contains invalid characters")

#             elif not ((email[-4] == ".") ^ (email[-3] == ".")):
#                 print("❌ Invalid: Dot (.) not at valid position")

#             else:
#                 # Loop through characters
#                 for i in email:
#                     if i.isspace():
#                         k = 1
#                     elif i.isalpha():
#                         if i.isupper():
#                             j = 1
#                     elif i.isdigit():
#                         continue
#                     elif i in allowed_symbols:
#                         continue
#                     else:
#                         d = 1

#                 # Check last part (TLD)
#                 tld = email.split(".")[-1]
#                 if tld not in allowed_tlds:
#                     print("❌ Invalid: TLD must be .com, .in, .org or .net")

#                 elif k == 1:
#                     print("❌ Invalid: Email contains space")
#                 elif j == 1:
#                     print("❌ Invalid: Email contains uppercase letter")
#                 elif d == 1:
#                     print("❌ Invalid: Email contains disallowed character")
#                 else:
#                     print("✅ Valid Email")
#         else:
#             print("❌ Invalid: '@' error (missing or multiple)")
#     else:
#         print("❌ Invalid: Email must start with a letter")
# else:
#     print("❌ Invalid: Email length should be at least 6")
