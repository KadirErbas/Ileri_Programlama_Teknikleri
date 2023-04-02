#!/usr/bin/env python
# coding: utf-8

# In[15]:


"""
    Oluşturulan metot parametre olarak 6 sayı(tahmin edilen sayılar) gönderilecek.
    Metot 1-49 arası sayı arasında 6 adet sayı tutacak, kaç tane tahminin tuttuğunu yazacak.
"""

import random

guess=[]
for i in range(6):
    num = int(input(f"{i+1}. sayıyı giriniz: "))
    guess.append(num)

lottery(set(guess))


# In[11]:


def lottery(guess):
    lottery_numbers = random.sample(range(1,50),6)
    matches = set(lottery_numbers).intersection(set(guess))
    print("Loto numaraları:", lottery_numbers)
    print(f"Tahminleriniz: {guess}")
    print(f"Tahminlerinizden {len(matches)} tanesi doğru!")


# In[ ]:




