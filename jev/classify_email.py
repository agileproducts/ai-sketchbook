import sys
from dataclasses import dataclass, field

from dotenv import load_dotenv
from typesafe_sdk import Choice, TypeSafeClient

load_dotenv()

INVALID = "invalid"

CATEGORIES = {
    "academic": "Belongs to a university, college, school, or research institution",
    "corporate": "Belongs to a company or commercial organisation",
    "non_academic_institution": "Belongs to a government body, hospital, NGO, or other non-company institution",
    "generic": "A free or consumer email provider such as gmail.com, qq.com, outlook.com, or yahoo.com",
}


@dataclass
class Classification:
    email: str
    category: str
    confidence: float | None = None
    probabilities: dict[str, float] = field(default_factory=dict)

    @property
    def is_valid(self) -> bool:
        return self.category != INVALID


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


def classify(email: str, client: TypeSafeClient) -> Classification:
    if not looks_like_email(email):
        return Classification(email=email, category=INVALID)

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
    return Classification(
        email=email,
        category=answer.choice,
        confidence=answer.confidence,
        probabilities=dict(answer.probabilities),
    )


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("error: no email supplied", file=sys.stderr)
        print("usage: uv run classify_email.py EMAIL", file=sys.stderr)
        return 1

    result = classify(argv[1], TypeSafeClient())

    print(f"email      : {result.email}")
    print(f"category   : {result.category}")
    if result.confidence is None:
        print("source     : structural check (no API call)")
        return 0
    print(f"confidence : {result.confidence:.2f}")
    print("probabilities:")
    for name, prob in sorted(result.probabilities.items(), key=lambda kv: -kv[1]):
        print(f"  {prob:.2f}  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))