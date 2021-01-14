from codestudy.models import Paper
import re
import string
import fuzzywuzzy.process


def search(terms, tags, user):
    """
    The search engine that returns a ranked result based on the search terms, tags and user. The search term uses
    Levenshtein distance to ranked the relevance to the search term. The tag is counted such that the number of tag in
    the portion search query that matches that in the database is linearly related to the ranking score. The proportion
    of the element that is in the search term but not in the database is linearly related to one minus the ranking
    score. The user is used to place a higher relevance to the papers that the user have bookmarked. The weighing of
    each factor is provided below.
    Weights:
    properties: 3/4
        title + description: 1/3
            title: 2/3
            description: 1/3
        tags: 1/3
            has_tag: 2/3
            no_tag: 1/3
        others: 1/3:
            star_count: 2/3
            field_search: 1/3
    star: 1/4
    :param terms: the search terms.
    :param tags: the search tags.
    :param user: the user logged in.
    :return: A list of paper, ranked.

    """
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    terms = _RE_COMBINE_WHITESPACE.sub(" ", terms).lower().translate(str.maketrans('', '', string.punctuation))
    tags = set(tags)
    texts = []
    text_scores = {}
    titles = []
    title_scores = {}
    descriptions = []
    descriptions_scores = {}
    scores = {}
    max_no_tag = 1
    max_bookmarker = 1
    for paper in Paper.objects.all():
        titles.append(paper.title)
        descriptions.append(paper.description)
        texts.append(paper.text)
        scores[paper] = 0
        if user and paper.is_bookmarked(user):
            scores[paper] += 1/4
        no_tag = 0
        for tag in paper.tags.all():
            if tag not in tags:
                no_tag += 1
        max_no_tag = max(max_no_tag, no_tag)
        max_bookmarker = max(max_bookmarker, paper.bookmarkers.count())
    fz = fuzzywuzzy.process.extract(terms, texts)
    for text, score in fz:
        text_scores[text] = score / 100
    fz = fuzzywuzzy.process.extract(terms, titles)
    for title, score in fz:
        title_scores[title] = score / 100
    fz = fuzzywuzzy.process.extract(terms, descriptions)
    for description, score in fz:
        descriptions_scores[description] = score / 100
    for paper in scores:
        scores[paper] += title_scores.get(paper.title, 0) * 3/4 * 1/3 * 2/3
        scores[paper] += descriptions_scores.get(paper.description, 0) * 3/4 * 1/3 * 1/3
        scores[paper] += text_scores.get(paper.text, 0) * 3/4 * 1/3 * 1/3
        scores[paper] += paper.bookmarkers.count() / max_bookmarker * 3/4 * 1/3 * 2/3
        tag_has = 0
        paper_tags = set([tag for tag in paper.tags.all()])
        for tag in tags:
            if tag in paper_tags:
                tag_has += 1
        scores[paper] += tag_has / max(1, len(tags)) * 3/4 * 1/3 * 2/3
        tag_no = 0
        for paper_tag in paper_tags:
            if paper_tag not in tags:
                tag_no += 1
        scores[paper] += (max_no_tag-tag_no) / max_no_tag * 3/4 * 1/3 * 1/3

    papers_ranked = [k for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)]
    return papers_ranked
