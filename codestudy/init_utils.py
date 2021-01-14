from .models import TagClass, Tag


def populate_new_database():
    """
    The client asked to have some specific tags, but because of the generality of the tag systems, the specific tags
    have to added manually. The function adds them programmatically.
    """
    tags_groups = {
        'Approaches': [
            'Biological',
            'Cognitive',
            'Sociocultural',
        ],
        'Topics': [
            'Brain & Behavior',
            'Hormones and pheromones and their effects on behavior',
            'The relationship between genetics and behavior',
            'Cognitive processes',
            'The reliability of cognitive processes',
            'Emotion and cognition',
            'The individual and the group',
            'Cultural origins of behavior and cognition',
            'Cultural influences on behavior',
        ],
        'Content': []
    }
    for tag_class, tags in tags_groups.items():
        tc = TagClass(name=tag_class)
        tc.save()
        for tag in tags:
            Tag(tag_class=tc, name=tag).save()

