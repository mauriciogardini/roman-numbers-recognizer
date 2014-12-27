#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This program recognizes roman numbers from 1 to 3999.
'''


class RomanNumbersRecognizer(object):
    """
    Represents a class that recognizes roman numbers from 1 to 3999.
    """
    def __init__(self):
        self.text = None
        self.token_index = 0

    def recognize(self, input_text):
        """
        :param string input_text: The text to be processed.
        :return: A number, if the string translated to a valid number;
            or None, if the string was invalid.
        Initializes the recognition of an input text.
        """
        self.text = input_text
        self.token_index = 0
        result = self.check_thousands() + self.check_hundreds() + \
            self.check_decimals() +  self.check_ones()
        return result if self.token_index >= len(self.text) else None

    def get_next_token(self):
        """
        :return: A string character; or None, if there aren't any characters.
        Gets the next token.
        """
        return self.text[self.token_index]\
            if self.token_index < len(self.text) else None

    def check_thousands(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of characters that represent algarisms in
        the thousands place (M).
        """
        result = None
        if self.get_next_token() == 'M':
            self.token_index += 1
            result = 1000
            result += self.check_more_m()
            return result
        return 0

    def check_more_m(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of M characters.
        """
        result = None
        if self.get_next_token() == 'M':
            self.token_index += 1
            result = 1000
            result += self.check_yet_more_m()
            return result
        return 0

    def check_yet_more_m(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of M characters.
        """
        if self.get_next_token() == 'M':
            self.token_index += 1
            return 1000
        return 0

    def check_hundreds(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of characters that represent algarisms in
        the hundreds place (C, D and M).
        """
        result = None
        if self.get_next_token() == 'C':
            self.token_index += 1
            result = 100
            if self.get_next_token() == 'M':
                self.token_index += 1
                return 900
            else:
                result += self.check_more_d_c()
                return result
        elif self.get_next_token() == 'D':
            self.token_index += 1
            result = 500
            result += self.check_more_c()
            return result
        return 0

    def check_more_d_c(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of D and C characters.
        """
        result = None
        if self.get_next_token() == 'D':
            self.token_index += 1
            result = 300
            result += self.check_more_c()
            return result
        elif self.get_next_token() == 'C':
            self.token_index += 1
            result = 100
            result += self.check_yet_even_more_c()
            return result
        return 0

    def check_more_c(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of C characters.
        """
        result = None
        if self.get_next_token() == 'C':
            self.token_index += 1
            result = 100
            result += self.check_even_more_c()
            return result
        return 0

    def check_even_more_c(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of C characters.
        """
        result = None
        if self.get_next_token() == 'C':
            self.token_index += 1
            result = 100
            result += self.check_yet_even_more_c()
            return result
        return 0

    def check_yet_even_more_c(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of C characters.
        """
        if self.get_next_token() == 'C':
            self.token_index += 1
            return 100
        return 0

    def check_decimals(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of characters that represent algarisms in
        the decimals place (X, L and C).
        """
        result = None
        if self.get_next_token() == 'X':
            self.token_index += 1
            result = 10
            result += self.check_more_x_l_c()
            return result
        elif self.get_next_token() == 'L':
            self.token_index += 1
            result = 50
            result += self.check_more_x()
            return result
        return 0

    def check_more_x_l_c(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of X, L and C characters.
        """
        result = None
        if self.get_next_token() == 'X':
            self.token_index += 1
            result = 10
            result += self.check_yet_even_more_x()
            return result
        elif self.get_next_token() == 'L':
            self.token_index += 1
            result = 30
            return result
        elif self.get_next_token() == 'C':
            self.token_index += 1
            return 80
        return 0

    def check_more_x(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of X characters.
        """
        result = None
        if self.get_next_token() == 'X':
            self.token_index += 1
            result = 10
            result += self.check_even_more_x()
            return result
        return 0

    def check_even_more_x(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of X characters.
        """
        result = None
        if self.get_next_token() == 'X':
            self.token_index += 1
            result = 10
            result += self.check_yet_even_more_x()
            return result
        return 0

    def check_yet_even_more_x(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of X characters.
        """
        if self.get_next_token() == 'X':
            self.token_index += 1
            return 10
        return 0

    def check_ones(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of characters that represent algarisms in
        the ones place (I, V and X).
        """
        result = None
        if self.get_next_token() == 'I':
            self.token_index += 1
            result = 1
            result += self.check_more_i_v_x()
            return result
        elif self.get_next_token() == 'V':
            self.token_index += 1
            result = 5
            result += self.check_more_i()
            return result
        return 0

    def check_more_i_v_x(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of I, V and X characters.
        """
        result = None
        if self.get_next_token() == 'I':
            self.token_index += 1
            result = 1
            result += self.check_yet_even_more_i()
            return result
        if self.get_next_token() == 'V':
            self.token_index += 1
            return 3
        if self.get_next_token() == 'X':
            self.token_index += 1
            return 8
        return 0

    def check_yet_even_more_i(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of I characters.
        """
        if self.get_next_token() == 'I':
            self.token_index += 1
            return 1
        return 0

    def check_more_i(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of I characters.
        """
        result = None
        if self.get_next_token() == 'I':
            self.token_index += 1
            result = 1
            result += self.check_even_more_i()
            return result
        return 0

    def check_even_more_i(self):
        """
        :return: A number which was the result of the checking.
        Checks for the existence of I characters.
        """
        result = None
        if self.get_next_token() == 'I':
            self.token_index += 1
            result = 1
            result += self.check_yet_even_more_i()
            return result
        return 0


if __name__ == '__main__':
    RECOGNIZER = RomanNumbersRecognizer()
    while True:
        INPUT_TEXT = (raw_input('Write a roman number. '))
        RECOGNIZEMENT = RECOGNIZER.recognize(INPUT_TEXT)
        print '%s - %s' % (INPUT_TEXT, RECOGNIZEMENT) if RECOGNIZEMENT \
            else '%s - %s' % (INPUT_TEXT, 'Invalid number')
