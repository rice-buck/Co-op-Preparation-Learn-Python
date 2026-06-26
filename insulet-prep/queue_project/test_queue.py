#test_queue.py
import pytest

from queue_class import Queue

@pytest.fixture
def q():
    return Queue()

def test_new_queue_is_empty(q):
    assert q.is_empty()

def test_fifo_order(q):
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"

def test_enqueue_changes_emptiness(q):
    assert q.is_empty()
    q.enqueue(1)
    assert not q.is_empty()
    q.dequeue()
    assert q.is_empty()
    

def test_dequeue_empty_raises(q):
    with pytest.raises(IndexError):
        q.dequeue()

@pytest.mark.parametrize("items, expected_first", [
    ([1, 2, 3], 1),
    (["a", "b", "c", "d"], "a"),
    (["hello"], "hello"),
    ([], IndexError),
])

def test_dequeue_returns(q, items, expected_first):
    for it in items:
        q.enqueue(it)
    assert q.dequeue() == expected_first