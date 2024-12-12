# Mrs Knuth Part II - Actions

Actions in Mrs. Knuth - Part II are identical in format to actions in Mrs. Knuth - Part I. One possible action is needed for each student for each day/hour of the student’s availability. The possible actions in the example test case are:

```text
('place student', 'Drew', 'Trombone', 'F', 10)
('place student', 'Drew', 'Trombone', 'F', 11)
('place student', 'Drew', 'Trombone', 'F', 1)
('place student', 'Ella', 'Flute', 'F', 10)
('place student', 'Ella', 'Flute', 'F', 1)
('place student', 'Lola', 'Drums', 'F', 11)
('place student', 'Lola', 'Drums', 'F', 1)
```

Next, we identify the requirements satisfied by each of those actions. I’ll add the full list of requirements and optional requirements so that the next segment captures a full model of the example test case for Mrs. Knuth – Part II.

```text
Requirements:
    ('student scheduled', 'Drew')
    ('student scheduled', 'Ella')
    ('student scheduled', 'Lola')

Optional Requirements:
    ('slot filled', 'F', 8)
    ('slot filled', 'F', 9)
    ('slot filled', 'F', 10)
    ('slot filled', 'F', 11)
    ('slot filled', 'F', 1)
    ('instrument on day', 'F', 'Trombone')
    ('instrument on day', 'F', 'Drums')
    ('instrument on day', 'F', 'Flute')
    (('Ella', 'F', 10), ('Drew', 'F', 11))
    (('loud instrument', 'F', 8), ('loud instrument', 'F', 9))
    (('loud instrument', 'F', 9), ('loud instrument', 'F', 10))
    (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))

Action: ('place student', 'Drew', 'Trombone', 'F', 10)
    Satisfied Requirements: ('student scheduled', 'Drew')
                            ('slot filled', 'F', 10)
                            ('instrument on day', 'F', 'Trombone')
                            (('loud instrument', 'F', 9), ('loud instrument', 'F', 10))
                            (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))

Action: ('place student', 'Drew', 'Trombone', 'F', 11)
    Satisfied Requirements: ('student scheduled', 'Drew')
                            ('slot filled', 'F', 11)
                            ('instrument on day', 'F', 'Trombone')
                            (('Ella', 'F', 10), ('Drew', 'F', 11))
                            (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))

Action: ('place student', 'Drew', 'Trombone', 'F', 1)
    Satisfied Requirements: ('student scheduled', 'Drew')
                            ('slot filled', 'F', 1)
                            ('instrument on day', 'F', 'Trombone')

Action: ('place student', 'Ella', 'Flute', 'F', 10)
    Satisfied Requirements: ('student scheduled', 'Ella')
                            ('slot filled', 'F', 10)
                            ('instrument on day', 'F', 'Flute')
                            (('Ella', 'F', 10), ('Drew', 'F', 11))

Action: ('place student', 'Ella', 'Flute', 'F', 1)
    Satisfied Requirements: ('student scheduled', 'Ella')
                            ('slot filled', 'F', 1)
                            ('instrument on day', 'F', 'Flute')

Action: ('place student', 'Lola', 'Drums', 'F', 11)
    Satisfied Requirements: ('student scheduled', 'Lola')
                            ('slot filled', 'F', 11)
                            ('instrument on day', 'F', 'Drums')
                            (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))

Action: ('place student', 'Lola', 'Drums', 'F', 1)
    Satisfied Requirements: ('student scheduled', 'Lola')
                            ('slot filled', 'F', 1)
                            ('instrument on day', 'F', 'Drums')
```

