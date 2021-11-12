import os


class FileManager:
    def get_working_directory():
        """
        Return a unicode string representing the current
        working directory.
        """
        return os.getcwd()

    def path_split(path):
        """
        Split a pathname. Returns tuple "(head, tail)" where "tail" is
        everything after the final slash. Either part may be empty.
        """
        return os.path.split(path)

    def path_join(path, *paths):
        """
        Join two or more pathname components, inserting '/' as needed.
        If any component is an absolute path, all previous path components
        will be discarded. An empty last part will result in a path that
        ends with a separator.
        """
        return os.path.join(path, *paths)
