# outreach/message_templates.py

FINOVIA_COMPANY_URL = "https://www.linkedin.com/company/110907918"
POSOVIA_COMPANY_URL = "https://www.linkedin.com/company/110932178"

FINOVIA_PDF_URL = "https://drive.google.com/file/d/1eRyN6XCwGrmKh732-_at8M9YdRJfk9PK/view?usp=sharing"
POSOVIA_PDF_URL = "https://drive.google.com/file/d/1-t2P7Sr_pq41v7Dtv1UnAf6RSY_7nAbt/view?usp=sharing"


def _first_name(full_name: str | None) -> str:
    if not full_name:
        return ""
    return full_name.split(" ")[0]


# ============================================================
# Connection notes
# ============================================================

def build_connection_note(investor: dict) -> str:
    """
    Entry point: returns the correct connection note
    based on investor["source_product"].
    """
    product = (investor.get("source_product") or "").lower()

    if product == "finovia":
        return build_finovia_connection_note(investor)
    elif product == "posovia":
        return build_posovia_connection_note(investor)
    elif product in ("investor", "general_investor"):
        return build_investor_connection_note(investor)
    else:
        return build_generic_connection_note(investor)


def build_finovia_connection_note(investor: dict) -> str:
    name = _first_name(investor.get("name"))
    greeting = f"Hi {name}," if name else "Hi,"

    return (
        f"{greeting} I’m building Finovia, an infrastructure layer for Tier 1/2 banks, "
        "asset managers, private credit funds, and market operators launching digital products. "
        "Would love to connect and share how we’re unifying execution, settlement, and reporting into a single layer."
    )


def build_posovia_connection_note(investor: dict) -> str:
    name = _first_name(investor.get("name"))
    greeting = f"Hi {name}," if name else "Hi,"

    return (
        f"{greeting} I’m building POSOVIA, a unified retail infrastructure stack for operators who’ve "
        "outgrown consumer-grade tools like Square, Toast, and Shopify. POSOVIA merges POS, inventory, "
        "payments, accounting, and settlement into one operational and financial source of truth. "
        "Would be great to connect."
    )


def build_investor_connection_note(investor: dict) -> str:
    """
    For angels, VCs, PE, SaaS/fintech investors.
    """
    name = _first_name(investor.get("name"))
    greeting = f"Hi {name}," if name else "Hi,"

    return (
        f"{greeting} I’m building a unified financial and commerce infrastructure stack with two products on the same core engine. "
        "Finovia is the financial settlement and accounting layer; POSOVIA is the omnichannel POS and commerce system built directly on top of it. "
        "Would love to connect with people who think in systems, not just features."
    )


def build_generic_connection_note(investor: dict) -> str:
    name = _first_name(investor.get("name"))
    greeting = f"Hi {name}," if name else "Hi,"

    return (
        f"{greeting} I’m building infrastructure in fintech and commerce and would love to connect "
        "and share what we’re shipping."
    )


# ============================================================
# Post-accept messages
# ============================================================

def build_post_accept_message(investor: dict) -> str:
    """
    Entry point: returns the correct post-accept message
    based on investor["source_product"].
    """
    product = (investor.get("source_product") or "").lower()

    if product == "finovia":
        return build_finovia_post_accept(investor)
    elif product == "posovia":
        return build_posovia_post_accept(investor)
    elif product in ("investor", "general_investor"):
        return build_investor_post_accept(investor)
    else:
        return build_generic_post_accept(investor)


def _thanks_line(investor: dict) -> str:
    name = _first_name(investor.get("name"))
    return (
        f"Thanks for connecting — I appreciate it, {name}."
        if name
        else "Thanks for connecting — I appreciate it."
    )


def build_finovia_post_accept(investor: dict) -> str:
    first = _thanks_line(investor)
    return (
        f"{first}\n\n"
        "I’m building a unified financial and commerce infrastructure stack with two products that sit on the same core engine. "
        "Finovia is the financial settlement and accounting layer, and POSOVIA is the omnichannel POS and commerce system built directly on top of it.\n\n"
        "I’m reaching out because I’m opening early conversations with investors who understand infrastructure‑level products and the value of consolidating "
        "execution, settlement, accounting, and commerce into a single operating layer. This is the direction I’m building toward, and I’m looking to connect "
        "with people who think in systems, not features.\n\n"
        "Here are brief overviews of both products:\n"
        f"Finovia → {FINOVIA_PDF_URL}\n"
        f"POSOVIA → {POSOVIA_PDF_URL}\n\n"
        "If it makes sense, I’d be glad to share more context or walk through the roadmap.\n\n"
        "No pressure — just connecting with people who understand where this kind of infrastructure is going."
    )


