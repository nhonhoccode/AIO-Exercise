def evaluate_classification_model(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
        return
    if not isinstance(fp, int):
        print("fp must be int")
        return
    if not isinstance(fn, int):
        print("fn must be int")
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1_score:.2f}")


if __name__ == "__main__":
    evaluate_classification_model(2, 3, 4)
    evaluate_classification_model('a', 3, 5)
