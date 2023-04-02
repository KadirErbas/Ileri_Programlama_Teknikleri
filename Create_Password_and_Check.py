#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

num_users = 100
passwords = []

for i in range(num_users):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    passwords.append(password)
    print(f"Kullanıcı {i+1} için oluşturulan şifre: {password}")

print("Tüm şifreler:")
print(passwords)


# In[40]:


def check_passwords(passwords):
    wrong_password_index = 0
    for password in passwords:
        for i in range(len(password)-1):
            if password[i].isdigit() and password[i+1].isdigit():
                print(f"Hata: Indexi {wrong_password_index} olan şifrede yan yana iki veya daha fazla rakam var: {password} Bunlar: {password[i]} ve {password[i+1]}")
                return False
        wrong_password_index +=1
    return True


# In[41]:


check_passwords(passwords)


# In[ ]:





# In[ ]:




