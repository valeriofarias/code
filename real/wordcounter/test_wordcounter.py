import unittest
from wordcounter import counter, test_summary

class TestWordCounter(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(counter(''), 0)
        
    def test_one_word(self):
        self.assertEqual(counter('word'), 1)
    
    def test_two_words(self):
        self.assertEqual(counter('I am'), 2) 
        
    def test_remove_symbols(self):
        self.assertEqual(counter('I am , crazy : ! @ # $ % ^ & * ( ) _ + < > ? : . , ;'), 3)


class TestSummary(unittest.TestCase):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla semper dolor nisi, sit amet lobortis sem consectetur sed. Sed lectus enim, accumsan id lorem eget, facilisis sagittis nunc. Phasellus varius augue ipsum, non egestas ligula pulvinar id. Suspendisse interdum gravida venenatis. Sed finibus quam ut ornare consequat. Nam rutrum tellus nulla, tristique auctor libero cursus et. Morbi tincidunt facilisis odio in ultricies. Sed quis magna semper, cursus erat luctus, aliquam erat. Curabitur in feugiat est, a interdum libero. Suspendisse a facilisis magna. Phasellus euismod malesuada dui. Etiam facilisis ipsum et lectus efficitur iaculis. Etiam libero quam, ornare sit amet leo in, vestibulum dictum est. Nullam mattis ornare dolor in aliquam. Mauris nisl purus, finibus sit amet egestas et, mollis ac lorem. In fringilla enim dui, at condimentum nulla faucibus vitae. Sed ut mi id est dignissim gravida sed sed dui. Sed pharetra convallis rutrum. Nullam in orci quam. Pellentesque nec nisi purus. Pellentesque gravida tellus quis augue pulvinar, vitae venenatis nisi vestibulum. Cras ipsum ipsum, placerat eget faucibus sit amet, sodales ut urna. Integer rhoncus libero sem, a molestie dui rhoncus et. Phasellus ac eros non ante euismod sagittis ut eget nunc. Ut euismod nunc leo, vitae ornare neque euismod tempus. Aenean a porta dolor, et pharetra elit. In interdum.' 

    
    def test_if_text_has_between_150_and_200_words_with_210_words(self):
        self.assertEqual(test_summary(self.summary), False)
    
    def test_if_text_has_between_150_and_200_words_with_149_words(self):
        self.assertEqual(test_summary(' '.join(self.summary.split()[:149])), False)
        
    def test_if_text_has_between_150_and_200_words_with_175_words(self):
        self.assertEqual(test_summary(' '.join(self.summary.split()[:175])), True)
