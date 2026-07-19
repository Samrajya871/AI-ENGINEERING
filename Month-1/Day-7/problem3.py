words=""
count=0
def vowels_count(words,count):
    for i in words:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
        
        
    print("No of vowels", count)

vowels_count("samrajya",count)

    