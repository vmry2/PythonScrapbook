# with open(
#     "test.txt", "w"
# ) as f:  # using file context manager; automatically closes the file at the end of the block
# f_contents = f.read(100)  # reads only 100 characters
# print(f_contents, end="")

# for line in f:    # reads one line at a time
#     print(line, end="")

# f_contents = f.read()

# f_contents = f.readline()
# print(f_contents, end="")

# size_to_read = 10
# f_contents = f.read(size_to_read)

# while len(f_contents) > 0:
#     print(f_contents, end="")
#     f_contents = f.read(size_to_read)

# f.write("Test first line")
# f.seek(0)
# f.write("Test2")

# f = open("test.txt", "r")
# print(f.name)
# f.close()

# with open("test.txt", "r") as rf:
#     with open("text_copy.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)

with open(
    "test.jpg", "rb"
) as rf:  # Opens the file in binary format, because source is an image
    with open(
        "text_copy.jpg", "wb"
    ) as wf:  # Saves the destination file in binary format
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk)> 0
        wf.write(rf_chunk)

        rf_chunk = rf.read(chunk_size)
