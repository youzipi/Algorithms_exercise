# with open("./tinyUF.txt", 'r') as f:
import os.path

import pytest

from python.algs.dynamic_connectivity import UF
from python.algs.dynamic_connectivity2 import QuickUnion
from python.algs.dynamic_connectivity3 import WeightedQuickUnionUF

CUR_DIR = os.path.dirname(__file__)


def process(file_path, clazz):
    with open(file_path, 'r') as f:
        n = int(f.readline())
        print("number=", n)
        a = clazz(n)
        for line in f:
            points = [int(i) for i in line.split()]
            p = points[0]
            q = points[1]
            if (not a.connected(p, q)):
                a.union(p, q)
    return a.count


def test_tiny():
    count = process(os.path.join(CUR_DIR, "tinyUF.txt"), clazz=UF)
    assert count == 2


def test_tiny_quick():
    count = process(os.path.join(CUR_DIR, "tinyUF.txt"), clazz=QuickUnion)
    assert count == 2


"""
benchmark
"""


@pytest.mark.benchmark(
    group="medium",
    disable_gc=True,
)
def test_medium(benchmark):
    count = benchmark(process, os.path.join(CUR_DIR, "mediumUF.txt"), clazz=UF)
    assert count == 3


@pytest.mark.benchmark(
    group="medium",
    disable_gc=True,
)
def test_medium_quick(benchmark):
    count = benchmark(process, os.path.join(CUR_DIR, "mediumUF.txt"), clazz=QuickUnion)
    assert count == 3


@pytest.mark.benchmark(
    group="medium",
    disable_gc=True,
)
def test_medium_weighted(benchmark):
    count = benchmark(process, os.path.join(CUR_DIR, "mediumUF.txt"), clazz=WeightedQuickUnionUF)
    assert count == 3


@pytest.mark.benchmark(
    group="large",
    min_rounds=3,
    disable_gc=True,
)
def test_large_quick(benchmark):
    count = benchmark(process, os.path.join(CUR_DIR, "largeUF.txt"), clazz=QuickUnion)
    assert count == 6


@pytest.mark.benchmark(
    group="large",
    min_rounds=3,
    disable_gc=True,
)
def test_large_weighted(benchmark):
    count = benchmark(process, os.path.join(CUR_DIR, "largeUF.txt"), clazz=WeightedQuickUnionUF)
    assert count == 6
