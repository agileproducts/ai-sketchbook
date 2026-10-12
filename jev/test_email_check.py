import pytest

from classify_email import INVALID, Classification, looks_like_email

INVALID_CASES = [
    "",
    "banana",
    "not-an-email",
    "@gmail.com",
    "alice@",
    "a@@b.com",
    "a b@c.com",
    "\talice@x.com",
    "alice@localhost",
    ".alice@x.com",
    "alice.@x.com",
    "a..b@x.com",
    "alice@.com",
    "alice@x..com",
]

VALID_CASES = [
    "alice@mit.edu",
    "zhangsan@zju.edu.cn",
    "first.last+tag@sub.domain.co.uk",
    "x@a.io",
    "user_name@example-domain.org",
]


@pytest.mark.parametrize("candidate", INVALID_CASES)
def test_rejects_non_email_shapes(candidate):
    assert not looks_like_email(candidate)


@pytest.mark.parametrize("candidate", VALID_CASES)
def test_accepts_realistic_addresses(candidate):
    assert looks_like_email(candidate)


@pytest.mark.parametrize("candidate", INVALID_CASES)
def test_invalid_category_returns_without_api_call(candidate):
    from classify_email import classify

    result = classify(candidate, client=None)

    assert result.category == INVALID
    assert result.confidence is None
    assert result.probabilities == {}
    assert not result.is_valid


def test_is_valid_helper():
    assert Classification(email="a@b.com", category="academic").is_valid
    assert not Classification(email="banana", category=INVALID).is_valid