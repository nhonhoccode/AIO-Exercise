def word_count(file_path):
    counter = {}
    with open(file_path, 'r') as f:
        data = f.read()
    data = data.lower()
    data = data.split()
    for word in data:
        counter[word] = counter.get(word, 0) + 1
    return counter


if __name__ == "__main__":
    file_path = 'D:\AIO_2024\AIO-Exercise\mod01_w02\P1_data.txt'
    print(word_count(file_path))
