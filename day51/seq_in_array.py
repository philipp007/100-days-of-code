def seq_in_array(seq, array):
    seq_len = len(seq)

    for i in range(0, len(array) - seq_len + 1):
        if seq == array[i:i+seq_len]:
            return True

    return False


def main():
    test = seq_in_array([1, 3, 4], [5, 2, 7, 1, 3, 4])
    print(test)


if __name__ == '__main__':
    main()
