#Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
#Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
#No additional characters are allowed except for those mentioned.
#Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :]

#Example cases:

#countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
#countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
#countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;


def count_smileys(arr): 

    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    faces = []

# Craete a list of all possible faces
    for e in eyes:
        for n in noses:
            for m in mouths:
                face = e + n + m
                faces.append(face)
# Best Practice: count += arr.count(face)
 # Is the face acceptable   
    for elm in arr :
        if elm in faces:
            count += 1
    print(count)
    return count
 

count_smileys([';D', ':-(', ':-)', ';~)'])