import unittest
import filecmp
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    '''def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)
        with self.assertRaises(FileNotFoundError):
            freqlist = cnt_freq('n')
            freqlist = cnt_freq(1)

    def test_lt_and_eq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(ascii, freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(lst.index(HuffmanNode(101, 0)), 0)
        self.assertEqual(lst.index(HuffmanNode(100, 16)), 6)
        self.assertEqual(lst.index(HuffmanNode(97, 2)), 2)
        self.assertFalse(HuffmanNode(97, 2) == None)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

        second_tree = create_huff_tree([])
        self.assertEqual(None, second_tree)

        # new
        freq_list_3 = cnt_freq('empty_file.txt')
        third_tree = create_huff_tree(freq_list_3)
        self.assertEqual(None, third_tree)

        freq_list_4 = cnt_freq('letters.txt')
        fourth_tree = create_huff_tree(freq_list_4)
        self.assertEqual(25, fourth_tree.freq)
        self.assertEqual(97, fourth_tree.char)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

        # new
        freqlist2 = cnt_freq('empty_file.txt')
        self.assertEqual(create_header(freqlist2), '')

        freqlist3 = cnt_freq('letters.txt')
        self.assertEqual(create_header(freqlist3), '97 25')

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')
        self.assertEqual(codes[ord(' ')], '')

    def test_create_code_2(self):
        freq_list_2 = cnt_freq("file_spaces.txt")
        huff_tree_2 = create_huff_tree(freq_list_2)
        codes_2 = create_code(huff_tree_2)
        self.assertEqual(codes_2[ord(' ')], '')

    def test_create_code_3(self):
        freq_list_2 = cnt_freq("file_spaces_multiline.txt")
        huff_tree_2 = create_huff_tree(freq_list_2)
        codes_2 = create_code(huff_tree_2)
        self.assertEqual(codes_2[ord(' ')], '1')

    def test_inexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode('does_not_exist.txt', 'does_not_exist_out.txt')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_03_textfile(self):
        huffman_encode("empty_file.txt", "empty_file_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_file_out.txt empty_file.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb empty_file_out_compressed.txt empty_file.txt", shell=True)
        self.assertEqual(err, 0)

    def test_04_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb multiline_out_compressed.txt multiline_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_05_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_06_textfile(self):
        huffman_encode("same_freq.txt", "same_freq_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb same_freq_out.txt same_freq_soln.txt", shell=True)
        self.assertEqual(err, 0)
        '''

    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
                    0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)

    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_02_test_file1_decode(self):
        huffman_decode("letters_out_compressed.txt", "letters_decoded.txt")
        err = subprocess.call("diff -wb letters.txt letters_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_04_test_file1_decode(self):
        huffman_decode("file_spaces_multiline_out_compressed.txt", "file_spaces_multiline_decoded.txt")
        err = subprocess.call("diff -wb file_spaces_multiline.txt file_spaces_multiline_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_05_test_file1_decode(self):
        huffman_decode("file2_compressed_soln.txt", "file2_decoded.txt")
        err = subprocess.call("diff -wb file2.txt file2_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_06_test_file1_decode(self):
        huffman_decode("file_spaces_out_compressed.txt", "file_spaces_decoded.txt")
        err = subprocess.call("diff -wb file_spaces.txt file_spaces_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_07_test_file1_decode(self):
        huffman_decode("multiline_compressed_soln.txt", "multiline_decoded.txt")
        err = subprocess.call("diff -wb multiline.txt multiline_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_08_test_file1_decode(self):
        huffman_decode("same_freq_out_compressed.txt", "same_freq_decoded.txt")
        err = subprocess.call("diff -wb same_freq.txt same_freq_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_empty_file_02(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode('does_not_exist.txt', 'does_not_exist_out.txt')

    def test_09_test_file1_decode(self):
        huffman_decode("numbers_out_compressed.txt", "numbers_decoded.txt")
        err = subprocess.call("diff -wb numbers.txt numbers_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_10_test_file1_decode(self):
        huffman_decode("single_char_out_compressed.txt", "single_char_decoded.txt")
        err = subprocess.call("diff -wb single_char.txt single_char_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_11_test_file1_decode(self):
        huffman_decode("newline_only_out_compressed.txt", "newline_only_decoded.txt")
        err = subprocess.call("diff -wb newline_only.txt newline_only_decoded.txt", shell=True)
        self.assertEqual(err, 0)


if __name__ == '__main__':
    unittest.main()
