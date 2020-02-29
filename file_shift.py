from pathlib import Path
import shutil
import errors


def file_shift(src, semester):
    """
    :type src: Path
    :type semester: Semester
    :return:
    """
    if not src.exists():
        raise errors.InvalidSource(src)
    smpl = 'sample'
    dst = src

    for file in src.iterdir():
        for course in semester.courses:
            if [eval(param, locals(), globals()) for param in course.params]:
                dst = course.dir
            shutil.copy(str(src), str(dst))


