seconds=eval(input("enter the integer for seconds"))
mins=seconds//60
remainingseconds=seconds%60
hours=mins/60
print(hours)
print(seconds, "seconds is", mins,"minutes and", remainingseconds, "seconds")