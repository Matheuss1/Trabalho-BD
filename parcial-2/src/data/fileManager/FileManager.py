import os


class FileManager:
    def get_working_directory():
        """ Return a unicode string representing the current
        working directory. """
        return os.getcwd()

    def path_split(path):
        """ Split a pathname. Returns tuple "(head, tail)" where "tail" is
        everything after the final slash. Either part may be empty. """
        return os.path.split(path)

    def path_join(path, *paths):
        return os.path.join(path, *paths)
