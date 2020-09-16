import camelCase


from unittest import TestCase


class TestCamelCase(TestCase):

    def test_camel_case_sentence(self):
        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))
    

    def test_emptystring(self):
        self.assertEqual("Please enter something. No empty string allowed", camelCase.camel_case(""))

    def test_numbers_allowed(self):
        self.assertEqual("No numbers allowed. Please enter string only", camelCase.camel_case('1234567890'))

    def test_combinations_of_upper_lower_case(self):
        self.assertEqual('ahmedIsGoingHome', camelCase.camel_case('aHmeD is gOIng HoME'))

    def test_more_than_one_space_between_words(self):
        self.assertEqual('heIsHeadingHome', camelCase.camel_case('he  is   heading  home')) 

    def test_string_with_whitespace_at_the_start_and_at_the_end(self):
        self.assertEqual('heToldMeToGoAway', camelCase.camel_case(' he told me to go away ')) 

    def test_for_one_word(self):
        self.assertEqual('waiting', camelCase.camel_case('waiting')) 

    def test_camel_case_international(self):

        input_and_expected_outputs = {
            '你叫 什么 名字': '你叫什么名字',
            'Write a résumé': 'writeARésumé',
            'Über die Brücke': 'überDieBrücke',
            'Fahre über die Brücke': 'fahreÜberDieBrücke',
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camelCase.camel_case(input_val))   







