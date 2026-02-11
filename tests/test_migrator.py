import pytest
from src.migrator import contains_domain, replace_domain

def test_contains_domain():
    """Test the regex matching for domain identification."""
    # Valid matches
    assert contains_domain("user@abc.edu", "abc.edu") is True
    assert contains_domain("first.last@abc.edu", "abc.edu") is True
    assert contains_domain("admin-123@abc.edu", "abc.edu") is True
    
    # Invalid matches (should be ignored)
    assert contains_domain("user@xyz.edu", "abc.edu") is False
    assert contains_domain("user@abc.edu.com", "abc.edu") is False
    assert contains_domain("abc.edu@other.com", "abc.edu") is False
    assert contains_domain("user@notabc.edu", "abc.edu") is False

def test_replace_domain():
    """Test the regex substitution for domain replacement."""
    # Standard replacements
    assert replace_domain("user@abc.edu", "abc.edu", "xyz.edu") == "user@xyz.edu"
    assert replace_domain("first.last@abc.edu", "abc.edu", "new.org") == "first.last@new.org"