import streamlit as st


def load_vocab(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


words = load_vocab(file_path="word.txt")


def levenshtein_distance(token1, token2):
    row_num = len(token1) + 1
    col_num = len(token2) + 1
    distances = [[0] * col_num for _ in range(row_num)]

    for t1 in range(row_num):
        distances[t1][0] = t1

    for t2 in range(col_num):
        distances[0][t2] = t2

    for t1 in range(1, row_num):
        for t2 in range(1, col_num):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                distances[t1][t2] = 1 + min(
                    distances[t1][t2 - 1],
                    distances[t1 - 1][t2],
                    distances[t1 - 1][t2 - 1],
                )

    return distances[len(token1)][len(token2)]


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word:")

    if st.button("Compute"):

        leven_distances = {}
        for vocab in words:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1])
        )
        correct_word = list(sorted_distances.keys())[0]
        st.write("Correct word: ", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary:")
        col1.write(words)
        col2.write("Distances:")
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
