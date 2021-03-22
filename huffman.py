from ordered_list import OrderedList
from huffman_bit_writer import HuffmanBitWriter
from huffman_bit_reader import HuffmanBitReader


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the freqency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''

        if other is None:
            return False
        if type(other) is HuffmanNode:
            if (self.char == other.char) and (self.freq == other.freq):
                return True
        return False

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''

        if self.freq == other.freq:
            if self.char < other.char:
                return True
            else:
                return False
        elif self.freq < other.freq:
            return True
        else:
            return False


def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    try:
        file_input = open(filename, "r")
        contents = file_input.read()
        file_input.close()
    except:
        raise FileNotFoundError

    list_freq = 256 * [0]
    for i in range(len(contents)):
        list_freq[ord(contents[i])] += 1

    return list_freq


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''

    if not char_freq:
        return None

    huff_tree = OrderedList()

    for i in range(len(char_freq)):
        if char_freq[i] > 0:
            '''adds in the frequency and then the char
                is sorted by the frequency'''
            huff_tree.add(HuffmanNode(i, char_freq[i]))

    while huff_tree.size() > 1:
        first = huff_tree.pop(0)
        second = huff_tree.pop(0)

        huffman_branch = HuffmanNode(min(first.char, second.char), (first.freq + second.freq))
        huffman_branch.left = first
        huffman_branch.right = second

        huff_tree.add(huffman_branch)

    #if huff_tree.is_empty():
       # return None
    else:
        return huff_tree.pop(0)


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    if node is None:
        return [''] * 256
    else:
        return create_code_rec_help(node, '', [''] * 256)


def create_code_rec_help(node, level, code_list):
    if (node.left is None) and (node.right is None):
        code_list[node.char] = level
        return code_list

    else:
        create_code_rec_help(node.left, level + '0', code_list)
        create_code_rec_help(node.right, level + '1', code_list)

    return code_list


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    stringOfValues = ''

    for i in range(len(freqs)):
        if freqs[i] > 0:
            stringOfValues = stringOfValues + str(i) + ' ' + str(freqs[i]) + ' '

    return stringOfValues[:-1]


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''

    list_char_count = cnt_freq(in_file)

    huff_tree_root = create_huff_tree(list_char_count)
    header_string = create_header(list_char_count)
    list_of_codes = create_code(huff_tree_root)

    # opens out text file
    # writes header
    text_file = open(out_file, "w")
    text_file.write(header_string)

    # opens compressed text file
    # writes header
    compressed_text_file = HuffmanBitWriter(out_file[:-4] + '_compressed.txt')
    compressed_text_file.write_str(header_string)

    if huff_tree_root:
        text_file.write('\n')
        compressed_text_file.write_str('\n')

        with open(in_file) as file_input:
            contents = file_input.read()
            for y in range(len(contents)):
                text_file.write(list_of_codes[ord(contents[y])])
                compressed_text_file.write_code(list_of_codes[ord(contents[y])])

    text_file.close()
    compressed_text_file.close()





def huffman_decode(encoded_file, decode_file):
    try:
        read = HuffmanBitReader(encoded_file)
    except:
        raise FileNotFoundError

    header = read.read_str()

    parsed_list = parse_header(header)
    recreated_tree = create_huff_tree(parsed_list)

    count_range = 0
    for y in parsed_list:
        count_range += y

    writer_file = open(decode_file, "w")


    for i in range(0, count_range):
        node = recreated_tree
        cont = True
        while cont == True:
            if (node.left is None) and (node.right is None):
                writer_file.write(chr(node.char))
                cont = False
            else:

                bit_value = read.read_bit()

                if bit_value:
                    node = node.right

                if not bit_value:
                    node = node.left

    writer_file.close()
    read.close()


def parse_header(byte_string):
    list_of_values = byte_string.split()
    list_of_freq = [0] * 256
    for i in range(0, len(list_of_values), 2):
        list_of_freq[int(list_of_values[i])] = int(list_of_values[i + 1])
    return list_of_freq


