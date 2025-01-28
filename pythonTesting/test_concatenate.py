from concat import concatenate
import pytest



def test_concat():
    assert concatenate("om","man") == "omman"
    assert concatenate("hello", "hi") == "hellohi"