def build_posovia_post_accept(investor: dict) -> str:
    first = _thanks_line(investor)
    return (
        f"{first}\n\n"
        "I’m building a unified financial and commerce infrastructure stack with two products that sit on the same core engine. "
        "Finovia is the financial settlement and accounting layer, and POSOVIA is the omnichannel POS and commerce system built directly on top of it.\n\n"
        "On the POSOVIA side, I’m talking with operators and owners who think in systems — people who see the cost of juggling separate tools "
        "for POS, inventory, payments, and accounting, and want a single operational and financial layer instead.\n\n"
        "Here are brief overviews of both products:\n"
        f"Finovia → {FINOVIA_PDF_URL}\n"
        f"POSOVIA → {POSOVIA_PDF_URL}\n\n"
        "If it makes sense, I’d be glad to share more context or walk through the roadmap.\n\n"
        "No pressure — just connecting with people who understand where this kind of infrastructure is going."
    )


def build_investor_post_accept(investor: dict) -> str:
    """
    For general investors (angels, VCs, PE, SaaS/fintech investors).
    Uses your exact investor framing.
    """
    first = _thanks_line(investor)
    return (
        f"{first}\n\n"
        "I’m building a unified financial and commerce infrastructure stack with two products that sit on the same core engine. "
        "Finovia is the financial settlement and accounting layer, and POSOVIA is the omnichannel POS and commerce system built directly on top of it.\n\n"
        "I’m reaching out because I’m opening early conversations with investors who understand infrastructure‑level products and the value of consolidating "
        "execution, settlement, accounting, and commerce into a single operating layer. This is the direction I’m building toward, and I’m looking to connect "
        "with people who think in systems, not features.\n\n"
        "Here are brief overviews of both products:\n"
        f"Finovia → {FINOVIA_PDF_URL}\n"
        f"POSOVIA → {POSOVIA_PDF_URL}\n\n"
        "If it makes sense, I’d be glad to share more context or walk through the roadmap.\n\n"
        "No pressure — just connecting with people who understand where this kind of infrastructure is going."
    )


def build_generic_post_accept(investor: dict) -> str:
    first = _thanks_line(investor)
    return (
        f"{first}\n\n"
        "I’m building infrastructure for fintech and commerce and sharing the buildout along the way. "
        "Happy to keep you in the loop as we ship."
    )


# ============================================================
# Follow-up messages
# ============================================================

def build_followup_message(investor: dict) -> str:
    """
    Entry point: returns the correct follow-up message
    based on investor["source_product"].
    """
    product = (investor.get("source_product") or "").lower()

    if product == "finovia":
        return build_finovia_followup(investor)
    elif product == "posovia":
        return build_posovia_followup(investor)
    elif product in ("investor", "general_investor"):
        return build_investor_followup(investor)
    else:
        return build_generic_followup(investor)


def build_finovia_followup(investor: dict) -> str:
    return (
        "Quick follow-up: if your team is exploring new rails, digital products, or wants a cleaner "
        "infrastructure layer for risk, settlement, and reporting, I’m happy to walk through how we’re "
        "approaching Finovia and the unified engine behind both products. Even a 15-minute architecture-level "
        "chat could be useful as a reference point."
    )


def build_posovia_followup(investor: dict) -> str:
    return (
        "Quick follow-up: a lot of operators we talk to are stuck between multiple systems "
        "(POS, inventory, payments, accounting) that never fully reconcile. POSOVIA is our answer to that. "
        "If you’d like, I can share a concrete view of what unified operations and financial truth look like "
        "when everything sits on one infrastructure layer."
    )


def build_investor_followup(investor: dict) -> str:
    return (
        "Circling back in case a deeper look at the unified engine behind Finovia and POSOVIA would be useful. "
        "The interesting part isn’t just two products — it’s the shared infrastructure for execution, settlement, "
        "accounting, and commerce. Happy to walk through the architecture and roadmap if that’s in your wheelhouse."
    )


def build_generic_followup(investor: dict) -> str:
    return (
        "Circling back in case it’s helpful to see how we’re thinking about unified fintech/commerce infrastructure. "
        "Happy to share a concise walkthrough, no pitch."
    )
