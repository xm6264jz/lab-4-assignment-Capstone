

def camel_case(sentence):
   if sentence=="":
      return "Please enter something. No empty string allowed"
      
   if sentence.isnumeric():
      return "No numbers allowed. Please enter string only"

   else:  
      sentence_Split = sentence.split()
      my_List = [sentence_Split[0].lower()]

   #for loop   
      for j in range(1, len(sentence_Split)):
         word = sentence_Split[j].capitalize()
         my_List.append(word)
   
      return "" .join(my_List)



      
def main():
    
 
   sentence = input('Enter your sentence: ')
   camelcased= camel_case(sentence)
   print(camelcased) 
   
if __name__ == "__main__":
    main()