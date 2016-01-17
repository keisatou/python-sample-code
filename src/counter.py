""""use case of collections.Counter."""
from collections import Counter


def most_common(arr):
    """use case of collections.Counter.most_common()."""
    return Counter(arr).most_common(1)

if __name__ == '__main__':
    values = [
        'hoge',
        'hoge',
        'hoge',
        'fuga',
        'fuga',
    ]
    print(most_common(values))
