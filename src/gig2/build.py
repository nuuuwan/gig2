# from gig2.build_regions import build_regions
# from gig2.build_census import build_census
from gig2.build_elections import build_elections

from gig2.metadata import infer_metadata


def build():
    # build_regions()
    # build_census()
    build_elections()
    infer_metadata()


if __name__ == '__main__':
    build()
