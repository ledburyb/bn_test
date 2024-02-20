import re
import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

positive_location_matcher = Matcher(nlp.vocab)
positive_patterns = [
    [{"LOWER": "from"}, {"ENT_TYPE": "GPE"}],
    [{"LOWER": "in"}, {"ENT_TYPE": "GPE"}],
    [{"LOWER": "relocate"}, {"LOWER": "to"}, {"ENT_TYPE": "GPE"}],
]
positive_location_matcher.add("PositivePreference", positive_patterns)

negative_location_matcher = Matcher(nlp.vocab)
negative_patterns = [
    [{"LOWER": "outside"}, {"ENT_TYPE": "GPE"}],
    [{"LOWER": "outside"}, {"LOWER": "of"}, {"ENT_TYPE": "GPE"}],
]
negative_location_matcher.add("NegativePreference", negative_patterns)

# TODO: In future this would be trained against a corpus of known job roles
job_title_matcher = Matcher(nlp.vocab)
job_title_patterns = [
    [{"LOWER": "designer"}],
    [{"LOWER": "design"}],
    [{"LOWER": "developer"}],
    [{"LOWER": "marketing"}],
    [{"LOWER": "marketer"}],
    [{"LOWER": "internship"}],
]
job_title_matcher.add("JobTitle", job_title_patterns)

def extract_location_preferences(text):
    doc = nlp(text)
    positive_matches = positive_location_matcher(doc)
    negative_matches = negative_location_matcher(doc)

    positive_locations = []
    negative_locations = []

    for _, _, end in positive_matches:
        positive_locations.append(doc[end - 1].text.lower())

    for _, _, end in negative_matches:
        negative_locations.append(doc[end - 1].text.lower())

    return {
        "positive": positive_locations,
        "negative": negative_locations
    }

def extract_job_title_keywords(candidate_bio):
    job_titles = []
    doc = nlp(candidate_bio)
    matches = job_title_matcher(doc)
    for _, _, end in matches:
        job_titles.append(doc[end - 1].text.lower())
    return job_titles
