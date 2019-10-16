import sys
import random

# RANDOMIZEDMOTIFSEARCH(Dna, k, t)
# randomly select k-mers Motifs = (Motif1, ... , Motift) in each string from Dna
# BestMotifs Motifs
# while forever
# Profile PROFILE(Motifs)
# Motifs MOTIFS(Profile, Dna)
# if SCORE(Motifs) < SCORE(BestMotifs)
# BestMotifs Motifs
# else
# return BestMotifs
def profile(motif):
    dnaProfile = []
    for i in range(len(motif[0])):
        numA = 0
        numC = 0
        numG = 0
        numT = 0
        for dna in motif:
            if dna[i].lower() == 'a':
                numA += 1
            elif dna[i].lower() == 'c':
                numC += 1
            elif dna[i].lower() == 'g':
                numG += 1
            elif dna[i].lower() == 't':
                numT += 1
        profA = numA / len(motif)
        profC = numC / len(motif)
        profG = numG / len(motif)
        profT = numT / len(motif)

        dnaProfile.append([profA, profC, profG, profT])
    return dnaProfile

def motifs(profile, dna, k):
    motif = []
    for seq in dna:
        bestScore = 0
        bestSeq = ''
        for i in range(len(seq) - k - 1):
            dnaStr = seq[i:i+k]
            k = 0
            score = 1
            for nuc in dnaStr:
                if nuc.lower() == 'a':
                    score *= profile[k][0]
                elif nuc.lower() == 'c':
                    score *= profile[k][1]
                elif nuc.lower() == 'g':
                    score *= profile[k][2]
                elif nuc.lower() == 't':
                    score *= profile[k][3]
                k+=1
            if bestScore < score:
                bestScore = score
                bestSeq = dnaStr
            else:
                bestSeq = dnaStr
        motif.append(bestSeq)
    return motif

def score(motif, k):
    score = 0
    for i in range(k):
        dnaList = dict()
        minKey = ''
        for dna in motif:
            if dna[i].lower() not in dnaList:
                dnaList[dna[i].lower()] = 1
            else:
                dnaList[dna[i].lower()] += 1
        while len(dnaList) != 1:
            minKey = min(dnaList, key=dnaList.get)
            score += dnaList[minKey]
            del(dnaList[minKey])
    return score

# def score(strings, k):
#         i = 0
#         setScore = 0
#         while i < len(strings):
#                 counts = [0,0,0,0] #ACGT
#                 for seq in strings:
#                         if seq[i] == "A":
#                                 counts[0] += 1
#                         elif seq[i] == "C":
#                                 counts[1] += 1
#                         elif seq[i] == "G":
#                                 counts[2] += 1
#                         elif seq[i] == "T":
#                                 counts[3] += 1
#                 maxval = max(counts)
#                 for num in counts:
#                         if num != maxval:
#                                 setScore += num
#                 i+=1
#         return(setScore)

def randomMotifSearch(dna, k):
    motif = []
    for dnaStr in dna:
        i = random.randint(0, len(dnaStr) - int(k))
        motif.append(dnaStr[i:i+int(k)])
    bestMotif = motif
    while True:
        dnaProfile = profile(motif)
        motif = motifs(dnaProfile, dna, int(k))
        if score(bestMotif, k) > score(motif, k):
            bestMotif = motif
        else:
            return bestMotif

dnaFile = open(sys.argv[1])
num = dnaFile.readline().strip()
k, t = num.split()
dnaList = []
for line in dnaFile:
    dnaList.append(line.strip())
bestScore = float('Inf')
bestMotif = []
for i in range(int(100000)):
    currentMotif = randomMotifSearch(dnaList, int(k))
    if score(currentMotif, int(k)) < bestScore:
        bestScore = score(currentMotif, int(k))
        print(bestScore)
        for member in currentMotif:
            print(member)
        bestMotif = currentMotif
# for member in bestMotif:
#     print(member)
