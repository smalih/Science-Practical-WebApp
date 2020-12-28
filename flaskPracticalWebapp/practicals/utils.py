def getDegStudyTitle(degStudy):
    if degStudy == "gcse":
        return degStudy.upper()
    return f"{degStudy[0].upper()} {degStudy[1].upper()}{degStudy[2:]}"

def getSubjectTitle(subject):
    return f"{subject[0].upper}{subject[1].lower()}"
