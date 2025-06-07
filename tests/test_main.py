from src.main import main

def test_main() -> None:
    result = main()
    assert result is None

def test_empty() -> None:
    assert True
