def calculate_love_score(name1,name2):
    word1="TRUE".lower()
    word2="LOVE".lower()
    
    combined_name = (name1+name2).lower()
    true_count = 0
    love_count = 0
    
    for i in combined_name:
        if i in word1:
            true_count+=1
        if i in word2:
            love_count+=1
            
    print (str(true_count)+str(love_count))
    
calculate_love_score("Kanye West", "Kim Kardashian")