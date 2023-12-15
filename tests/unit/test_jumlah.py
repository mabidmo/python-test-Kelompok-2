from src.jumlah import jumlah
def test_jumlah_salah():
    assert not jumlah(3) == 5

def test_jumlah_benar():
    assert jumlah(3) == 4