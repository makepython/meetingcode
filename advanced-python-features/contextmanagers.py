import contextlib
import tempfile
import shutil

class TempDir(object):
    def __init__(self):
        self._tmpdir = None

    def __enter__(self, *args):
        self._tmpdir = tempfile.mkdtemp()
        return self._tmpdir

    def __exit__(self, exc_class, exc, tb):
        if self._tmpdir is not None:
            try:
                print("removing", self._tmpdir)
                shutil.rmtree(self._tmpdir)
            except OSError:
                pass

        return False


@contextlib.contextmanager
def tempdir():
    tmp = tempfile.mkdtemp()
    try:
        yield tmp
    finally:
        try:
            shutil.rmtree(tmp)
        except OSError:
            pass


with tempdir() as tmp, TempDir() as tmp2:
    print(tmp, tmp2)

