import itertools

def ring_writer():
    for idx in itertools.cycle(range(3)):
        written = 0
        print("opening file {}".format(idx))
        with open("ring{}.txt".format(idx), "w") as f:
            while True:
                line = yield
                print("writing line {} to file {}: {}".format(
                    written, idx, line))
                f.write(line+"\n")
                written = (written + 1) % 3
                if written == 0:
                    break


writer = ring_writer()

next(writer)
writer.send("file0 0")
writer.send("file0 1")
writer.send("file0 2")
writer.send("file1 0")
writer.send("file1 1")
writer.send("file1 2")
writer.send("file2 0")
writer.send("file2 1")
writer.send("file2 2")

