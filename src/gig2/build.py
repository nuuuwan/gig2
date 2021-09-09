# from gig2.build_regions import build_regions
# from gig2.build_census import build_census
from gig2.metadata import infer_metadata


def build():
    # build_regions()
    # build_census()
    infer_metadata()


if __name__ == '__main__':
    build()
