import pytest

from classify_email import looks_like_email

INVALID = [
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

VALID = [
    "alice@mit.edu",
    "zhangsan@zju.edu.cn",
    "first.last+tag@sub.domain.co.uk",
    "x@a.io",
    "user_name@example-domain.org",
]


@pytest.mark.parametrize("candidate", INVALID)
def test_rejects_non_email_shapes(candidate):
    assert not looks_like_email(candidate)


@pytest.mark.parametrize("candidate", VALID)
def test_accepts_realistic_addresses(candidate):
    assert looks_like_email(candidate)