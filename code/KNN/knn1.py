from collections import Counter



def raw_majority_vote(labels: list[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


assert raw_majority_vote(['a', 'b', 'c', 'b']) == 'b'
