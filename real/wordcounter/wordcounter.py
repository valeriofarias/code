"""
You're in a project which objective is to create a bank of theses summary and you're responsible to create a robot that make sure that all summaries have to have between 150 and 200 words. The quality of platform depends on this filter.

You should do first a funciont to count words and after that you can do another function to test summary between 150 and 200 words. 
 
"""
def test_summary(text):
    return True if counter(text) > 149 and counter(text) < 201 else False

def counter(text): 
    punctuation = '!@#$%^&*()_+<>?:.,;'
    
    for char in text:
        if char in punctuation:
            text = text.replace(char, '')
      
    temp = text.split() 
    return len(temp)
     
