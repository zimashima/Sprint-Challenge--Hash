def finder(files, queries):

    hash_finder = { q: True for q in queries}

    result = []

    for i in files:
        new = i.split("/")[-1]
        if new in hash_finder:
            result.append(i)
            
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
