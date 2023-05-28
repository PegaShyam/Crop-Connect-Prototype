list_of_ordered_crops = ["apple", "banana", "blackgram", "chickpea", "coconut",
                                 "coffee", "cotton", "grapes", "jute", "kidneybeans",
                                 "lentil", "maize", "mango", "mothbeans", "mungbean",
                                 "muskmelon", "orange", "papaya", "pigeonpeas",
                                 "pomegranate", "rice", "watermelon"]
li=[0]*22
li[list_of_ordered_crops.index('grapes')]=1
tem=[3]
print(li)
li2=tem+li
print(li2)