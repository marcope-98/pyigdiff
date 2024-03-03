from pyigdiff import ZipReader, DiffFinder

def pyigdiff(filepath):
    zip = ZipReader(filepath)
    df = DiffFinder(zip.getFollowers(), zip.getFollowing())
    return df.generate_report()
