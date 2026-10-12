import sys

from dotenv import load_dotenv
from typesafe_sdk import Choice, TypeSafeClient

load_dotenv()

CATEGORIES = {
    "academic": "Belongs to a university, college, school, or research institution",
    "corporate": "Belongs to a company or commercial organisation",
    "non_academic_institution": "Belongs to a government body, hospital, NGO, or other non-company institution",
    "generic": "A free or consumer email provider such as gmail.com, qq.com, outlook.com, or yahoo.com",
}


def looks_like_email(s: str) -> bool:
    if not s or any(c.isspace() for c in s):
        return False
    if s.count("@") != 1:
        return False
    local, domain = s.split("@")
    if not local or not domain:
        return False
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in domain:
        return False
    return True


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("error: no email supplied", file=sys.stderr)
        print("usage: uv run classify_email.py EMAIL", file=sys.stderr)
        return 1

    email = argv[1]
    if not looks_like_email(email):
        print(f"error: not a valid email address: {email!r}", file=sys.stderr)
        print("usage: uv run classify_email.py EMAIL", file=sys.stderr)
        return 1

    client = TypeSafeClient()

    response = client.system_one(
        state={"email": email},
        questions={
            "institution_type": Choice(
                instructions="What kind of organisation does this email address belong to?",
                criteria=CATEGORIES,
            ),
        },
    )

    answer = response.answers["institution_type"]
    print(f"email      : {email}")
    print(f"category   : {answer.choice}")
    print(f"confidence : {answer.confidence:.2f}")
    print("probabilities:")
    for name, prob in sorted(answer.probabilities.items(), key=lambda kv: -kv[1]):
        print(f"  {prob:.2f}  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))