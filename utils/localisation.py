import json
import string
meta = {
    "ACCOUNT_LOOKUP_OUTPUT":["zc","items"],
    "FILTERS_MESSAGE_INVITE_LINK":["mention"],
    "MODERATION_PRUNE_FAIL_INT":["amount"],
    "MODERATION_PRUNE_DELETING":["amount"],
    "ASSIGNMENT_TAG_SAVING":["name"],
    "ASSIGNMENT_TAG_PERM_0":["name"],
    "ASSIGNMENT_TAG_SUCCESS":["name"],
    "ASSIGNMENT_TAG_PERM_FAIL_GENERIC":["name"],
    "ASSIGNMENT_RTAG_SAVING":["name"],
    "ASSIGNMENT_RTAG_SUCCESS":["name"],
    "ASSIGNMENT_RTAG_FAIL":["name"],
    "ASSIGNMENT_ASSIGN_FINDING":["name"],
    "ASSIGNMENT_ASSIGN_SUCCESS":["name"],
    "ASSIGNMENT_ASSIGN_FAIL":["name"],
    "ASSIGNMENT_UNASSIGN_FINDING":["name"],
    "ASSIGNMENT_UNASSIGN_SUCCESS":["name"],
    "ASSIGNMENT_UNASSIGN_FAIL":["name"],
    "ASSIGNMENT_TAGS_SUCCESS":["tags"]
}

def read(key="*"):
    with open('utils/localisation.json', 'r+') as f:
        data = json.load(f)
        if key == "*":
            return data
        else:
            return data[key]

def write(key, value):
    with open('utils/localisation.json', 'r+') as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    return read(key)

def reset():
    with open('utils/localisation_backup.json', 'r+') as f:
        data = json.load(f)
    with open('utils/localisation.json', 'r+') as f:
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def localise(key, **vars):
    value = read(key)

    try:
        meta[key]
    except KeyError:
        return value

    value = string.Template(value)

    return value.substitute(**vars)
