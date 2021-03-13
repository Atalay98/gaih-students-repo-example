#!/usr/bin/env python
# coding: utf-8

# In[15]:


#create dictionary to keep 10 questions. Questions as key, answers as value
questions = {"Türkiye'nin başkenti neresidir? ": "Ankara",
            "Türkiye'de kaç il vardır? ": 81,
            "Baklavası ile ünlü şehrimiz hangisidir? " : "Gaziantep",
            "Türkiye'de nüfusu en çok olan il hangisidir? ": "Istanbul",
            "'Fe' hangi elementin simgesidir? ": "Demir",
            "Amerika bayrağında kaç yıldız vardır? ": 50,
            "Türkiye Cumhuriyeti hangi yıl kurulmuştur? ": 1923,
            "Kaç tane rakam vardır? ": 10,
            "Nüfusu en çok olan ülke hangisidir? ": "Çin",
            "3 basamaklı rakamları farklı en büyük sayı kaçtır? ": 987}

totalCorrect = 0

for k,v in questions.items():
    print("Doğru Sayınız: ",totalCorrect)
    cevap = input(k)
    if type(v)==int :
        answer = 0
        try:
            answer = int(cevap)
        except ValueError:
            print("Hatalı yanıt verdiniz. Doğru cevap: ", v)
            continue
        if(answer == v):
            totalCorrect += 1
        else:
            print("Hatalı yanıt verdiniz. Doğru cevap: ", v)
            
    else:
        userAnswer = cevap.upper()
        correctAnswer = v.upper()
        if(userAnswer == correctAnswer):
            totalCorrect += 1
        else:
            print("Hatalı yanıt verdiniz. Doğru cevap: ", v)
    
if(totalCorrect > 5):
    print("Tebrikler. Kazandınız. Puanınız: ", totalCorrect*10)
else:
    print("Başarılı olamadınız. Puanınız: ", totalCorrect*10)


# In[ ]:




