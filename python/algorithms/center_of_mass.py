from __future__ import division


class GoUp(Exception):
    """
    Hack for GOTO.
    """
    pass


def get_max_len(sections):
    max_len = 0
    max_seg = ''

    # Get segments
    segments = get_segments(sections)
    print segments

    possible_segs = []

    for l in range(1, len(sections) // 2):
        for i in range(len(segments)):
            seg1 = segments[i]
            if len(seg1) != l:
                continue
            for j in range(i, len(segments)):
                seg2 = segments[j]
                if len(seg2) != l:
                    continue
                seg = '{}{}'.format(seg1, seg2)
                possible_segs.append(seg)

    possible_segs = list(set(possible_segs))

    for seg in possible_segs:
        segl = list(seg)
        lsegl = len(segl)
        m = sum([int(segl[x]) for x in range(lsegl)])
        wm = sum([int(segl[x]) * (x + 1) for x in range(lsegl)])
        qm = wm / m
        qd = (lsegl + 1) / 2.

        if qm == qd:
            if lsegl > max_len:
                max_len = lsegl
                max_seg = seg

    return max_len, max_seg


def get_segments(sections):
    # Make the input data usable
    # sections = list(sections)
    length = len(sections)

    if length < 1:
        return None

    # Setup buffer for weights and segments
    segments = []

    for i in range(length):
        for j in range(i + 1, length):
            seg1 = sections[i:j]
            seg2 = seg1[::-1]

            # m1 = sum(seg1)
            # m2 = sum(seg2)
            # wm1 = sum([int(seg1[x]) * (x + 1) for x in range(j - i - 1)])
            # wm2 = sum([int(seg2[x]) * (x + 1) for x in range(j - i - 1)])

            # segments[j - i - 1].append([seg1, m1, wm1])
            # segments[j - i - 1].append([seg2, m2, wm2])sum(seg1)

            segments.append(seg1)
            segments.append(seg2)

    return segments


if __name__ == '__main__':
    sections = '131251141231'
    sections = '132231'
    max_len, max_seg = get_max_len(sections)
    print 'Max Length: {}'.format(max_len)
    print 'Segment:    {}'.format(max_seg)

    # import pprint
    # pprint.pprint(make_segments(sections))
