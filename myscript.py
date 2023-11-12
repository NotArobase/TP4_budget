import os


def git_bisect(bad_hash, good_hash, test_command):

    os.system(f'git bisect start {bad_hash} {good_hash}')

    os.system(f'git bisect run {test_command}')


if __name__ == "__main__":

    bad_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"
    good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c0"
    test_command = "python manage.py test"

    git_bisect(bad_hash, good_hash, test_command)