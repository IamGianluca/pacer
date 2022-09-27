from typing import List


def func(savings: List[float]) -> List[float]:
    budget_avail: float = 0
    n_years: int = len(savings)
    result: List[float] = list()

    for t in range(n_years):
        ideal = (budget_avail + sum(savings[t:])) / len(savings[t:])
        budget_avail += savings[t]

        investment = min(budget_avail, ideal)

        result.append(investment)
        budget_avail -= investment

    return result
