def isParticipantAMoreQualified(a, b, atSession):
    if a[atSession] > b[atSession]:
        return True
    elif a[atSession] < b[atSession]:
        return False
    else:
        return isParticipantAMoreQualified(a, b, atSession - 1)


tc = int(input())
for _ in range(tc):
    n, m = [int(q) for q in input().split()]
    participants = []
    x = input()  # participant name whom will be evaluated whether he qualified or not
    participantX = []
    qualifiedParticipant = 0
    for _ in range(n):
        t = input().split()
        if participantX == [] and t[0] == x:
            participantX.append(t[0])
            participantX += [int(q) for q in t[1:]]
        else:
            participant = [t[0]]
            participant += [int(q) for q in t[1:]]
            participants.append(participant)
    for participant in participants:
        if isParticipantAMoreQualified(participant, participantX, 3):
            qualifiedParticipant += 1
            if qualifiedParticipant == m:
                break
    if qualifiedParticipant + 1 <= m:
        print("YA")
    else:
        print("TIDAK")

# I got WA on my answer below,
# i didn't expect that M (total participant that will be qualified/selected),
# as mentioned on restriction (which i didn't read carefully), could be 0.
# Who the hell conduct a selection if no one would ever be selected?
# But, as the problem is listed on "competitive programming introduction" section, i think
# they want to enforce us to read the restrictions carefully.


# def isParticipantAMoreQualified(a, b, atSession):
#     if a[atSession] > b[atSession]:
#         return True
#     elif a[atSession] < b[atSession]:
#         return False
#     else:
#         return isParticipantAMoreQualified(a, b, atSession - 1)


# tc = int(input())
# for _ in range(tc):
#     n, m = [int(q) for q in input().split()]
#     participants = []
#     x = input()  # participant name whom will be evaluated whether he qualified or not
#     participantX = []
#     qualifiedParticipant = 0
#     participantXIsQualified = True
#     for _ in range(n):
#         t = input().split()
#         if participantX == [] and t[0] == x:
#             participantX.append(t[0])
#             participantX += [int(q) for q in t[1:]]
#         else:
#             participant = [t[0]]
#             participant += [int(q) for q in t[1:]]
#             participants.append(participant)
#     for participant in participants:
#         if isParticipantAMoreQualified(participant, participantX, 3):
#             qualifiedParticipant += 1
#             if qualifiedParticipant == m:
#                 participantXIsQualified = False
#                 break
#     if participantXIsQualified:
#         print("YA")
#     else:
#         print("TIDAK")
