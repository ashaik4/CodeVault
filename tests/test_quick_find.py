# tests/test_unionfind.py
import pytest
from src.quick_find import UnionFind
from tests.logging_config import configure_logging

# Initialize logging
log = configure_logging()


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Ensure logging is configured for the test session."""
    log.info("Starting test session.")
    yield
    log.info("Test session finished.")


def test_unionfind_init():
    uf = UnionFind(5)
    assert uf.root == [0, 1, 2, 3, 4]

def test_find():
    uf = UnionFind(5)
    assert uf.find(3) == 3

def test_union():
    uf = UnionFind(5)
    uf.union(1, 2)
    assert uf.root[1] == 2
    assert uf.isConnected(1, 2)

def test_isConnected():
    uf = UnionFind(5)
    assert not uf.isConnected(1, 2)
    uf.union(1, 2)
    assert uf.isConnected(1, 2)

def test_exception_handling():
    uf = UnionFind(5)
    with pytest.raises(IndexError):
        uf.find(6)

def test_union_find_connections():
    uf = UnionFind(10)

    # Perform unions: 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)

    # Assertions for connectivity
    assert uf.isConnected(1, 5), "1 and 5 should be connected"
    assert uf.isConnected(5, 7), "5 and 7 should be connected"
    assert not uf.isConnected(4, 9), "4 and 9 should not be connected"

    # Perform additional union: 9-4
    uf.union(9, 4)

    # Assertions after new union
    assert uf.isConnected(4, 9), "4 and 9 should now be connected"