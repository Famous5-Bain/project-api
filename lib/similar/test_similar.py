import similar 

example = [
    ("User1", "FilmA"), 
    ("User1", "FilmB"), 
    ("User2", "FilmC"), 
    ("User2", "FilmD"), 
    ("User2", "FilmE")
]


def test_sampledataset():
    assert len(example) == 5
